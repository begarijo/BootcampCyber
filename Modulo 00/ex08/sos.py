# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 17:01:07 by begarijo          #+#    #+#              #
#    Updated: 2023/04/14 10:12:22 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

encoder = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}

def make_morse(mes):
    """docstring for make_morse"""
    encoded = []
    for c in mes:
        encod_c = encoder.get(c.upper())
        if (encod_c):
            encoded.append(encod_c)
        else:
            return None
        return (" ".join(encoded))

def main():
    """docstring for main"""
    if (len(sys.argv) == 1):
        print("Error! Usage: python3 sos.py <arg>")
    else:
        encoded_m = []
        for mes in (" ".join(sys.argv[1:])):
            encoded = make_morse(mes)
            if encoded:
                encoded_m.append(encoded)
            else:
                print("Not encoded")
                sys.exit(1)
        print(" ".join(encoded_m))

if (__name__=='__main__'):
    main()

