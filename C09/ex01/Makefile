# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/31 14:55:09 by claudialbom       #+#    #+#              #
#    Updated: 2025/07/31 14:55:34 by claudialbom      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Variables
NAME		= libft.a
CC			= cc
CFLAGS		= -Wall -Wextra -Werror
INCLUDES	= -I includes
SRCS_DIR	= srcs
OBJS_DIR	= srcs

# Source files
SRCS		= $(addprefix $(SRCS_DIR)/, ft_putchar.c ft_swap.c ft_putstr.c ft_strlen.c ft_strcmp.c)
OBJS		= $(SRCS:.c=.o)

# Rules
all: $(NAME)

$(NAME): $(OBJS)
	@ar rcs $(NAME) $(OBJS)
	@echo "Library $(NAME) created"

$(OBJS_DIR)/%.o: $(SRCS_DIR)/%.c
	@$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@
	@echo "Compiled $<"

clean:
	@rm -f $(OBJS)
	@echo "Removed object files"

fclean: clean
	@rm -f $(NAME)
	@echo "Removed $(NAME)"

re: fclean all

.PHONY: all clean fclean re