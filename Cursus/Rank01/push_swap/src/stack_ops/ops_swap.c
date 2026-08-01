/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_swap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:34 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:35 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Swaps the two top nodes of a stack.
 *
 * Caller must already have checked the stack has >= 2 elements. Runs
 * in O(1): only relinks the first three nodes and updates the new
 * head's cached tail (which changes to "first" itself when the stack
 * has exactly 2 elements, since first is then the new last node).
 *
 * @param s Pointer to the stack whose top two nodes are swapped.
 * @return void
 */
static void	swap_top(t_stack **s)
{
	t_stack	*first;
	t_stack	*second;

	first = *s;
	second = first->next;
	first->next = second->next;
	if (first->next)
	{
		first->next->prev = first;
		second->tail = first->tail;
	}
	else
		second->tail = first;
	second->prev = NULL;
	first->prev = second;
	second->next = first;
	*s = second;
}

/**
 * @brief Swaps the two top nodes of stack a.
 *
 * Does nothing if a has fewer than 2 elements.
 *
 * @param a Pointer to the stack to swap.
 * @param print 1 to print "sa\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_sa(t_stack **a, int print, t_bench *bench)
{
	if (!*a || !(*a)->next)
		return ;
	swap_top(a);
	if (bench)
		bench->sa++;
	if (print)
		write(1, "sa\n", 3);
}

/**
 * @brief Swaps the two top nodes of stack b.
 *
 * Does nothing if b has fewer than 2 elements.
 *
 * @param b Pointer to the stack to swap.
 * @param print 1 to print "sb\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_sb(t_stack **b, int print, t_bench *bench)
{
	if (!*b || !(*b)->next)
		return ;
	swap_top(b);
	if (bench)
		bench->sb++;
	if (print)
		write(1, "sb\n", 3);
}

/**
 * @brief Swaps the two top nodes of both stacks a and b at once.
 *
 * ss does sa and sb at the same time, printing (and counting) just
 * one combined operation instead of two.
 *
 * @param a Pointer to the first stack to swap.
 * @param b Pointer to the second stack to swap.
 * @param print 1 to print "ss\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_ss(t_stack **a, t_stack **b, int print, t_bench *bench)
{
	if (*a && (*a)->next)
		swap_top(a);
	if (*b && (*b)->next)
		swap_top(b);
	if (bench)
		bench->ss++;
	if (print)
		write(1, "ss\n", 3);
}
