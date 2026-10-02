import os
def main():
    ret=os.path.exists("Demo.txt")
    if(ret==True):
        print("file is present in current directory")
    else:
        print("file is not present")

if __name__=="__main__":
    main()