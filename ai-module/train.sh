python /home/ignitor/Personal/spill-detect/ai-module/yolov7/train.py --workers 8 --device 0 --batch-size 8 --data /home/ignitor/Personal/spill-detect/ai-module/data/data.yaml --img 1280 720 --cfg /home/ignitor/Personal/spill-detect/ai-module/models/config.yaml --weights /home/ignitor/Personal/spill-detect/ai-module/models/yolov7.pt --name /home/ignitor/Personal/spill-detect/ai-module/models/yolov7-spill-detect --hyp /home/ignitor/Personal/spill-detect/ai-module/models/hyper_parameters.yaml --epochs 50