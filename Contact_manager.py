def add_person():
    name=input("ENTER YOUR NAME: ")
    age=input("ENTER YOUR AGE: ")
    email=input("ENTER YOUR EMIAL: ")
    person={"name": name, "age": age, "email":email}
    return person

def delete_contact(people):
    
    for i,person in enumerate(people):
        print(i+1,"-", person["name"],person["age"],person["email"],":")
        while True:
            number=input('ENTER THE NUMBER TO DELETE THE CONTACT')
            try:
                number=int(number)
                if number <=0 or number > len(people):
                    print("ENTER THE VALID NUMBER TO DELTE THE CONTACT ")
                else:
                    break
                    
            except:
                print("invalid input")
        people.pop(number-1)

def show_person(people):
    if not people:
        print("NO CONTACTS  AVAILABLE TO DELTE!")
    else:
        for i,x in enumerate(people):
            print(f"{i+1} {person["name"]} {person["age"]} {person["email"]}")

people=[]
print("WELCOME TO CONTACE MANAGER")
print()
print("YOU CAN ADD, DELETE AND VIEW CONTACT")
print()
while True:
    command= input("'A' FOR ADD CONTACTS 'D' FOR DELETE CONTACTS 'S' VIEW CONTACTS AND Q for quit:\n").lower()
    if command =='a' or command=='add':
        person=add_person()
        people.append(person)
        print("person added!")

    elif command=='delete' or command== 'd':
        delete_contact(people)
        print("person deleted")

    elif command=='s':
        show_person(people)
    elif command =="q":
        print("thank you for using contact manager!")

        break
    else:
        print("ENTER THE CORRECT INPUT!")