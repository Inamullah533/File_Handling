from pathlib import Path
import os
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for  i, items in enumerate (items):
        print(f'{i+1} : {items}')

def createfile():
    try:
        readfileandfolder()
        name = input(f"PLease give a name of file for creating :- ")
        p = Path(name)
        if p.exists:
            with open(p,"w") as fs:
                data = input("What u want to write in file :")
                fs.write(data)
            print("File created Successfully")
        else:
            print("File already exists")

    except Exception as err:
        print(f"An error occur as {err}")


def readfile():
    try:
        readfileandfolder()
        name=input("Which file u want to read :- ")
        p= Path(name)
        if p.exists and p.is_file:
            with open(p,'r') as fs:
                data= fs.read()
                print(data)
        else:
            print("File not occur")        

    except Exception as err:
        print(f"An error occur as {err}")            


def updatefile():
    try:
        readfileandfolder()
        name=input("Which file you want to update :- ")
        p=Path(name)
        if p.exists and p.is_file:
            print("Press 1 for changed file name. ")
            print("Press 2 for overwrite a data.")
            print("Press 3 for Append a data.")
            choice=int(input("Select any one option :- "))
            if choice==1:
                name2=input("Enter a new name for file :- ")
                p2=Path(name2)
                p.rename(name2)

            if choice==2:
                with open(p,'w') as fs:

                    data=input("What u want to write in file, this is overwrite :- ")
                    fs.write(data)

            if choice==3:
                with open(p, 'a') as fs:
                    data=input("What u want to write , this is append data :- ")
                    fs.write(data)        

    except Exception as err:
        print(f"An error occur as {err}")

        
def deletefile():
    try:
        readfileandfolder()
        name=input("Which file u want to delete :- ")
        p=Path(name)

        if p.exists and p.is_file:
            os.remove(p)

    except Exception as err:
        print(f"An error occur as {err}")        










print("Press 1 for creating a file ")
print("Press 2 for reading a file ")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

chose = int(input(f"Please choose any one option :- "))

if chose==1:
    createfile()


if chose==2:
    readfile()  


if chose==3:
    updatefile()  


if chose==4:
    deletefile()        