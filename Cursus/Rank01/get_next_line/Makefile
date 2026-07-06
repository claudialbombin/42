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

NAME = gnl_test
NAME_BONUS = gnl_test_bonus

CC = cc
CFLAGS = -Wall -Wextra -Werror

SRCS =  get_next_line.c \
        get_next_line_utils.c \
        main_test.c

SRCS_BONUS =    get_next_line_bonus.c \
                get_next_line_utils_bonus.c \
                main_test_bonus.c

# Object files: substitutes .c with .o for each source file
OBJS = $(SRCS:.c=.o)
OBJS_BONUS = $(SRCS_BONUS:.c=.o)

# Default target: builds the mandatory test binary
all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

# Builds the bonus test binary (multiple simultaneous file descriptors)
bonus: $(NAME_BONUS)

$(NAME_BONUS): $(OBJS_BONUS)
	$(CC) $(CFLAGS) $(OBJS_BONUS) -o $(NAME_BONUS)

# Removes object files only
clean:
	rm -f $(OBJS) $(OBJS_BONUS)

# Removes object files and the binaries (full clean)
fclean: clean
	rm -f $(NAME) $(NAME_BONUS)

# Rebuilds everything: removes old files and compiles again
re: fclean all

# Marks these targets as not actual files (phony targets)
.PHONY: all bonus clean fclean re
