word: str = input("enter a word:")
my_word = []
for letter in word:
    if type(letter) == str:
        letter.upper()
        my_word.append(letter)
    else:
        continue
print(my_word)
# לא הצלחתי להבדיל מה מספר ומה אות (מה שבעצם השאלה בעצמה חח