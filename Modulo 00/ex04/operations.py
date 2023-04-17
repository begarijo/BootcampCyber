# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 15:48:20 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 12:02:04 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def do_op(a, b):
    if (a != 0 and b != 0):
        print("Sum:", a + b)
        print("Difference:", a - b)
        print("Product:", a * b)
        print("Quotient:", a / b)
        print("Remainder:", a % b)
    elif (a == 0 or b == 0):
        print("Sum:", a + b)
        print("Difference", a - b)
        print("Product:", a * b)
        print("Quotient: Error(division by zero)")
        print("Remainder: Error(module by zero)")

def main():
    """docstring for main"""
    try:
        if (len(sys.argv) == 3):
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            do_op(a, b)
    except:
        print("Not integers!!")
    if (len(sys.argv) > 3):
        print("Too many args")
    elif (len(sys.argv) < 3):
        print("Too few args")

if (__name__=='__main__'):
    main()
