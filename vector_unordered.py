import numpy as np

class VectorUnordered:
  def __init__(self, size):
    self.size = size
    self.last_position = -1
    self.values = np.empty(self.size, dtype=int)

  # O(n)
  def prints(self):
    if self.last_position == -1:
      print('The vector is empty!')
    else:
      for i in range(self.last_position + 1):
        print('index:', i, ' - ', self.values[i])

  # O (1)
  def inserts(self, value):
    if self.last_position == self.size -1:
      print("Maximum vector size reached!")
    else: 
      self.last_position += 1
      self.values[self.last_position] = value  

  # O(n)
  def search(self, value):
    for i in range(self.last_position + 1):
      if value == self.values[i]:
        return i
    return -1

  # O (n)
  def delete(self, value):
    position = self.search(value)
    if position == -1:
      return -1
    else:
      for i in range(position, self.last_position):
        self.values[i] = self.values[i + 1]

      self.last_position -= 1

vectorExample = VectorUnordered(5) # Size 5
vectorExample.inserts(2)
vectorExample.inserts(3)
vectorExample.inserts(5)
vectorExample.inserts(8)
vectorExample.inserts(7)

vectorExample.prints()