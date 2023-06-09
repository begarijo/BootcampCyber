# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 15:59:51 by begarijo          #+#    #+#              #
#    Updated: 2023/04/12 09:52:19 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def rev_alpha(string):
    return string.swapcase()[::-1]

if (len(sys.argv) > 1):
    s = ' '.join(sys.argv[1:])
    res = rev_alpha(s)
    print(res)
else:
    print("Error! Usage python3 exec.py <str>")
