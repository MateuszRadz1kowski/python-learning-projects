class BinaryConverter:
  def __init__(self,number):
    self.number = number

  def convert_to_decimal(self):
    decimal_value = 0
    for i in range(len(self.number)):
      if self.number[-i-1]=="1": decimal_value+= 2**i
    print(decimal_value)

      
converter = BinaryConverter("1010110")
converter.convert_to_decimal()