# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#              #
#    Updated: 2026/05/16 18:00:30 by claudialbom      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Name of the library to be created
NAME = libft.a

# Compiler and compilation flags
CC = gcc
# Flags: -Wall (all warnings), -Wextra (extra warnings), -Werror (treat warnings as errors)
CFLAGS = -Wall -Wextra -Werror

# List of source files to compile
SRCS =	memset.c \
		bzero.c \
		memcpy.c \
		memccpy.c \
		memmove.c \
		memchr.c \
		memcmp.c \
		strlen.c \
		strdup.c \
		strcpy.c \
		strncpy.c \
		strcat.c \
		strncat.c \
		strlcat.c \
		strchr.c \
		strrchr.c \
		strstr.c \
		strnstr.c \
		strcmp.c \
		strncmp.c \
		atoi.c \
		isalpha.c \
		isdigit.c \
		isalnum.c \
		isascii.c \
		isprint.c \
		toupper.c \
		tolower.c \
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
