#The Collatz Sequence
def collatz(number):
    """This function floor division by 2 if the number is even, and multiplies the paramater by 3 and adds 1 if it is not."""
    if number % 2 == 0:
        spam = number // 2
    else:
        spam = 3 * number + 1
    return spam



collatzNumber = 0

print('Enter a number:')
while True:
    try:
        numberEntered = int(input())
        break
    except ValueError:
        print("Enter a valid number - please try again ...")

while collatzNumber != 1:
    #This will loop through the number entered until it reaches 1. It always reaches 1.
    collatzNumber = collatz(numberEntered)
    print(collatzNumber)
    numberEntered = collatzNumber


