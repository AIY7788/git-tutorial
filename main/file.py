
file_data = [ "Alice"
             ,"Bob"
             ,"Charlie"
             ,"David"
             ,"Eve"
             ,"aiy"]

file_name = "C:\\Users\\Trivico\\OneDrive\\Desktop/test.txt"    

with open(file_name , "w") as file :
    for name in file_data :
        file.write(name + "\n")
    
    
                            
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
     