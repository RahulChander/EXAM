WORDLIST_FILENAME = "MONSTER.txt"
def task2():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    check = 0
    a = input("Please enter monster name")
    for line in inFile:
        word = line.split(',')
        if word[1] == a:
            print("Monster Found")
            check = 1
            break
    if check == 0:
        print("Monster not found")

task2()
