import os

#Author: Justin Mabutas

def main():

    while(True):
        path = input("Enter Folder Name: ")
        try:
            folder = os.listdir(path)
            os.chdir(path)
            break
        except:
            print("Folder could not be found")

    os.system("md " + path + "TextFiles")


    for fileName in folder:
        if(fileName[-5:] == ".java"):
            file = open(fileName, "r+")
            fileText = file.read()
            file = open(path + "TextFiles\\" + fileName[:-5] +".txt", "w")
            file.write(fileText)


if __name__ == "__main__":
    main()      
