from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for  i, items in enumerate (items):
        print(f'{i+1} : {items}')

def createfile():
    readfileandfolder()
    name = input(f"PLease give a name of file for creating :- ")
    p = Path(name)
    with open(p,"w") as fs:
        data = input("What u want to write in file :")
        fs.write(data)










print("Press 1 for creating a file ")
print("Press 2 for reading a file ")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

chose = int(input(f"Please choose any one option :- "))

if chose==1:
    createfile()