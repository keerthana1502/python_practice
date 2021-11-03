h = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
a=['_','_','_','_','_']
word= "mango"
count=0
def user():
    c=int(input("Enter a number = "))
    for i in range (len(word)):
        if(word[i]==c):
           a[i]=c
while(True):
    if(c in word):
        user()
    elif(c not in word):
        print(h[count])
        count++1
    elif(count<=7):
        print("Game over")
