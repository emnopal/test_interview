def front_back(n):
    for i in range(1, n+1):
        if i%3 != 0 and i%5 != 0:
            print(i, end=",")
        if i%3 == 0:
            print("Frontend", end=",")
        if i%5 == 0:
            print("Backend", end=",")

if __name__ == '__main__':
    front_back(50)