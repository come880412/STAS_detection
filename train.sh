python train.py --weights pretrained/yolov5s6.pt --cfg models/yolov5s.yaml --hyp data/hyps/lung_low.yaml --device 0,1 --name yolov5s

python train.py --weights pretrained/yolov5n6.pt --cfg models/yolov5n.yaml --hyp data/hyps/lung_low.yaml --device 0,1 --name yolov5n

python train.py --weights pretrained/yolov5m6.pt --cfg models/yolov5m.yaml --hyp data/hyps/lung_med.yaml --device 0,1 --name yolov5m

python train.py --weights pretrained/yolov5l6.pt --cfg models/yolov5l.yaml --hyp data/hyps/lung_high.yaml --device 0,1 --name yolov5l

python train.py --weights pretrained/yolov5x6.pt --cfg models/yolov5x.yaml --hyp data/hyps/lung_high.yaml --device 0,1 --name yolov5x
