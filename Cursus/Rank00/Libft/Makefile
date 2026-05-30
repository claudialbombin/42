# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#              #
#    Updated: 2026/05/18 15:54:24 by claudialbom      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Name of the library to be created
NAME = libft.a

# Compiler and compilation flags
CC = gcc
# Flags: -Wall (all warnings), -Wextra (extra warnings), -Werror (treat warnings as errors)
CFLAGS = -Wall -Wextra -Werror

# List of source files to compile
	SRCS =	ft_memset.c \
		ft_bzero.c \
		ft_memcpy.c \
		ft_memccpy.c \
		ft_memmove.c \
		ft_memchr.c \
		ft_memcmp.c \
		ft_strlen.c \
		ft_strdup.c \
		ft_strcpy.c \
		ft_strncpy.c \
		ft_strcat.c \
		ft_strncat.c \
		ft_strlcat.c \
		ft_strchr.c \
		ft_strrchr.c \
		ft_strstr.c \
		ft_strnstr.c \
		ft_strcmp.c \
		ft_strncmp.c \
		ft_atoi.c \
		ft_isalpha.c \
		ft_isdigit.c \
		ft_isalnum.c \
		ft_isascii.c \
		ft_isprint.c \
		ft_toupper.c \
		ft_tolower.c \
		ft_memalloc.c \
		ft_memdel.c \
		ft_strnew.c \
		ft_strdel.c \
		ft_strclr.c \
		ft_striter.c \
		ft_striteri.c \
		ft_strmap.c \
		ft_strmapi.c \
		ft_strequ.c \
		ft_strnequ.c \
		ft_strsub.c \
		ft_strjoin.c \
		ft_strtrim.c \
		ft_strsplit.c \
		ft_itoa.c \
		ft_putchar.c \
		ft_putstr.c \
		ft_putendl.c \
		ft_putnbr.c \
		ft_putchar_fd.c \
		ft_putstr_fd.c \
		ft_putendl_fd.c \
		ft_putnbr_fd.c \
		ft_lstnew.c \
		ft_lstdelone.c \
		ft_lstdel.c \
		ft_lstadd.c \
		ft_lstiter.c \
		ft_lstmap.c

# Object files: substitutes .c with .o for each source file
OBJS = $(SRCS:.c=.o)

# Default target: builds the library
all: $(NAME)

# Builds the static library from object files
$(NAME): $(OBJS)
	ar rc $(NAME) $(OBJS)
	ranlib $(NAME)

# Removes object files only
clean:
	rm -f $(OBJS)

# Removes object files and the library (full clean)
fclean: clean
	rm -f $(NAME)

# Rebuilds everything: removes old files and compiles again
re: fclean all

# Marks these targets as not actual files (phony targets)
.PHONY: all clean fclean re
