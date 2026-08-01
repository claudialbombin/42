/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker_bonus.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pvivas-f <pvivas-f@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:09:58 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 15:34:40 by pvivas-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "checker_bonus.h"

/**
 * @brief Prints "OK\n" or "KO\n" to stdout depending on the result.
 *
 * "a is sorted and b is empty" is the only success condition the
 * subject defines - anything else, including a non-empty b, is KO.
 *
 * @param a Final state of stack a.
 * @param b Final state of stack b.
 * @return void
 */
static void	checker_print_result(t_stack *a, t_stack *b)
{
	if (ft_is_sorted(a) && !b)
		write(1, "OK\n", 3);
	else
		write(1, "KO\n", 3);
}

/**
 * @brief Reads and applies instructions from standard input.
 *
 * Reads each instruction line provided through stdin using get_next_line
 * and applies it immediately to the given stacks. If an invalid instruction
 * is encountered, frees the allocated memory for the current line and exits
 * with an error, as required by the checker behavior.
 *
 * The function processes instructions in the same order they are received
 * and stops when stdin reaches EOF.
 *
 * @param a Stack A to be modified by the instructions.
 * @param b Stack B to be modified by the instructions.
 *
 * @return void
 */
void	checker_read_stdin(t_stack *a, t_stack *b)
{
	char	*line;

	line = get_next_line(0);
	while (line)
	{
		if (line[ft_strlen(line) - 1] == '\n')
			line[ft_strlen(line) - 1] = '\0';
		if (!(checker_apply_line(line, &a, &b)))
		{
			free (line);
			exit_error(a, b);
		}
		free (line);
		line = get_next_line(0);
	}
	free(line);
}

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;

	if (argc <= 1)
		return (0);
	a = ft_build_stack(argc, argv);
	b = NULL;
	checker_read_stdin(a, b);
	checker_print_result(a, b);
	ft_free_stack(&a);
	ft_free_stack(&b);
	return (0);
}
