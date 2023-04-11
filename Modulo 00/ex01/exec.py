# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 15:59:51 by begarijo          #+#    #+#              #
#    Updated: 2023/04/11 16:16:32 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def main():
    print(' '.join(sys.argv[1:])[::-1].swapcase())

if (__name__=='__main__'):
    main()