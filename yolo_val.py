# -*- coding: UTF-8 -*-
import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 加载训练好的模型
model = YOLO('runs/train/hrsc2016_yolo8_250420a/weights/best.pt')  # 替换为你的最佳模型路径
if __name__ == '__main__':

    # 验证模型
    metrics = model.val(
        data='D:/PycharmProjects/2026-BankCardScan/datasets/bank_num/bank_num.yaml',  # 数据集配置文件路径
        batch=8,  # 批量大小
        imgsz=800,  # 输入图像大小
        # conf=0.25,  # 对象置信度阈值
        # iou=0.6,  # NMS IoU阈值
        split='test',  # 可以是 'val', 'test' 或 'speed'
        device='0',  # 使用GPU (可以是 '0', '0,1,2,3' 或 'cpu')
        half=False,  # 使用FP16半精度推理
        dnn=False,  # 使用OpenCV DNN进行ONNX推理
        plots=True,  # 保存验证结果图
        save_json=False,  # 保存结果为JSON文件
        save_hybrid=False,  # 保存混合版本标签
        save_conf=False,  # 保存结果带置信度
        save_txt=False,  # 保存结果为.txt文件
        save_dir='runs/val',  # 保存目录
        name='exp',  # 实验名称
        exist_ok=False,  # 是否覆盖现有项目
        augment=False,  # 增强推理
        verbose=True,  # 打印详细输出
    )
