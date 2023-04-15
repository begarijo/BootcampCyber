# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:26:55 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 12:05:53 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (2019, 9, 25, 3, 30)

def main():
    """docstring for main"""
    y = str(kata[0])
    m = str(kata[1])
    d = str(kata[2])
    h = str(kata[3])
    mi = str(kata[4])
    print("{y:>04}/{m:>02}/{d:>02} {h:>02}:{mi:>02}".format(y=y, m=m, d=d, h=h, mi=mi))
    return

if (__name__=='__main__'):
    main()
