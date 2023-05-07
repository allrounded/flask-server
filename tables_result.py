def get_default_row_list():
    index = []
    period = "AM"
    for i in range(15):
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
    return index


class TablesResult:
    def __init__(self):
      self.default_columns = ['MON','TUE','WED','THU','FRI','SAT','SUN']
      self.default_row = get_default_row_list()
      self.default_frame = pd.DataFrame(1, index=self.default_row, columns=self.default_columns)
    
    def get_final_result(self, table_images):
      for key in self.default_columns:
        for table in table_images:
          if key in table:
            times = table.index[table[key] == 0].tolist()
            for time in times:          
              self.default_frame.loc[time, key] = 0
      return self.default_frame

table_result = TablesResult()