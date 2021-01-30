def collatz(num):
    if num % 2 == 0:
        #Even
        print(num // 2)
        return (num // 2)
    if num % 2 == 1:
        #Odd
        print((3*num) + 1)
        return ((3*num) + 1)


try:
    num = int(input("Give me a number: "))
    while num != 1:
        num = collatz(num)

except ValueError:
    print("Enter a int!")








