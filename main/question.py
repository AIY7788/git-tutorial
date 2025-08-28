

questions = ["how many eiements are in periodic table",
             "which animal lays the largest eggs",
             "what is the most abundant gas in earth's atmosphere",
             "how many bones are in the human body",
             "which planet in solar system is the hottest"]




options = (("A.116" ,"B.117" ,"C.118" ,"D.119"),
           ("A.elephent" ,"B.crocodile" ,"C.whale" ,"D.Ostrich"),
           ("A.nitrogen" ,"B.carbon" ,"C.oxygen" ,"D.hydrogen"),
           ("A.206" ,"B.207" ,"C.208" ,"D.209"),
           ("A.mars" ,"B.venus" ,"C.earth" ,"D.mercury"))

answers = ("c","d","a","a","b")
guesses = []
score = 0
question_num = 0


for question in questions:
    
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("enter (A, B, C, D) : ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("corract")
    else:
        print("incorract")
        print(f"{answers[question_num]} is the corract answer")

    question_num += 1

print("####result####")

print("answers : ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses : ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()


score = (score / len(questions)) * 100
print(f"score : {score}%")