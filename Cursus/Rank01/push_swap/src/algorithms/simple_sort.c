/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:24 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:13:11 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Brings the node at a given position to the top of a.
 *
 * Chooses whichever rotation direction needs fewer moves.
 *
 * @param a Pointer to the stack to rotate.
 * @param index Position (from the top) of the node to bring up.
 * @param size Number of elements in the stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
static void	rotate_to_top(t_stack **a, int index, int size, t_bench *bench)
{
	if (index <= size - index)
	{
		while (index > 0)
		{
			ft_ra(a, 1, bench);
			index--;
		}
	}
	else
	{
		index = size - index;
		while (index > 0)
		{
			ft_rra(a, 1, bench);
			index--;
		}
	}
}

/**
 * @brief Sorts stack a in O(n^2) using a selection-sort approach.
 *
 * n times, finds the current minimum of a, rotates it to the top and
 * pushes it to b. The very last element left in a is automatically
 * the maximum, so it stops at size 1 instead of moving it too.
 * Finally, pushes everything back from b to a in the right order.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	ft_simple_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	size;
	int	index;

	if (ft_is_sorted(*a))
		return ;
	size = ft_stack_size(*a);
	while (size > 1)
	{
		index = ft_min_index(*a);
		rotate_to_top(a, index, size, bench);
		ft_pb(a, b, 1, bench);
		size--;
	}
	while (*b)
		ft_pa(a, b, 1, bench);
}
