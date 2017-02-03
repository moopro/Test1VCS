import random
def genrate_list():
    alist = [x for x in range(random.randint(-10,10))]
    return alist

def printIt():
    print(genrate_list())

def main():
    printIt()
    
if __name__ == '__main__':
    print("Test printIt():")
    main()
