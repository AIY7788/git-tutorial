
import random


options_que = {1:("A.116" ,"B.117" ,"C.118" ,"D.119"),
               2:("A.elephent" ,"B.crocodile" ,"C.whale" ,"D.Ostrich"),
               3:("A.nitrogen" ,"B.carbon" ,"C.oxygen" ,"D.hydrogen"),
               4:("A.206" ,"B.207" ,"C.208" ,"D.209"),
               5:("A.mars" ,"B.venus" ,"C.earth" ,"D.mercury")}





#for l in range(4):
#    for d in options_que:
#        print(options_que.get(d)[l],end="  ")  
#    print()   


       
[print(" ".join(str(j) for j in range(1,i))) for i in range(1,7)]

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return f"{(self._celsius * 9 / 5) + 32:.2f}"

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = f"{(value - 32) * 5 / 9:.2f}"
temp = Temperature(0)
print(temp.fahrenheit)  # ได้ 32.0
temp.fahrenheit = 412   # ตั้งค่าใน F ได้
print(temp._celsius)    # ได้ 100.0   