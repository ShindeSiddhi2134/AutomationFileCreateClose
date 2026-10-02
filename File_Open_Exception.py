def main():
    try:
        open("Demo.tst","r")
        print("file gets opened")
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__=="__main__":
    main()