def dowrong():
    return 1/0

def main():
    try:
        dowrong()
    except:
        print("oops")
    finally:
        print("program finished")

if __name__ == "__main__":
    main()