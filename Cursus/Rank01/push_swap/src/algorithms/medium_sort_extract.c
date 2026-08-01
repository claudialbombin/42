/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort_extract.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:06 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:07 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Isolates one chunk's elements from a into b in a single pass.
 *
 * Same bounded single-pass trick as complex_sort's do_bit_pass, but
 * matching against a [lower, upper] rank range instead of a bit:
 * every element currently in a gets looked at exactly once (ra to
 * skip it, pb to grab it), so this always costs exactly the current
 * size of a - never more, regardless of how many elements match.
 * That's what keeps the chunk algorithm at O(n * sqrt(n)) instead of
 * O(n^2): each of the sqrt(n) chunk passes costs O(current size of
 * a), not O(a full rescan per selected element).
 *
 * @param a Pointer to the main stack, scanned once from the top.
 * @param b Pointer to the stack receiving this chunk's elements.
 * @param bounds Two-element array: bounds[0] = lower rank (inclusive),
 *               bounds[1] = upper rank (inclusive).
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	extract_chunk(t_stack **a, t_stack **b, int *bounds, t_bench *bench)
{
	int	i;
	int	size;

	size = ft_stack_size(*a);
	i = 0;
	while (i < size)
	{
		if ((*a)->index >= bounds[0] && (*a)->index <= bounds[1])
			ft_pb(a, b, 1, bench);
		else
			ft_ra(a, 1, bench);
		i++;
	}
}
