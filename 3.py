def FindID(Monster):
    Check = 0
    LastID = 0
    with open('MONSTER.txt') as f:
        for line in f:
            parts = line.split(",")
            LastID = parts[0]
            if parts[1] == Monster:
                ID = parts[0]
                Check = 1
                return ID
        if Check == 0:
            return str(int(LastID) + 1)

def findlastline():
    count = -1
    with open('MONSTER.txt') as f:
        for line in f:
            count += 1

    return count


def makeMonsterCard():
    a = input("Please enter Monster Name")
    b = input("Please enter Monster Origin")
    c = input("Please enter Monster Description")
    d = int(input("Please enter Attack: 0 to 30"))
    e = int(input("Please enter Magical Force: 0 to 30"))
    f = int(input("Please enter Magical Defense: 0 to 30"))
    g = int(input("Please enter Defense: 0 to 30"))
    h = int(input("Please enter Intelligence: 0 to 30"))
    i = int(input("Please enter Health: 0 to 30"))
    j = int(input("Please enter Experience: 0 to 30"))
    List = [a,b,c,d,e,f,g,h,i,j]
    return List


def printCard(List):
    ID = FindID(List[1])
    if type(List[0]) != type(8):
        List.insert(0,ID)
    print(' ')
    print("MONSTER CARD # " + str(List[0]))
    print("Monster Name: " + List[1])
    print("Origin: " + List[2])
    print("Description: " + List[3])
    print("STATISTICS")
    print("Attack: " + str(List[4]))
    print("Magical Force: " + str(List[5]))
    print("Magical Defense: " + str(List[6]))
    print("Defense: " + str(List[7]))
    print("Intelligence: " + str(List[8]))
    print("Health: " + str(List[9]))
    print("Experience: " + str(List[10]))

def MakeList(count):
    List = []
    with open('MONSTER.txt') as f:
        check = 0
        for line in f:
            parts = line.split(",")
            if check == count:
                List = [parts[0],parts[1],parts[2],parts[3],int(parts[4]),int(parts[5]),int(parts[6]),int(parts[7]),int(parts[8]),int(parts[9]),parts[10]]
                break
            check += 1
    w = List[10]
    a = w[0]
    a = int(a)
    List.pop()
    List.append(a)
    return List

def chooserandommonster(monstercard):
    import random
    w = random.randint(1,895)
    a = MakeList(w)
    ascore = 0
    bscore = 0
    for i in range(4,11,1):
        first = a[i]
        second = monstercard[i]
        if first > second:
            ascore += 1
        elif second > first:
            bscore += 1
        elif first == second:
            ascore += 0.5
            bscore += 0.5
    if ascore > bscore:
        print("The computer's monster has " + str(ascore) + " points, while you have " + str(bscore) + " points, so the computer wins")
    elif ascore < bscore:
        print("The computer's monster has " + str(ascore) + " points, while you have " + str(bscore) + " points, so you win")
    else:
        print("Nobody wins")


# GAME
print("Please enter your monster details now")
w = makeMonsterCard()
b = findlastline()
b += 1
w.insert(0,b)


while True:
    a = input("Please enter 1 to compare to our monster, 2 to print your monster, 3 to add it to our List, 4 to end")
    if a == '1':
        chooserandommonster(w)
    elif a == '2':
        printCard(w)
    elif a == '4':
        print("Program Ending","...")
        break
    elif a == '3':
        string = ''
        for i in range(0,11,1):
            print(w)
            string += str(w[i])
            string += ','
        string += '\n'
        with open("MONSTER.txt","a") as f:
            f.write(string)
