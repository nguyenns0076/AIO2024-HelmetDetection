# AIO2024 - Helmet Detection

**Project Helmet Detection** ở Module01-Week04 của **AIO2024**.
Đây là một project dùng để nhận diện nón bảo hiểm trong ảnh đầu vào sử dụng model YOLOv10.

## 1. Clone project

    git clone https://github.com/nguyenns0076/AIO2024-HelmetDetection.git

## 2. Clone model

    mkdir model
    cd model
    git clone https://github.com/THU-MIG/yolov10.git
    cd yolov10

## 3. (Optional) Create and activate a virtual environment:

`conda create -n yolov10 python=3.9`

`conda activate yolov10`


## 4. Install the required dependencies and step to run project:

`pip install -r requirements.txt`

`pip install -e .`

`pip install gdown`

`pip install unzip`

`curl -o yolov10n.pt https://github.com/THU-MIG/yolov10/releases/download/v1.1`

`cd ..\..\`

`mkdir datasets`

`cd datasets`

`gdown 1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R`

`tar -xf Safety_Helmet_Dataset.zip`

sử dụng lệnh `yolo checks` nếu CUDA None thì dùng lệnh

`conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`

## 5. Starting the Application

One everything is ready, you can launch the application by running:
`streamlit run app.py`
