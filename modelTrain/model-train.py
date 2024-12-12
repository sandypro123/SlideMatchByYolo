'''
Author: Sandy
Date: 2024-11-25 10:38:13
LastEditors: Please set LastEditors
LastEditTime: 2024-12-12 20:04:58
Description: yolo模型训练
'''

import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO()
    #model.load('yolov8n.pt') # 加载预训练权重,改进或者做对比实验时候不建议打开，因为用预训练模型整体精度没有很明显的提升
    model.train(data=r'D:\SlideMatchByYolo\modelTrain\data.yaml',
                imgsz=640,
                epochs=30,
                device='CPU',
                batch=1,
                workers=2,
                optimizer='SGD',
                close_mosaic=10,
                resume=False,
                #project='runs/train',
                #name='exp',
                single_cls=False,
                cache=True,
                )