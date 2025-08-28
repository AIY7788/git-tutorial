
text = input("Input a word: ")

if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")