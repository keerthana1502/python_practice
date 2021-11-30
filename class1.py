class Bottle:
  def diaplay(self,litter,rate):
    self.litter= litter
    self.rate = rate
steel=Bottle()
a=input("litter : ")
b=int(input(("rate : ")))
steel.diaplay(a,b)
print(steel.litter)
print(steel.rate)