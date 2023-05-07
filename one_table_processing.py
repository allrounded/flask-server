import cv2
import numpy as np
import pandas as pd

# 30분 단위로 바꾸기
def table_half_hour(row_count, col_count, hori_cell, ver_cell, dst):
  result_list = []
  y = hori_cell//4 
  for i in range(row_count*2):
    x = ver_cell//2
    row_list = []
    for j in range(col_count):
      value = dst[y, x]
      row_list.append(value)
      x += ver_cell
    y += hori_cell//2
    result_list.append(row_list)

  columns = ['MON','TUE','WED','THU','FRI']
  if col_count == 6:
    columns.append('SAT')
  elif col_count == 7:
    columns.extend(['SAT', 'SUN'])

  # 데이터 프레임의 인덱스 값 설정
  index = []
  period = "AM"
  for i in range(row_count):
    start_time = i+9
    if start_time >= 13:
      start_time -= 12
    elif start_time == 12:
      period = "PM"
    for j in range(2):
      if j == 0:
        index.append(f"{period} {start_time}:00 ~ {start_time}:30")
      else:
        index.append(f"{period} {start_time}:30 ~ {start_time%12+1}:00")
  
  result_frame = pd.DataFrame(result_list, index = index, columns=columns)
  return result_frame



class OneTableProcessing:
  def __init__(self):
    self.MODE = "LIGHT"
  
  def img_to_dataframe(self, img_path):
    image = cv2.imread(img_path)

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

    # contour로 외곽선 검출 및 확인
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 각 contour를 감싸는 최소 크기의 사각형 좌표를 구함
    # 사각형의 좌표 (x, y, w, h) 형태의 튜플: x와 y - 좌상단 좌표, w와 h - 각 사각형의 너비와 높이
    rects = [cv2.boundingRect(cnt) for cnt in contours]
    # y좌표를 기준으로 오름차순으로 정렬
    rects = sorted(rects, key=lambda x: x[1])
    # x좌표를 기준으로 오름차순으로 정렬
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
    result_frame = table_half_hour(row_count, col_count, hori_cell, ver_cell, cropped_image)
    return result_frame

one_table_processing = OneTableProcessing()