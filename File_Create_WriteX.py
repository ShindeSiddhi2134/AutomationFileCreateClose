def main():
    try:
        fobj=open("Demo.txt","w")
        print("file get opened")

        fobj.write("marvellous infosysytem")
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__=="__main__":
    main()