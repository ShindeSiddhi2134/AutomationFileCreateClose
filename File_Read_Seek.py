#seek(kuthe,Kuthun)
#kuthun:0/1/2
#0 starting
#1current
#2 end

def main():
    try:
        fobj=open("Demo.txt","r")
        print("file gets opened")

        fobj.seek(6,0)
        data=fobj.read()
        print(data)

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__=="__main__":
    main()