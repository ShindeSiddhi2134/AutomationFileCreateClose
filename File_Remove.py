import os
def main():
    try:
        os.remove("Demo.txt")
        print("file is remove from directory")
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__=="__main__":
    main()