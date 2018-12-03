def MakeList():
    monster_list = []
    with open('MONSTER.txt') as f:
        for line in f:
            parts = line.split(",")
            monster_list.append(parts[1])
        return monster_list


def FindMonster(monsterlist,name):
    check = 0
    for i in monsterlist:
        if i == name:
            check = 1
            print("Monster Found")
            break
    if check == 0:
        print("Monster Not Found")



print("Program beginning.... Loaded")

while True:
    menu = (input("Please enter 1 to display list, 2 to search for a monster, 3 to end"))
    if menu == '1':
        print(MakeList())
    elif menu == '2':
        a = input("Please enter name of Monster")
        FindMonster(MakeList(),a)
    elif menu == '3':
        break
    else:
        print("Invalid command")
