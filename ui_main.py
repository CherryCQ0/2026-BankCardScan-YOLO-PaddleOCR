import warnings

from PIL.FitsImagePlugin import FitsGzipDecoder

warnings.filterwarnings("ignore")
import sys
import os
import time
import re

import cv2
import numpy as np
from ultralytics import YOLO
from PySide6.QtWidgets import QFileDialog, QHBoxLayout, QDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtGui, QtCore
from paddleocr import PaddleOCR
from PIL import Image, ImageDraw, ImageFont

from yoloQt import Ui_MainWindow



def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img, width, height, width * channel, QImage.Format_RGB888)


#图形界面按钮的方法绑定
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  # 加载pyside6的UI
        self.timer = QTimer()   # 加载定时器
        self.timer.setInterval(2000)  # 设置定时器触发时间
        self.video = None
        self.is_running = False
        self.weights_path = 'runs/train/exp/weights/best.pt'
        try:
            self.model = YOLO(self.weights_path)
            self.model(np.zeros((800, 800, 3)).astype(np.uint8))  #预先加载推理模型
        except:
            pass
        # 初始化conf和iou
        self.conf = self.doubleSpinBox_conf.value() if hasattr(self, 'doubleSpinBox_conf') else 0.5
        self.iou = self.doubleSpinBox_iou.value() if hasattr(self, 'doubleSpinBox_iou') else 0.7
        self.bind_slots()   # 事件绑定
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        # 视频/摄像头模式下的卡号稳定显示缓存
        self.ocr_text_cache = {}  # {track_id: {'text': str, 'count': int, 'last_box': tuple}}
        self.ocr_cache_threshold = 3  # 连续3帧相同才确认显示
        self.ocr_track_id = 0

    def bind_slots(self):
        self.Button_checkImg.clicked.connect(self.select_images)  # 检测图片
        self.Button_openCamera.clicked.connect(self.open_camera)  # 检测摄像头
        self.Button_checkVideo.clicked.connect(self.select_video)  # 检测视频
        # self.Button_select_folder.clicked.connect(self.select_folder)  # 检测文件夹
        self.Button_select_w_p.clicked.connect(self.select_weights)  # 选择权重
        self.pushButton_bofang.clicked.connect(self.run_stop)  # 播放暂停
        self.timer.timeout.connect(self.video_pred)
        # conf/iou参数绑定
        if hasattr(self, 'doubleSpinBox_conf'):
            self.doubleSpinBox_conf.valueChanged.connect(self.update_conf)
        if hasattr(self, 'doubleSpinBox_iou'):
            self.doubleSpinBox_iou.valueChanged.connect(self.update_iou)
        # horizontalSlider绑定
        if hasattr(self, 'horizontalSlider_conf'):
            self.horizontalSlider_conf.valueChanged.connect(self.update_hor_conf)
        if hasattr(self, 'horizontalSlider_iou'):
            self.horizontalSlider_iou.valueChanged.connect(self.update_hor_iou)

    def update_conf(self, value):
        self.conf = value
        if hasattr(self, 'horizontalSlider_conf'):
            self.horizontalSlider_conf.setValue(int(value * 100))

    def update_iou(self, value):
        self.iou = value
        if hasattr(self, 'horizontalSlider_iou'):
            self.horizontalSlider_iou.setValue(int(value * 100))

    def update_hor_conf(self, value):
        conf = value * 0.01
        self.conf = conf
        if hasattr(self, 'doubleSpinBox_conf'):
            self.doubleSpinBox_conf.setValue(conf)

    def update_hor_iou(self, value):
        iou = value * 0.01
        self.iou = iou
        if hasattr(self, 'doubleSpinBox_iou'):
            self.doubleSpinBox_iou.setValue(iou)

    def video_pred(self):
        ret, frame = self.video.read()
        if not ret:
            self.run_stop()
        else:
            # 进度条处理
            if hasattr(self, 'progressBar') and self.video:
                try:
                    current_frame = int(self.video.get(cv2.CAP_PROP_POS_FRAMES))
                    total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
                    if total_frames > 0:
                        percent = int(current_frame / total_frames * 100)
                        self.progressBar.setValue(percent)
                except Exception:
                    pass
            start_time = time.time()
            results = self.model(frame, conf=self.conf, iou=self.iou)
            end_time = time.time()
            img_bgr = results[0].plot()
            num = len(results[0].boxes)

            # ========== OCR 银行卡卡号识别 ==========
            img_src = frame.copy()
            img_pil = Image.fromarray(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(img_pil)

            for box in results[0].boxes.xyxy.cpu().numpy():
                x1, y1, x2, y2 = map(int, box)
                crop = img_src[max(0, y1):min(img_src.shape[0], y2),
                               max(0, x1 - 10):min(img_src.shape[1], x2 + 10)]

                if crop.size == 0:
                    continue

                ocr_result = self.ocr.ocr(crop, cls=True)
                if ocr_result and ocr_result[0]:
                    text = re.sub(r'[^0-9]', '', ''.join(
                        [line[1][0] for line in ocr_result[0]]))

                    if text:
                        box_height = y2 - y1
                        font_size = int(box_height * 0.6)
                        font_size = max(font_size, 12)
                        font = ImageFont.truetype("simhei.ttf", font_size)
                        y_text = y2 + int(box_height * 0.2) if y2 + int(box_height * 0.2) < img_bgr.shape[
                            0] else y2 - font_size
                        draw.text((x1, y_text), text, font=font, fill=(255, 0, 0))

            img_bgr = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            # ========== OCR 结束 ==========

            if hasattr(self, 'label_nums'):
                self.label_nums.setText(str(num))
            if hasattr(self, 'label_times'):
                self.label_times.setText(f"{(end_time - start_time)*1000:.1f} ms")
            # 自动保存视频帧
            if hasattr(self, 'checkBox_isSave') and self.checkBox_isSave.isChecked():
                save_dir = r'./save_result'
                os.makedirs(save_dir, exist_ok=True)
                if not hasattr(self, 'video_writer') or self.video_writer is None:
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    h, w = img_bgr.shape[:2]
                    # 判断是摄像头还是视频文件
                    if hasattr(self, 'video_path') and self.video_path:
                        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
                        save_path = os.path.join(save_dir, f'{base_name}.mp4')
                        fps = int(self.video.get(cv2.CAP_PROP_FPS)) or 25
                    else:
                        import datetime
                        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                        save_path = os.path.join(save_dir, f'camera_{now}.mp4')
                        fps = int(1000 // self.timer.interval())
                    self.video_writer = cv2.VideoWriter(save_path, fourcc, fps, (w, h))
                self.video_writer.write(img_bgr)
            height, width = img_bgr.shape[:2]
            width_ratio = 861 / width
            height_ratio = 621 / height
            scale_ratio = min(width_ratio, height_ratio)
            new_width = int(width * scale_ratio)
            new_height = int(height * scale_ratio)
            img_bgr = cv2.resize(img_bgr, (new_width, new_height))
            img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
            self.label_result.setPixmap(QPixmap.fromImage(convert2QImage(img_rgb)))

    def preprocess_for_ocr(self, img):
        """
        对图像进行数据增强，提高OCR识别准确率
        """
        # 1. 灰度化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. 对比度增强 (CLAHE)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        # 3. 高斯模糊去噪
        blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

        # # 4. 自适应二值化
        # binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                                cv2.THRESH_BINARY, 11, 2)

        # 5. 边缘增强
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(blurred, -1, kernel)

        # 6. 转换回BGR格式（PaddleOCR需要彩色图像）
        result = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2BGR)

        # 7.保存处理后的图像
        cv2.imwrite('preprocessed_plate.jpg', result)

        return result

    def select_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                    "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
                                                    options=options)
        if image_path:
            if hasattr(self, 'progressBar'):
                self.progressBar.setValue(100)
            start_time = time.time()
            results = self.model(image_path, conf=self.conf, iou=self.iou, imgsz=480)
            end_time = time.time()
            img_bgr = results[0].plot()
            num = len(results[0].boxes)
            cls = results[0].boxes.cls.cpu().numpy()

            # ========== OCR 步骤 ==========
            plate = '无'
            img_src = cv2.imread(image_path)  # 用原图做裁剪

            # 把OpenCV图像转成PIL图像
            img_pil = Image.fromarray(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(img_pil)
            # 需要指定一个支持中文的字体，比如simhei.ttf
            font = ImageFont.truetype("simhei.ttf", 54)

            for box in results[0].boxes.xyxy.cpu().numpy():  # xyxy格式
                x1, y1, x2, y2 = map(int, box)
                crop = img_src[max(0,y1):min(img_src.shape[0],y2), max(0,x1-10):min(img_src.shape[1],x2+10)]

                if crop.size == 0:
                    continue

                # crop = self.preprocess_for_ocr(crop)

                ocr_result = self.ocr.ocr(crop, cls=True)
                if ocr_result and len(ocr_result[0]) > 0:
                    text = re.sub(r'[^0-9]', '', ''.join([ocr_result[0][i][1][0] for i in range(len(ocr_result[0]))]))  # PaddleOCR输出格式 (text, conf)
                    # === 根据检测框高度动态调整字体大小 ===
                    box_height = y2 - y1
                    # 设置字体大小为检测框高度的0.6倍（可以根据需要调整比例）
                    font_size = int(box_height * 0.6)
                    # 确保字体大小不小于12，避免太小看不清
                    font_size = max(font_size, 12)
                    # 加载字体
                    font = ImageFont.truetype("simhei.ttf", font_size)

                    # === 在框下方画车牌号 ===
                    y_text = y2 + int(box_height * 0.2) if y2 + int(box_height * 0.2) < img_bgr.shape[
                        0] else y2 - font_size
                    draw.text((x1, y_text), text, font=font, fill=(255, 0, 0))

            # PIL 转回 OpenCV
            img_rgb = np.array(img_pil)

            # 自动保存图片
            if hasattr(self, 'checkBox_isSave') and self.checkBox_isSave.isChecked():
                save_dir = r'./save_result'
                os.makedirs(save_dir, exist_ok=True)
                cv2.imwrite(os.path.join(save_dir, os.path.basename(image_path)), cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))



            height, width = img_bgr.shape[:2]
            width_ratio = 861 / width
            height_ratio = 621 / height
            scale_ratio = min(width_ratio, height_ratio)
            new_width = int(width * scale_ratio)
            new_height = int(height * scale_ratio)
            img_rgb = cv2.resize(img_rgb, (new_width, new_height))
            # img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

            if hasattr(self, 'label_nums'):
                self.label_nums.setText(str(num))
            if hasattr(self, 'label_times'):
                self.label_times.setText(f"{(end_time - start_time) * 1000:.1f} ms")

            self.label_result.setPixmap(QPixmap.fromImage(convert2QImage(img_rgb)))

    def select_weights(self):
        options = QFileDialog.Options()
        weights_path, _ = QFileDialog.getOpenFileName(self, '选择pt权重', '', 'pt (*.pt)', options=options)
        if weights_path:
            # self.end_thread()
            self.line_weights.setText(weights_path)
            self.weights_path = weights_path
            self.model = YOLO(self.weights_path)
            self.model(np.zeros((800, 800, 3)).astype(np.uint8))  #预先加载推理模型

    def open_camera(self):
        self.video = cv2.VideoCapture(0)
        self.video_path = None  # 摄像头时清空video_path
        bool_open = self.video.isOpened()
        if not bool_open:
            QMessageBox.warning(self, u"Warning", u"打开摄像头失败", buttons=QMessageBox.Ok,
                                          defaultButton=QMessageBox.Ok)

    def select_video(self):
        options = QFileDialog.Options()
        video_path, _ = QFileDialog.getOpenFileName(self, '选择视频', '',
                                                    'Videos (*.mp4 *.avi *.mkv);;All Files (*)', options=options)
        if video_path:
            self.video = cv2.VideoCapture(video_path)
            self.video_path = video_path  # 记录当前视频路径
        else:
            self.video_path = None

    def run_stop(self):
        if not self.video:
            QMessageBox.warning(self, u"Warning", u"请选择视频或者摄像头", buttons=QMessageBox.Ok,
                                          defaultButton=QMessageBox.Ok)
            return
        else:
            self.is_running = not self.is_running  # 切换状态
            icon = QtGui.QIcon()
            if self.is_running:
                self.timer.start()
                icon.addPixmap(QtGui.QPixmap("icon/暂停.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                self.timer.stop()
                icon.addPixmap(QtGui.QPixmap("icon/播放.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                # 关闭视频保存
                if hasattr(self, 'video_writer') and self.video_writer is not None:
                    self.video_writer.release()
                    self.video_writer = None
            self.pushButton_bofang.setIcon(icon)
            self.pushButton_bofang.setIconSize(QtCore.QSize(32, 32))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())

