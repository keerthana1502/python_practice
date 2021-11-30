class Bottle:
  def __init__(self,litter,rate):
    self.litter= litter
    self.rate = rate
steel= Bottle("1l", 40)
plastic=Bottle("2l",20)
print(steel.litter,"\n",steel.rate)
print(plastic.litter)
print(plastic.rate)