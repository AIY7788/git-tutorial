
import random
def s_pin ():
    sympols = ['⭐', '🍋', '💎' ,'🏆', '🪙']
    return [random.choice(sympols) for _ in range(3)]



def p_ayout(r , pin):
    if r[0] == r[1] == r[2]:
        if r[0] == '🍋' :
            return pin * 3
        elif r[0] == '⭐':
            return pin * 5
        elif r[0] == '🪙':
            return pin * 7
        elif r[0] == '🏆':
            return pin * 10
        elif r[0] == '💎':
            return pin * 20
    return 0    

def m_ian():
    balance = 200

    print("  wellcom to slot game  ")
    print("sympols:⭐ 🍋 💎 🏆 🪙")

    while True :
        
        print(f"current balance : ${balance}")

        pin = input("place your bet amount : ")

        if not pin.isdigit():
            print(f"{pin} is not a valid number")
            continue

        pin = int(pin)
        
        if pin <= 0 :
            print("bet must be greater then 0")
            continue


        if balance < pin :
            print("instufficient funds")
            continue

        
        balance -= pin

        r = s_pin()
        print("runing....")
        print("###############")
        print("  |  ".join(r))
        print("###############")
        print("\n")

        p = p_ayout(r , pin)
        balance += p

        if p > 0 :
            print("###############")
            print(f"you won ${p}")
            print(f"current balance : ${balance}")
            print("###############")
            if input("play again ? (y/n) : ") != 'y' : 
                return False
        else :
            print("sorry you lost this round")

        

        if balance <= 0 :
            print(f"your balance is {balance} see you later 👋")
            return False

        
if __name__ == "__main__" :
    m_ian()
    