/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:06:10 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:06:11 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Counts the number of nodes in a stack.
 *
 * @param stack Stack to count.
 * @return Number of nodes in stack.
 */
int	ft_stack_size(t_stack *stack)
{
	int	size;

	size = 0;
	while (stack)
	{
		size++;
		stack = stack->next;
	}
	return (size);
}

/**
 * @brief Checks whether a stack is sorted in ascending order.
 *
 * @param a Stack to check.
 * @return 1 if a is sorted ascending, 0 otherwise.
 */
int	ft_is_sorted(t_stack *a)
{
	while (a && a->next)
	{
		if (a->value > a->next->value)
			return (0);
		a = a->next;
	}
	return (1);
}

/**
 * @brief Finds the position of the minimum value in a stack.
 *
 * @param a Stack to search; must not be NULL.
 * @return Index (from the top, 0-based) of the minimum value.
 */
int	ft_min_index(t_stack *a)
{
	t_stack	*current;
	int		index;
	int		min_index;
	int		min_value;

	index = 0;
	min_index = 0;
	min_value = a->value;
	current = a;
	while (current)
	{
		if (current->value < min_value)
		{
			min_value = current->value;
			min_index = index;
		}
		index++;
		current = current->next;
	}
	return (min_index);
}

/**
 * @brief Frees every node of a stack and clears the caller's pointer.
 *
 * Frees every node of a stack one by one, then makes sure the
 * caller's pointer is set to NULL so it can't be used by accident
 * after being freed.
 *
 * @param stack Pointer to the stack to free.
 * @return void
 */
void	ft_free_stack(t_stack **stack)
{
	t_stack	*current;
	t_stack	*next;

	current = *stack;
	while (current)
	{
		next = current->next;
		free(current);
		current = next;
	}
	*stack = NULL;
}
