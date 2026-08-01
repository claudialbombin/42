/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:29 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:30 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Rotates a stack upwards by one position.
 *
 * The first element becomes the last one, everything else shifts up
 * by one position. Caller must already have checked the stack has at
 * least 2 elements. Runs in O(1): the old head's cached tail says
 * exactly where to reattach it, no traversal needed.
 *
 * @param s Pointer to the stack to rotate.
 * @return void
 */
static void	rotate_up(t_stack **s)
{
	t_stack	*old_head;
	t_stack	*new_head;
	t_stack	*old_tail;

	old_head = *s;
	new_head = old_head->next;
	old_tail = old_head->tail;
	new_head->prev = NULL;
	old_tail->next = old_head;
	old_head->prev = old_tail;
	old_head->next = NULL;
	new_head->tail = old_head;
	*s = new_head;
}

/**
 * @brief Rotates stack a upwards by one position.
 *
 * Does nothing if a has fewer than 2 elements.
 *
 * @param a Pointer to the stack to rotate.
 * @param print 1 to print "ra\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_ra(t_stack **a, int print, t_bench *bench)
{
	if (!*a || !(*a)->next)
		return ;
	rotate_up(a);
	if (bench)
		bench->ra++;
	if (print)
		write(1, "ra\n", 3);
}

/**
 * @brief Rotates stack b upwards by one position.
 *
 * Does nothing if b has fewer than 2 elements.
 *
 * @param b Pointer to the stack to rotate.
 * @param print 1 to print "rb\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_rb(t_stack **b, int print, t_bench *bench)
{
	if (!*b || !(*b)->next)
		return ;
	rotate_up(b);
	if (bench)
		bench->rb++;
	if (print)
		write(1, "rb\n", 3);
}

/**
 * @brief Rotates both stacks a and b upwards at the same time.
 *
 * rr does ra and rb at the same time, printing (and counting) just
 * one combined operation instead of two.
 *
 * @param a Pointer to the first stack to rotate.
 * @param b Pointer to the second stack to rotate.
 * @param print 1 to print "rr\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_rr(t_stack **a, t_stack **b, int print, t_bench *bench)
{
	if (*a && (*a)->next)
		rotate_up(a);
	if (*b && (*b)->next)
		rotate_up(b);
	if (bench)
		bench->rr++;
	if (print)
		write(1, "rr\n", 3);
}
