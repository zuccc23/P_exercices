#string manipulation
text="Hello World" #variable 1
alphabet="abcdefghijklmnopqrstuvwxyz" #variable 2 
shift= 3 #variable 3

for char in text.lower(): #variable 4 WITHIN variable 1 BUT lowercase
    index=alphabet.find(char) #variable 5 with value 'alphabet.find(char)'
    new_index = index+shift 
    new_char=alphabet[new_index]
    print(' char:' ,char, 'new char:', new_char)
