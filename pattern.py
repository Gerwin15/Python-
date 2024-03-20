cars = ["Toyota", "Tesla", "Mercedes", "Honda", "Audi"]
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print(cars[4])

def hello():
    print("Hello")

def printPattern(rmax, cMax):
    for r in range(rmax):
        for c in range(cMax):
            if r == 0 or c == 6 or r == 6 or c == 0 or c == r:
                print("\t●", end=" ")
            else:
                print("\t✖", end=" ")
        print()
n1 = 7
n2 = 7
printPattern(n1,n2)



