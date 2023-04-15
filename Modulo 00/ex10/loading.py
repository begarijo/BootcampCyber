# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 16:03:14 by begarijo          #+#    #+#              #
#    Updated: 2023/04/15 11:07:44 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def ft_progress(lst):
    """docstring for ft_progress"""
    start_t = time.time()
    ref_t = 0
    for item in (lst):
        if (item == 1):
            ref_t = time.time() - start_t
        iter_t = time.time() - start_t
        ETA = (len(lst) - item) * ref_t
        perc = item / len(lst)
        prog = item + 1
        ppo = '=' * int(30 * prog / len(lst)) + '>' + ' ' * (30 - int(30 * prog / len(lst)))
        print("\r ETA: {ETA:6.1f}s [{perc:4.0%}] [{ppo}] {prog:4.0f} / {leng} | elapsed time {iter_t:.2f}".format(
            ETA=ETA,
            perc=perc,
            ppo=ppo,
            prog=prog,
            leng=len(lst),
            iter_t=iter_t),
            end='')
        yield item



def main():
    """docstring for main"""
    listy = range(10)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if (__name__=='__main__'):
    main()
