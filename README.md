# STAS_detection
Competition URL: https://tbrain.trendmicro.com.tw/Competitions/Details/21 (public 8th, private 19th)

# Getting started
- Clone this repo to your local
``` bash
git clone https://github.com/come880412/STAS_detection
cd STAS_detection
```

## Computer Equipment
- System: Windows10、Ubuntu20.04
- Pytorch version: Pytorch 1.7 or higher
- Python version: Python 3.7
- Testing:  
CPU: AMR Ryzen 7 4800H with Radeon Graphics
RAM: 32GB  
GPU: NVIDIA GeForce RTX 1660Ti 6GB  

- Training:  
CPU: Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz  
RAM: 256GB  
GPU: NVIDIA GeForce RTX 3090 24GB * 1

(TWCC server)
CPU: Intel(R) Xeon(R) Gold 6154 CPU @ 3.00GHz
RAM: 180 GB
GPU: Tesla V100 32 GB * 4

## Download & preprocess dataset
- You should prepare the dataset from [here](https://tbrain.trendmicro.com.tw/Competitions/Details/21), and put the dataset on the folder `../dataset`. After doing so, please use the following command to do data preprocessing.
``` bash
python3 preprocessing.py 
```
- Note: please modify the dataset path on the script `preprocessing.py`.

## Download pretrained models
- Please download the pretrained models from [here](https://drive.google.com/drive/folders/1XJhSn6OJ7Au_VqZfCohSRvOfHpR9okaK?usp=sharing), and put the models on the folder `./weights`.

## Inference
- After downloading the pretrained models and preparing the datasets, you could use the following command to test the best results on the public/private leaderboard.
``` bash
python3 public.py --conf-thres 0.05 --iou-thres 0.46 --img-size 1536 --weights ./weights/yolov5x/best.pt ./weights/yolov5l/best.pt ./weights/yolov5m/best.pt ./weights/yolov5s/best.pt  ./weights/yolov5n/best.pt  --TTA
```
- The result ".json" file will automatically save in the current path.

## Training
- You should download the COCO pretrained models on the offical[1]. And put all the models on the folder `./pretrained`. After that, please use the following script to train all the models used in this competition.
``` bash
bash train.sh
```

## Training result
Here, we show that our training results.
| labeled image | predicted image |
|:--------------------:|:--------------------:|
|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch0_labels.jpg" width=100% height=100%>|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch0_pred.jpg" width=100% height=100%>|
|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch1_labels.jpg" width=100% height=100%>|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch1_pred.jpg" width=100% height=100%>|
|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch2_labels.jpg" width=100% height=100%>|<img src="https://github.com/come880412/STAS_detection/blob/main/images/val_batch2_pred.jpg" width=100% height=100%>|

# Reference
[1] https://github.com/ultralytics/yolov5
