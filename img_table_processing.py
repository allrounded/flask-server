import cv2
import numpy as np
import pandas as pd
import urllib.request
from img_final_result import get_time_segment


# 30분 단위로 데이터 추출
def table_half_hour(row_count, col_count, hori_cell, ver_cell, dst):
  result_list = []
  y = hori_cell//24
  for i in range(row_count*2): # 행의 개수 * 2번
    x = ver_cell//2
    row_list = []
    for j in range(col_count): # 열의 개수
      value = dst[y, x]
      if value == 0:
        value = 1
      if value == 255:
        value = 0
      row_list.append(value)
      x += ver_cell
    if col_count == 5:
      row_list.extend([0, 0])
    if col_count == 6:
      row_list.append(1)
    result_list.append(row_list)
    y += hori_cell//2
  for i in range(30-row_count*2):
    result_list.append([0]*7)
    
  return result_list



class OneTableProcessing:
  def __init__(self):
    self.columns = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    self.index = get_time_segment()
  
  def img_to_dataframe(self, img_path):
    req = urllib.request.urlopen(img_path)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    
    # 다크모드
    if image[0][0][0] < 100:
      image = 255 - image
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      blur = cv2.GaussianBlur(image, (1, 1), 0)
      thresh, dst = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)
      kernel = np.ones((3,3), np.uint8)
      dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel, iterations=3)
    else:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      blur = cv2.GaussianBlur(image, (1, 1), 0)  
      thresh_value, dst = cv2.threshold(blur, 251, 255, cv2.THRESH_BINARY)
      kernel = np.ones((3,3), np.uint8)
      dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel, iterations=3)
    print(dst)
    # cv2.imshow('image',dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # contour로 외곽선 검출 및 확인
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects = [cv2.boundingRect(cnt) for cnt in contours]
    # y -> x좌표를 기준으로 오름차순
    rects = sorted(rects, key=lambda x: x[1])
    rects = sorted(rects, key=lambda x: x[0])
 
    col_count = sum(1 for tpl in rects if tpl[1] == rects[0][1]) - 1 # 열의 개수
    row_count = sum(1 for tpl in rects if tpl[0] == rects[0][0]) - 1 # 행의 개수
    index_width = rects[0][2] + rects[0][0]  # 인덱스 가로
    index_height = rects[0][3] + rects[0][1] # 인덱스 세로

    # 인덱스 자른이미지
    cropped_image = dst[index_height:, index_width:].copy() # 세로 자르기(요일), 가로자르기(시간)

    hori_pix = cropped_image.shape[0] # 세로: 행 픽셀개수
    ver_pix = cropped_image.shape[1]  # 가로: 열 픽셀개수
    hori_cell = hori_pix // row_count # 한칸 세로 길이
    ver_cell = ver_pix //col_count # 한칸 가로 길이

    # table_half_hour() 적용
    result_list = table_half_hour(row_count, col_count, hori_cell, ver_cell, cropped_image)
    result_frame = pd.DataFrame(result_list, columns=self.columns, index=self.index)
    
    return result_frame

one_table_processing = OneTableProcessing()