/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   disorder_index.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:36 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:04:37 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Counts ordering mistakes (inversions) in a stack.
 *
 * Goes through every pair (i, j) with j > i, comparing values. Each
 * time a bigger value appears before a smaller one, that counts as an
 * "inversion" (an ordering mistake).
 *
 * @param a Stack to inspect.
 * @return Total number of inversions found.
 */
static int	count_mistakes(t_stack *a)
{
	t_stack	*first;
	t_stack	*second;
	int		mistakes;

	mistakes = 0;
	first = a;
	while (first)
	{
		second = first->next;
		while (second)
		{
			if (first->value > second->value)
				mistakes++;
			second = second->next;
		}
		first = first->next;
	}
	return (mistakes);
}

/**
 * @brief Computes how disordered a stack is, as a value in [0, 1].
 *
 * disorder index = mistakes / total_pairs. With 0 or 1 elements there
 * are no pairs, so it is treated as 0. Must be called before any move
 * is applied to the stack.
 *
 * @param a Stack to inspect.
 * @return Disorder index between 0.0 (sorted) and 1.0 (fully reversed).
 */
double	compute_disorder(t_stack *a)
{
	int	size;
	int	total_pairs;
	int	mistakes;

	size = ft_stack_size(a);
	if (size <= 1)
		return (0.0);
	total_pairs = size * (size - 1) / 2;
	mistakes = count_mistakes(a);
	return ((double)mistakes / (double)total_pairs);
}
