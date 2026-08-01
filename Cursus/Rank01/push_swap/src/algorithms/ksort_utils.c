/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ksort_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:46 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:04:47 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Calculates the stack's median.
 *
 * @param b Pointer to the stack to analyze.
 * @return The index value representing the median.
 */

int	ft_get_median(t_stack **b)
{
	return (ft_stack_size(*b) / 2);
}

/**
 * @brief Finds the maximum value in a stack.
 *
 * @param a Stack to search; must not be NULL.
 * @return Index (from the top, 0-based) of the maximum value.
 */

int	ft_stack_max(t_stack *a)
{
	t_stack	*check;

	if (!a)
		return (-1);
	check = a;
	a = a->next;
	while (a)
	{
		if ((check->index) < a->index)
			check = a;
		a = a->next;
	}
	return (check->index);
}

/**
 * @brief Calculates the integer square root of a number.
 *
 * @param n The integer whose square root is to be calculated.
 * @return The calculated integer square root, rounded up.
 */

int	ft_sqr_rt(int n)
{
	int	res;

	res = 0;
	while (res * res < n)
		res++;
	return (res);
}
