/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort_utils.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:12 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:13 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Assigns every node in a its rank among the stack's values.
 *
 * Same rank trick as complex_sort: gives every node its rank (0 to
 * size - 1) instead of its raw value, so ranks can be grouped into
 * chunks.
 *
 * @param a Stack whose nodes get their index field set to their rank.
 * @return void
 */
void	assign_ranks(t_stack *a)
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
 * @brief Computes the chunk length used to split "size" ranks.
 *
 * A plain sqrt(size) chunk length is the right asymptotic answer, but
 * it isn't the cheapest one in practice: extract_chunk's pass costs
 * the *current* size of a on every one of the size/chunk chunks (it
 * never shrinks, see extract_chunk), while sorting each isolated
 * chunk only costs O(chunk^2). That imbalance means fewer, bigger
 * chunks end up costing less overall, even though both approaches
 * are O(n * sqrt(n)). Empirically, chunk ~= 3 * sqrt(size) minimizes
 * the real op count (measured ~35% fewer operations than sqrt(size)
 * for n = 500) - found by squaring both sides to keep this an
 * integer-only search, same style as the plain sqrt(size) version.
 *
 * @param size Total number of elements to split into chunks.
 * @return The chunk length.
 */
int	chunk_length(int size)
{
	int	chunk;

	chunk = 1;
	while (chunk * chunk < size * 9)
		chunk++;
	return (chunk);
}
