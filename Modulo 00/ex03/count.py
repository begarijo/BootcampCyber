# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:04:40 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 12:21:59 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def text_analyzer(*arg):
    up, lo, pu, sp, ch  = 0, 0, 0, 0, 0
    if (len(arg) == 0 or not arg[0]):
        text = input("What's the text?\n")
        text_analyzer(text)
        return
    if (type(arg[0]) != str):
        print("TypeError: Arg is not str")
        return
    else:
        text = arg[0]
    for c in text:
        if (c.isupper()): up += 1
        elif (c.islower()): lo += 1
        elif (c.isspace()): sp += 1
        elif (c in string.punctuation): pu += 1
        ch += 1
    print("The text contains {ch} character(s):\n-{up} upper letter(s)\n-{lo} lower letter(s)\n-{sp} space(s)\n-{pu} punctuation mark(s)\n".format(ch=ch, up=up, lo=lo, sp=sp, pu=pu))

def main():
    try:
        if (len(sys.argv) > 2):
            print("Error! Usage: python3 count.py <text>")
        elif (len(sys.argv) == 2):
            text_analyzer(sys.argv[1])
        else:
            text_analyzer()
        return
    except:
        return

if (__name__=='__main__'):
    main()
