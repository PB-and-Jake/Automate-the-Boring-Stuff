#making the Collatz Sequence - "The Simplest Impossible Math Problem

#collatz(number)
#if number is event, collatz() prints number //2 and return value
#if number is odd, collatz() prints and returns 3 * number+1

def collatz(number):
    if(number % 2==0):
        number = number//2
        print(number)
        return number
    elif(number % 2 == 1):
        number = 3*number+1
        print(number)
        return number

print('Enter a number:')
try:
    inputNum = int(input())
    while inputNum != 1:
       inputNum = collatz(inputNum)
except ValueError:
        print('Please enter an integer. The Collatz Sequence only works on integer values.')
    

    
