import sys

def factorPrime():
    numbers = sys.argv[1]
    numbers = open(numbers,"r")
    numbers = numbers.readlines()
    for number in numbers:
        number = int(number)
        for i in range(2,int((number**0.5))+1):
            if((int(number % i)) == 0):
                if((i % 2) != 0 or ((number/2) % 2) != 0):
                    print("{} = {} * {}".format(number,int(number/i),i))
                    break
                else:
                    continue
            else:
                continue

factorPrime()
