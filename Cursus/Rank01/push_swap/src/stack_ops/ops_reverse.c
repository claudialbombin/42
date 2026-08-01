/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_reverse.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:22 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:23 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Reverse rotates a stack downwards by one position.
 *
 * The last element becomes the first one, everything else shifts
 * down by one position. Caller must already have checked the stack
 * has >= 2 elements. Runs in O(1): the old tail's prev pointer gives
 * the new tail directly, no traversal needed.
 *
 * @param s Pointer to the stack to rotate.
 * @return void
 */
static void	rotate_down(t_stack **s)
{
	t_stack	*old_head;
	t_stack	*old_tail;
	t_stack	*new_tail;

	old_head = *s;
	old_tail = old_head->tail;
	new_tail = old_tail->prev;
	new_tail->next = NULL;
	old_tail->next = old_head;
	old_tail->prev = NULL;
	old_head->prev = old_tail;
	old_tail->tail = new_tail;
	*s = old_tail;
}

/**
 * @brief Reverse rotates stack a by one position.
 *
 * Does nothing if a has fewer than 2 elements.
 *
 * @param a Pointer to the stack to rotate.
 * @param print 1 to print "rra\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_rra(t_stack **a, int print, t_bench *bench)
{
	if (!*a || !(*a)->next)
		return ;
	rotate_down(a);
	if (bench)
		bench->rra++;
	if (print)
		write(1, "rra\n", 4);
}

/**
 * @brief Reverse rotates stack b by one position.
 *
 * Does nothing if b has fewer than 2 elements.
 *
 * @param b Pointer to the stack to rotate.
 * @param print 1 to print "rrb\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_rrb(t_stack **b, int print, t_bench *bench)
{
	if (!*b || !(*b)->next)
		return ;
	rotate_down(b);
	if (bench)
		bench->rrb++;
	if (print)
		write(1, "rrb\n", 4);
}

/**
 * @brief Reverse rotates both stacks a and b at the same time.
 *
 * rrr does rra and rrb at the same time, printing (and counting) just
 * one combined operation instead of two.
 *
 * @param a Pointer to the first stack to rotate.
 * @param b Pointer to the second stack to rotate.
 * @param print 1 to print "rrr\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_rrr(t_stack **a, t_stack **b, int print, t_bench *bench)
{
	if (*a && (*a)->next)
		rotate_down(a);
	if (*b && (*b)->next)
		rotate_down(b);
	if (bench)
		bench->rrr++;
	if (print)
		write(1, "rrr\n", 4);
}
