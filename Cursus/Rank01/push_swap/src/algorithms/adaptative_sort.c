/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   adaptative_sort.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:15 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:04:17 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Sorts stack a, picking a strategy based on its disorder index.
 *
 * Low disorder tries the O(n) rotation fix first (falling back to the
 * O(n log n) sort if that guess turns out wrong), medium disorder uses
 * the chunk-based sort, high disorder uses radix sort.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	ft_adaptive_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	double	disorder;

	if (ft_is_sorted(*a))
		return ;
	disorder = compute_disorder(*a);
	if (disorder < 0.2)
		ft_linear_sort(a, b, bench);
	else if (disorder < 0.5)
		ft_medium_sort(a, b, bench);
	else
		ft_complex_sort(a, b, bench);
}
