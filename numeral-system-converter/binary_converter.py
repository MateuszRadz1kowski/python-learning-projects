class BinaryConverter:
  def __init__(self,number):
    self.number = number

  def convert_to_decimal(self):
    decimal_value = 0
    for i in range(len(self.number)):
      if self.number[-i-1]=="1": decimal_value+= 2**i
    print(decimal_value)

  def convert_to_binary(self):
    max_power = 0
    while 2 ** (max_power + 1) <= int(self.number):
      max_power += 1

    binary_value = ""
    for i in range(max_power, -1, -1):
      print(i)
      if int(self.number) - 2 ** i >= 0:
        binary_value += "1"
        self.number = int(self.number) - 2 ** i
      else:
        binary_value += "0"

    print(binary_value)

#BinaryConverter("1010110").convert_to_decimal()
BinaryConverter("11").convert_to_binary()