/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort_chunk_sort.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:59 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:00 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Finds the node with the highest rank currently in b.
 *
 * After extract_chunk, b holds only this chunk's elements (at most
 * sqrt(n) of them) - a plain linear scan for the current max is
 * cheap here precisely because b is small, unlike scanning the full
 * stack.
 *
 * @param b Stack to search (only ever holds one chunk's elements).
 * @return The node with the highest rank, or NULL if b is empty.
 */
static t_stack	*find_max_in_b(t_stack *b)
{
	t_stack	*best;

	best = b;
	while (b)
	{
		if (b->index > best->index)
			best = b;
		b = b->next;
	}
	return (best);
}

/**
 * @brief Rotates b until "node" reaches the top.
 *
 * @param b Pointer to the stack to rotate.
 * @param node Node to bring to the top.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
static void	rotate_to_top_b(t_stack **b, t_stack *node, t_bench *bench)
{
	t_stack	*current;
	int		pos;
	int		size;

	pos = 0;
	current = *b;
	while (current != node)
	{
		pos++;
		current = current->next;
	}
	size = ft_stack_size(*b);
	if (pos <= size - pos)
	{
		while (pos-- > 0)
			ft_rb(b, 1, bench);
	}
	else
	{
		pos = size - pos;
		while (pos-- > 0)
			ft_rrb(b, 1, bench);
	}
}

/**
 * @brief Drains an already-isolated chunk from b into a, sorted.
 *
 * Drains an already-isolated chunk (everything currently in b) back
 * into a, largest first. Since pa always inserts at the new top,
 * pushing largest-to-smallest leaves that chunk's own values
 * ascending from the top once it's done - exactly what's needed so
 * that stacking one chunk's ascending run on top of the previous one
 * (processing chunks highest rank first) ends up fully sorted.
 *
 * @param a Pointer to the main stack receiving the sorted chunk.
 * @param b Pointer to the stack holding this chunk's elements.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	drain_chunk_sorted(t_stack **a, t_stack **b, t_bench *bench)
{
	t_stack	*node;

	node = find_max_in_b(*b);
	while (node)
	{
		rotate_to_top_b(b, node, bench);
		ft_pa(a, b, 1, bench);
		node = find_max_in_b(*b);
	}
}
