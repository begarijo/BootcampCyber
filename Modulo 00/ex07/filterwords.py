# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 13:48:59 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 14:03:19 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def main():
    if (len(sys.argv) != 3):
        print("Try again! Too few args")
    else:
        try:
            n = int(sys.argv[2])
            e = string.punctuation
            s = sys.argv[1]
            s = s.translate(str.maketrans('', '', e))
            w = [word for word in s.split() if len(word) >= n]
            print(w)
        except:
            print("Try again! Wrong type of arg <str> + <int>")

if (__name__=='__main__'):
    main()
