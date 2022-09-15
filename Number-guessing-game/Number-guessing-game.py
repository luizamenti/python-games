def test(random_number, input_number):
    if random_number == input_number:
        print("You guessed it!")
        quit()
    else:
        print("Sorry, not this time. Here's a hint:")

def hint1(random_number, input_number):
    if random_number > input_number:
        print("Try a greater number.")
    else:
        print("Try a smaller number.")

def hint2(random_number):
    if random_number % 2 == 0:
        print("It's an even number.")
    else:
        print("It's an odd number.")

def hint3(random_number):
    divisors = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 2, 1]
    for i in divisors:
        if random_number % i == 0:
            print("It's divisible by "+ str(i) + ".")
            break

def hint4(random_number):
    input_number = int(input("Input a number: "))
    if random_number == input_number:
        print("You guessed it!")
        quit()
    if random_number > input_number:
        print("Ehh, not yet. I'll make it easier for you. From now on, let's go only by \"greater\" and \"smaller\". Try a greater number.")
        hint4(random_number)
    else:
        print("Ehh, not yet. I'll make it easier for you. From now on, let's go only by \"greater\" and \"smaller\". Try a smaller number.")
        hint4(random_number)

import random
random_number = random.randint(1,50)
input_number = int(input("Input a number: "))

test(random_number, input_number)

hint1(random_number, input_number)

input_number = int(input("Input a number: "))

test(random_number, input_number)

hint2(random_number)

input_number = int(input("Input a number: "))

test(random_number, input_number)

hint3(random_number)

hint4(random_number)

