#Students will create a function that automatically generates an institutional email address from a person's first name and lastname
respuesta="yes"
i=0
def generate_email(name, lastname):
    email = (f"{name.lower()}.{lastname.lower()}@utd.edu.mx ")
    return email
#MAIN
while respuesta=="yes":
    i=i+1
    name=input("Put your name ")
    lastname=input("Put your lastname ")
    email = generate_email(name,lastname)
    print(email)
    respuesta=input(f"Do you want to make another mail (yes,no), you already have {i} emails generated ")


#Program for password validation
import re
def validation(password):
    validate=re.match(".{6,}",password)
    while not validate:
        print("Your password is incorrect, put it again")
        password=input("Put your password ").strip()
        validate=re.match(".{6,}",password)

#MAIN PROGRAM
password=input("Put your password ").strip()
validation(password)
print("Your password is correct ")