#age +name function
def cat_age_calc(age,name):
    if age<2:
        print(name,"is a kitten")
    if 2<age<12:
        print(name,"is an adult cat")
    if age>=12:
        print(name,"is an old cat")
cat_age_calc(10,"mina")

