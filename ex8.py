#how old is your cat?
def cat_age_calc():
    name,age=input("What is your cat's name and age?").split()
    new_age=int(age) 
    if new_age <2: 
        print( name, "is a kitten")
    if 2<new_age<12: 
        print(name,"is an adult cat")
    if new_age >=12 :
        print(name,"is an old cat")
cat_age_calc()
