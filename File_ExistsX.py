import os
def main():
    if(os.path.exists("Demo.txt")):
        print("file is present in curent directory")
    else:
        print("file is not present")

if __name__=="__main__":
    main()