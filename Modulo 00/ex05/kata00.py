# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:16:43 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 13:18:31 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (5, 6)

def main():
    """docstring for main"""
    flag = True
    if (isinstance(kata, int)):
        print("The number is: {number}".format(number=kata))
    elif (len(kata) > 1):
        for number in kata:
            if (type(number) != int):
                print()
                flag = False
        if flag:
             print("The {length} numbers are: {number}". format(length=len(kata), number=', '.join(str(n) for n in kata)))
    return

if (__name__=='__main__'):
    main()

