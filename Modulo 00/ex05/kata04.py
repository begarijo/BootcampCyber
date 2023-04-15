# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:35:11 by begarijo          #+#    #+#              #
#    Updated: 2023/04/12 16:41:05 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    """docstring for main"""
    mod = kata[0]
    ex = kata[1]
    n1 = kata[2]
    n2 = kata[3]
    n3 = kata[4]
    print("module_{mod:>02d}, ex_{ex:>02d} : {n1:.2f}, {n2:.2e}, {n3:.2e}".format(mod=mod, ex=ex, n1=n1, n2=n2, n3=n3))
    return

if (__name__=='__main__'):
    main()

