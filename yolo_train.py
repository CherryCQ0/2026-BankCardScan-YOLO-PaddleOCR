# -*- coding: UTF-8 -*-
import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':

    # 加载预训练模型
    model = YOLO('yolo26s.yaml')  # 可以是 yolov8n/s/m/l/x.pt

    # 训练模型
    model.train(data=r"datasets/bank_num/bank_num.yaml",
                # 如果大家任务是其它的'ultralytics/cfg/default.yaml'找到这里修改task可以改成detect, segment, classify, pose
                imgsz=800,              # 图像大小
                epochs=200,             # 训练轮数
                single_cls=False,       # 是否是单类别检测
                batch=8,                # 批大小
                close_mosaic=10,         # 倒数多少轮关闭mosaic
                workers=2,              # 线程数
                device='0',             # 选择GPU还是CPU
                optimizer='SGD',        # using SGD 优化器 默认为auto建议大家使用固定的.
                # resume=,              # 续训的话这里填写True, yaml文件的地方改为lats.pt的地址,需要注意的是如果你设置训练200轮次模型训练了200轮次是没有办法进行续训的.
                amp=True,               # 如果出现训练损失为Nan可以关闭amp
                project=r'D:/PycharmProjects/2026-BankCardScan/runs/train',   # 保存的项目
                name='exp2',             # 保存的名称
                )
