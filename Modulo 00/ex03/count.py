# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:04:40 by begarijo          #+#    #+#              #
#    Updated: 2023/04/11 18:00:44 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys, string

def text_analyzer(text):
    up, lo, pu, sp, ch = 0, 0, 0, 0, 0
    if (text.isdigit()):
        raise TypeError
    for letter in text:
        if (letter.isupper()):
            up += 1
        elif (letter.islower()):
            lo += 1
        elif (letter.isspace()):
            sp += 1
        elif(letter in string.punctuation):
            pu += 1
        ch += 1
    print("The text contains {ch} character(s):\n-{up} upper letter(s)\n-{lo} lower letter(s)\n-{sp} space(s)\n-{pu} punctuation mark(s)\n".format(ch=ch, up=up, lo=lo, sp=sp, pu=pu))

def main():
    try:
        if (len(sys.argv) > 2):
            print("Error! Too many args")
        elif (len(sys.argv) < 2):
            text =  input("What's the text?\n")
            text_analyzer(text)
        elif (len(sys.argv) == 2):
            text_analyzer(sys.argv[1])
    except:
         print("Arg is not a string")

if (__name__=='__main__'):
    main()
