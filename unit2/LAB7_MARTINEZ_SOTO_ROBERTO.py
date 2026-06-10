# functions
def choice1():
    print("1.-You like to code\n2.-You like to draw\n3.-You like money")
    choise1 = input("")
    if choise1 == "1":
        student["programming"] = student["programming"] + 5
    elif choise1 == "2":
        student["Digital design"] = student["Digital design"] + 5
    elif choise1 == "3":
        student["Business"] = student["Business"] + 5


def choice2():
    print("1.-You like puzzles\n2.-You like movies\n3.-You like socializing")
    choise2 = input("")
    if choise2 == "1":
        student["programming"] = student["programming"] + 5
    elif choise2 == "2":
        student["Digital design"] = student["Digital design"] + 5
    elif choise2 == "3":
        student["Business"] = student["Business"] + 5


def choice3():
    print(
        "1.-You like technical stuff\n2.-You like creating things\n3.-You like politicis"
    )
    choise3 = input("")
    if choise3 == "1":
        student["programming"] = student["programming"] + 5
    elif choise3 == "2":
        student["Digital design"] = student["Digital design"] + 5
    elif choise3 == "3":
        student["Business"] = student["Business"] + 5


def validator():
    for key in student:
        value = student[key]
        print(f"{key}:{value}")
    prog = student["programming"]
    design = student["Digital design"]
    business = student["Business"]
    if prog == design and prog > business:
        print("There is a tie between programing and design")
    elif prog == business and prog > design:
        print("There is a tie between programing and business")
    elif business == design and business > prog:
        print("There is a tie between business and desing")
    elif prog == business == design:
        print("Its a triple tie ")
    else:
        max_score = max(prog, design, business)
        if max_score == prog:
            print("Your career is TI ")
        elif max_score == design:
            print("Your career is arts ")
        elif max_score == business:
            print("Your career is business ")


# Main program
print("Recomendation career ")
name = input("Put your name: ")
student = {"name": "", "programming": 0, "Digital design": 0, "Business": 0}
choice1()
choice2()
choice3()
validator()
