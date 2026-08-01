/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   linear_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:54 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:04:55 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Walks forward a fixed number of nodes from a stack pointer.
 *
 * @param a Starting node.
 * @param index Number of nodes to walk forward.
 * @return The node reached after walking "index" steps.
 */
static t_stack	*node_at(t_stack *a, int index)
{
	while (index-- > 0)
		a = a->next;
	return (a);
}

/**
 * @brief Checks whether a stack is a sorted sequence that was rotated.
 *
 * A stack whose disorder index is this low is, in practice, either
 * already sorted or the sorted sequence rotated by some offset (eg.
 * the last k values moved in front of the rest). Walking once from
 * the minimum all the way back around to it must find every value
 * strictly increasing - if it doesn't, the stack isn't a pure rotation.
 *
 * @param a Stack to inspect.
 * @param min_index Index (from the top) of the stack's minimum value.
 * @param size Number of elements in the stack.
 * @return 1 if the stack is a rotated sorted sequence, 0 otherwise.
 */
static int	is_rotated_sorted(t_stack *a, int min_index, int size)
{
	t_stack	*current;
	int		i;
	int		prev;

	if (size <= 1)
		return (1);
	current = node_at(a, min_index);
	prev = current->value;
	i = 1;
	while (i < size)
	{
		current = current->next;
		if (!current)
			current = a;
		if (current->value < prev)
			return (0);
		prev = current->value;
		i++;
	}
	return (1);
}

/**
 * @brief Rotates the stack so its minimum ends up on top.
 *
 * Picks whichever rotation direction (ra or rra) needs fewer moves.
 *
 * @param a Pointer to the stack to rotate.
 * @param min_index Index (from the top) of the minimum value.
 * @param size Number of elements in the stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
static void	rotate_min_to_top(t_stack **a, int min_index, int size,
		t_bench *bench)
{
	if (min_index <= size - min_index)
	{
		while (min_index-- > 0)
			ft_ra(a, 1, bench);
	}
	else
	{
		min_index = size - min_index;
		while (min_index-- > 0)
			ft_rra(a, 1, bench);
	}
}

/**
 * @brief Sorts stack a in O(n) for the low-disorder regime.
 *
 * Finds the minimum (O(n)) and rotates it to the top the short way
 * (O(n)) - if the stack really was just a rotated sorted sequence,
 * that alone leaves it fully sorted. A true O(n) comparison sort
 * can't exist for every permutation in this regime (disorder only
 * bounds how many inversions there are, not the stack's shape), so as
 * a correctness safety net, the rare low-disorder stack that isn't a
 * pure rotation falls back to ft_complex_sort - that path is no
 * longer O(n), but it never produces a wrong result.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	ft_linear_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	size;
	int	min_index;

	if (ft_is_sorted(*a))
		return ;
	size = ft_stack_size(*a);
	min_index = ft_min_index(*a);
	if (!is_rotated_sorted(*a, min_index, size))
	{
		ft_complex_sort(a, b, bench);
		return ;
	}
	rotate_min_to_top(a, min_index, size, bench);
}
