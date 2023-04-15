# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 10:43:44 by begarijo          #+#    #+#              #
#    Updated: 2023/04/14 10:59:30 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, random

def check_num():
    secret = random.randint(1, 99)
    t = 0
    n = None
    while (n != secret):
        n = input("What's your guess?:D\n")
        if (n == "exit"):
            print("Okay! Bye:)")
            break
        elif (not n.isdigit() or int(n) < 1 or int(n) > 99):
            print("Not the right usage! Enter a number between 1 and 99")
            t += 1
            continue
        t += 1
        n = int(n)
        if (n < secret):
            print("Too low! Try again:)")
        elif (n > secret):
            print("Too high! Try again:)")
        else:
            if (secret == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42!")
            if (t == 1):
                print("Congratulations! You achieve it in your first try! MAKINON")
            else:
                print("Congratulations! It only took you {t} attemps!".format(t=t))

def main():
    """docstring for main"""
    if (len(sys.argv) == 1):
        print("Welcome to the Guessing Game!:D")
        print("You have to guess a number between 1 and 99")
        print("Type 'exit' to quit the game")
        print("Good luck;)")
        check_num()

if (__name__=='__main__'):
    main()

