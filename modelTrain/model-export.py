'''
Descripttion: 
Author: Sandy
Date: 2024-12-12 20:33:15
LastEditTime: 2024-12-12 20:34:07
'''
from ultralytics import YOLO
model=YOLO(r'D:\SlideMatchByYolo\modelTrain\runs\detect\train\weights\best.pt')
model.export(format='onnx')