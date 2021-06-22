# Face Recognition
在現今疫情的狀況，人與人的互動稀少，因此能彼此面對面的感受人的情緒的機會越來越少，因此這次的專案主要是想要辨識人的影像在網路鏡頭下，關於情緒的辨識。

## Introduction
本次專案是結合 [Windows Azure 人臉辨識API](https://azure.microsoft.com/zh-tw/services/cognitive-services/face/) 以及 [Python Flask](https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00) 做到情緒辨識和影像的即時串流。
本系統主要有三大功能:
1. 辨識性別
2. 辨識年齡
3. 辨識情緒以及其他面部特徵

## Dependencies
|Name|
|----|
|Flask 2.0.1|
|Python 3.7.6|
|opencv 3.4.2|
|cognitive-face 1.5.0|

## Build Process

### Installation
- 建立虛擬環境:
  ``` bash
  $ conda create --name face-recognition python=3.8
  $ conda activate face-recognition
  $ pip install -r requirements.txt
  ```
- 透過 [Windows Azure](https://azure.microsoft.com/zh-tw/services/cognitive-services/face/) 建立帳號後申請Windows Azure Face Recognition **API金鑰**
  
- (增加金鑰放置解釋)
  
- 下載所需檔案:
  [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
  
### Hardware
- WebCam

## Usage
- 輸入執行指令:
  ``` bash
  $ python3 app.py
  ```
## Results & Demo

## References
[Video Streaming in Web Browsers with OpenCV & Flask](https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00)

[Windows Azure Face Recognition API](https://azure.microsoft.com/zh-tw/services/cognitive-services/face/)

[Windows Azure Face Recognition Document](https://docs.microsoft.com/zh-tw/azure/cognitive-services/face/quickstarts/client-libraries?pivots=programming-language-python&tabs=visual-studio)