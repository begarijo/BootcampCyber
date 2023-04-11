# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 16:46:12 by begarijo          #+#    #+#              #
#    Updated: 2023/04/11 16:58:56 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def odd_even(num):
    if (num == 0):
        return "I'm Zero."
    elif (num % 2 == 0):
        return "I'm Even."
    elif (num % 2 != 0):
        return "I'm Odd."

if (len(sys.argv) == 2 and sys.argv[1].isdigit()):
    num = int(sys.argv[1])
    result = odd_even(num)
    print(result)

else:
    if (len(sys.argv) == 1):
        print(" ")
    elif (not sys.argv[1].isdigit()):
        print("Error! Not an integer")
    else:
        print("Error! More than one arg")
