def main():
    try:
        fobj=open("Demo.txt","a")
        print("file gets opend")
        fobj.write("siddhi pandurang shinde")
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not found in current directory")

if __name__=="__main__":
    main()