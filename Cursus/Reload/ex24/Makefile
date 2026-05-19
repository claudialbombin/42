# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/18 19:13:57 by claudialbom       #+#    #+#              #
#    Updated: 2026/05/18 19:13:58 by claudialbom      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a
CC = gcc
CFLAGS = -Wall -Wextra -Werror
SRCS_DIR = srcs
INCLUDES_DIR = includes
SRCS = $(SRCS_DIR)/ft_putchar.c $(SRCS_DIR)/ft_putstr.c $(SRCS_DIR)/ft_strcmp.c \
       $(SRCS_DIR)/ft_strlen.c $(SRCS_DIR)/ft_swap.c
OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -I $(INCLUDES_DIR) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re