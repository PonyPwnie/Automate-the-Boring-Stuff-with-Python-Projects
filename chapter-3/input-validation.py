#!/usr/bin/env python3

def collatz(number):
     if number % 2 == 0:
         result = number // 2
         print(result)
         return result
     else:
         result = 3 * number + 1
         print(result)
         return result


prompt = "Please input a number: "


while True:
    try:
        number = int(input(prompt))
        collatz(number)
    except ValueError:
        print("Make sure the input is a number.")


