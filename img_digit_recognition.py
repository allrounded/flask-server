
# 아직 작업중 # 실행안됨
import torch


class DigitRecognition:
    def __init__(self):
        self.device =  "cuda" if torch.cuda.is_available() else "cpu"
        self.model_path = 'static/model/fine_tuned_model_3.pt'
        
    def img_digit_recognition(self):
        model = torch.load(self.model_path, map_location=self.device)