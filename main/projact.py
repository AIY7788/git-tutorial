import time

my_time = int(input("enter the number of time : "))
my_time *= 3600

for t in range(my_time , 0 , -1):
    c = t % 60
    m = int(t / 60) % 60
    h = int(t / 3600)
    print(f"{h:02} : {m:02} : {c:02}")
    time.sleep(1)

print("time's up")