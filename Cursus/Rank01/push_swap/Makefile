# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pvivas-f <pvivas-f@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/01 14:11:47 by clopez-b, p       #+#    #+#              #
#    Updated: 2026/08/01 15:15:04 by pvivas-f         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror
INCLUDES = -Iincludes

SRC =	src/main.c \
	src/parsing/parser_flags.c \
	src/parsing/parser_numbers.c \
	src/parsing/build_stack.c \
	src/parsing/nodes.c \
	src/parsing/errors_stack.c \
	src/parsing/split.c \
	src/parsing/utils.c \
	src/parsing/ft_atol.c \
	src/parsing/utils_parser_num.c \
	src/parsing/libft_utils.c \
	src/stack_ops/ops_push.c \
	src/stack_ops/ops_swap.c \
	src/stack_ops/ops_rotate.c \
	src/stack_ops/ops_reverse.c \
	src/algorithms/linear_sort.c \
	src/algorithms/small_sort.c \
	src/algorithms/small_sort_bfs.c \
	src/algorithms/small_sort_apply.c \
	src/algorithms/small_sort_moves.c \
	src/algorithms/small_sort_run.c \
	src/algorithms/simple_sort.c \
	src/algorithms/medium_sort.c \
	src/algorithms/medium_sort_utils.c \
	src/algorithms/medium_sort_extract.c \
	src/algorithms/medium_sort_chunk_sort.c \
	src/algorithms/complex_sort.c \
	src/algorithms/adaptative_sort.c \
	src/algorithms/sort_utils.c \
	src/algorithms/ksort_utils.c \
	src/algorithms/disorder_index.c \
	src/bench/bench.c \
	src/bench/bench_utils.c

NAME_CHECKER = checker

CHECKER_SRC =	src/checker_bonus/checker_bonus.c \
	src/checker_bonus/exec_instr_bonus.c \
	src/parsing/parser_flags.c \
	src/parsing/parser_numbers.c \
	src/parsing/build_stack.c \
	src/parsing/nodes.c \
	src/parsing/errors_stack.c \
	src/parsing/split.c \
	src/parsing/utils.c \
	src/parsing/ft_atol.c \
	src/parsing/utils_parser_num.c \
	src/parsing/libft_utils.c \
	src/stack_ops/ops_push.c \
	src/stack_ops/ops_swap.c \
	src/stack_ops/ops_rotate.c \
	src/stack_ops/ops_reverse.c \
	src/algorithms/sort_utils.c \
	src/algorithms/ksort_utils.c \
	src/checker_bonus/get_next_line.c \
	src/checker_bonus/get_next_line_utils.c

OBJ_DIR = obj
OBJ = $(SRC:src/%.c=$(OBJ_DIR)/%.o)
CHECKER_OBJ = $(CHECKER_SRC:src/%.c=$(OBJ_DIR)/%.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

bonus: $(NAME_CHECKER)

$(NAME_CHECKER): $(CHECKER_OBJ)
	$(CC) $(CFLAGS) $(CHECKER_OBJ) -o $(NAME_CHECKER)

$(OBJ_DIR)/%.o: src/%.c includes/push_swap.h includes/checker_bonus.h
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(NAME) $(NAME_CHECKER)

re: fclean all

.PHONY: all bonus clean fclean re
