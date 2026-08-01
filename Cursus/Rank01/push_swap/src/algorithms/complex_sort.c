/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:26 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:13:54 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Assigns each node its rank based on relative value order.
 *
 * Radix sort needs each value's rank (0 to n - 1) instead of its raw
 * value, since ranks are the smallest possible range of numbers to
 * look at bit by bit. The rank of a node is simply how many other
 * nodes hold a smaller value.
 *
 * @param a Stack whose nodes get their index field filled in.
 * @return void
 */
static void	assign_indexes(t_stack *a)
{
	t_stack	*current;
	t_stack	*other;
	int		count;

	current = a;
	while (current)
	{
		other = a;
		count = 0;
		while (other)
		{
			if (other->value < current->value)
				count++;
			other = other->next;
		}
		current->index = count;
		current = current->next;
	}
}

/**
 * @brief Finds the physical position of a specific node by its index.
 *
 * Scans the stack from top to bottom to calculate the zero-based
 * distance of the node that matches the requested target index.
 *
 * @param b Pointer to the stack to be scanned.
 * @param max_idx The target index value to look for.
 * @return The physical position (0 to size - 1), or -1 if the stack is empty.
 */
int	get_max_pos(t_stack *b, int max_idx)
{
	int		pos;

	pos = 0;
	if (!b)
		return (-1);
	while (b && b->index != max_idx)
	{
		pos++;
		b = b->next;
	}
	return (pos);
}

/**
 * @brief Pushes nodes from stack B back to stack A in descending order.
 *
 * It continuously identifies the maximum index in stack B and rotates 
 * the stack using the most efficient path to bring that element to 
 * the top. It also handles the second-highest element efficiently 
 * and performs swaps on stack A to optimize instructions.
 *
 * @param a Double pointer to the destination stack A.
 * @param b Double pointer to the source stack B.
 * @param bench Pointer to the benchmarking and instruction counter structure.
 * @return void
 */
void	ksort_back(t_stack **a, t_stack **b, t_bench *bench)
{
	int	max_idx;
	int	pos;

	if (!a || !b)
		return ;
	while (*b)
	{
		max_idx = ft_stack_max(*b);
		if ((*b)->index == max_idx)
		{
			ft_pa(a, b, 1, bench);
			if (*a && (*a)->next && (*a)->index > (*a)->next->index)
				ft_sa(a, 1, bench);
		}
		else if ((*b)->index == max_idx - 1)
			ft_pa(a, b, 1, bench);
		else
		{
			pos = get_max_pos(*b, max_idx);
			if (pos <= ft_get_median(b))
				ft_rb(b, 1, bench);
			else
				ft_rrb(b, 1, bench);
		}
	}
}

/**
 * @brief Sorts stack A using an optimized chunk-based pre-sort algorithm.
 *
 * It maps all values to simplified ranks and uses a dynamic window size (k) 
 * based on the square root of the stack size. Nodes are pushed to stack B 
 * in a sorted hour-glass or butterfly shape before being reassembled 
 * back into stack A in perfect ascending order.
 *
 * @param a Double pointer to the main stack A to be sorted.
 * @param b Double pointer to the auxiliary stack B.
 * @param bench Pointer to the benchmarking and instruction counter structure.
 * @return void
 */
void	ft_complex_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	k;
	int	counter;

	assign_indexes(*a);
	k = ft_sqr_rt(ft_stack_size(*a) * 1.4);
	counter = 0;
	while (*a)
	{
		if ((*a)->index < counter)
		{
			ft_pb(a, b, 1, bench);
			counter++;
		}
		else if ((*a)->index < counter + k)
		{
			ft_pb(a, b, 1, bench);
			ft_rb(b, 1, bench);
			counter++;
		}
		else
			ft_ra(a, 1, bench);
	}
	ksort_back(a, b, bench);
}
