def main():
    try:
        fobj=open("Demo.txt","w")
        print("file gets opened")
        fobj.close()
    except FileNotFoundError as fobj:
        print("file is not present in current dictionary")

if __name__=="__main__":
    main()