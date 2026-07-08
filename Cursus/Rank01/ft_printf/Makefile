# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: claudialbombin                                 +#+  +:+       +#+     #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06                               #+#    #+#              #
#    Updated: 2026/07/06                               ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a
TEST_NAME = printf_test

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rc
RANLIB = ranlib

SRCS =  ft_printf.c \
        ft_putchar_count.c \
        ft_putstr_count.c \
        ft_putnbr_count.c \
        ft_putunbr_count.c \
        ft_puthex_count.c \
        ft_putptr_count.c

OBJS = $(SRCS:.c=.o)

# Default target: builds the static library
all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)
	$(RANLIB) $(NAME)

# Builds a small test binary comparing ft_printf against the libc printf
test: $(NAME)
	$(CC) $(CFLAGS) -I. mains/main_test.c $(NAME) -o $(TEST_NAME)

# Removes object files only
clean:
	rm -f $(OBJS)

# Removes object files, the library and the test binary (full clean)
fclean: clean
	rm -f $(NAME) $(TEST_NAME)

# Rebuilds everything: removes old files and compiles again
re: fclean all

# Marks these targets as not actual files (phony targets)
.PHONY: all test clean fclean re
