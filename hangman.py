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
b="mango"
count=0
def user():
    global count
    global  a
    global h
    c=input("Enter a char= ")
    for i in range(len(b)):
        if(c==b[i]):
            a[i]=c
            print(a)
        elif(b[i]!=c):
            print(h[count])
            count+=1
for i in range(len(b)):
    user()
