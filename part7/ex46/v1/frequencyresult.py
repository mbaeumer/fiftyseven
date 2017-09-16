#!/usr/bn/python

class FrequencyResult:
  def __init__(self, word_map, starttime, endtime):
    self.words = word_map
    self.starttime = starttime
    self.endtime = endtime
  
  def get_time_elapsed(self):
    return (self.endtime - self.starttime).microseconds        
