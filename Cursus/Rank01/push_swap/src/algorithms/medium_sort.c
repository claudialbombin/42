/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:18 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:19 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Sorts every chunk of ranks, highest range first.
 *
 * cfg[0] is the chunk length, cfg[1] the total size. Each chunk is
 * isolated into b in one bounded pass (extract_chunk) and drained
 * straight back into a, sorted (drain_chunk_sorted) - so a always
 * ends the loop with every chunk handled so far sitting correctly
 * ordered on top, and the next (lower) chunk's extraction pass
 * simply rotates straight past that already-sorted portion.
 *
 * @param a Pointer to the main stack.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param cfg Two-element array: cfg[0] = chunk length, cfg[1] = size.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
static void	sort_by_chunks(t_stack **a, t_stack **b, int *cfg, t_bench *bench)
{
	int	bounds[2];

	bounds[1] = cfg[1] - 1;
	while (bounds[1] >= 0)
	{
		bounds[0] = bounds[1] - cfg[0] + 1;
		if (bounds[0] < 0)
			bounds[0] = 0;
		extract_chunk(a, b, bounds, bench);
		drain_chunk_sorted(a, b, bench);
		bounds[1] = bounds[0] - 1;
	}
}

/**
 * @brief Sorts stack a in O(n * sqrt(n)) using a chunk-based sort.
 *
 * Splits the ranks into roughly sqrt(n) chunks. Every chunk-extraction
 * pass costs exactly the current size of a (bounded, see
 * extract_chunk), giving O(n * sqrt(n)) for that part; sorting each
 * isolated chunk of ~sqrt(n) elements costs O(sqrt(n)^2) = O(n), which
 * also sums to O(n * sqrt(n)) across all chunks.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	ft_medium_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	int	cfg[2];

	if (ft_is_sorted(*a))
		return ;
	assign_ranks(*a);
	cfg[1] = ft_stack_size(*a);
	cfg[0] = chunk_length(cfg[1]);
	sort_by_chunks(a, b, cfg, bench);
}
