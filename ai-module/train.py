from ultralytics import YOLO

model = YOLO("/home/ignitor/Personal/spill-detect/ai-module/models/train.yaml") # pass any model type
model.train()