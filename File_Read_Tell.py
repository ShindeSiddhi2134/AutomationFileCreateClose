def main():
    try:
        fobj=open("Demo.txt","r")
        print("file gets opend")
        print("file offset is:",fobj.tell())
        a=fobj.read(50)
        print(a)
        print("file is offset:",fobj.tell())

        fobj.close()
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__=="__main__":
    main()