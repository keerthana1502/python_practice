ch=input("enter a string = ")
vowel=0
consonent=0
special=0
digit=0
for i in range (len(ch)):
    if(ch[i] in 'aeiou'):
        vowel=vowel+1
    elif(ch[i]>='a' and ch[i]<='z'):
        consonent+=1
    elif(ch[i]>='0' and ch[i]<='9'):
        digit+=1
    else:
        special+=1
print("vowel count = ",vowel)
print("consonent count = ",consonent)
print("digit count = ",digit)
print("special count = ",special)
    
