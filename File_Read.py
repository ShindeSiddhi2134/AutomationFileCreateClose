def main():
    try:
        fobj=open("Demo.txt","r")
        print("file gets opend")

        a=fobj.read(7)
        print(a)

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__=="__main__":
    main()