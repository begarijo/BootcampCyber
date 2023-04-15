# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:22:15 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 13:19:47 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido vab Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf'
}

def main():
    """docstring for main"""
    for key, value in kata.items():
        print(f"{key} was created by {value}")
    return

if (__name__=='__main__'):
    main()

