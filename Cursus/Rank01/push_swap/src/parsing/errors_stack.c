/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   errors_stack.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:10:46 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:10:47 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Frees every node of a stack.
 *
 * @param stack Stack to free.
 * @return void
 */
void	free_stack(t_stack *stack)
{
	t_stack	*aux;

	while (stack != NULL)
	{
		aux = stack->next;
		free(stack);
		stack = aux;
	}
}

/**
 * @brief Frees both stacks, prints "Error" and exits with status 1.
 *
 * @param a Main stack to free before exiting, or NULL.
 * @param b Auxiliary stack to free before exiting, or NULL.
 * @return This function never returns; it calls exit(1).
 */
void	exit_error(t_stack *a, t_stack *b)
{
	free_stack(a);
	free_stack(b);
	write(2, "Error\n", 6);
	exit(1);
}
