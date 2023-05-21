# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/11 16:39:55 by begarijo          #+#    #+#              #
#    Updated: 2023/05/17 12:14:39 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

export INC = "-I/Users/begarijo/.brew/opt/openssl@1.1/include"
export LIB = "-L/Users/begarijo/.brew/opt/openssl@1.1/lib"

CFLAGS  =   -Werror -Wall -Wextra

all:
	@clear
	gcc corsair.c $(CFLAGS) $(INC) $(LIB) -lssl -lcrypto -o corsair
	@./corsair cert1.pem cert2.pem passwd.enc