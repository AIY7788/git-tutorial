
import random


#  ●, ┌, └, ┐, │, └, ┘ ─f

dice_art = {
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘" ),
    2:("┌───────────┐",
       "│  ●        │",
       "│           │",
       "│        ●  │",
       "└───────────┘" ),
    3:("┌───────────┐",
       "│  ●        │",
       "│     ●     │",
       "│        ●  │",
       "└───────────┘" ),
    4:("┌───────────┐",
       "│  ●     ●  │",
       "│           │",
       "│  ●     ●  │",
       "└───────────┘" ),
    5:("┌───────────┐",
       "│  ●     ●  │",
       "│     ●     │",
       "│  ●     ●  │",
       "└───────────┘" ),
    6:("┌───────────┐",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "└───────────┘" )
}

dice = []
total = 0
num_of_dice = int(input("how many dices : "))
 
for d in range(num_of_dice):
   dice.append(random.randint(1, 6))


for l in range(5):
   for d in dice:
      print(dice_art.get(d)[l],end='')
   print() 


for d in dice :
    total += d

print(total)