/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:19 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:20 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Moves the top node of one stack onto another.
 *
 * Caller must already have checked src is not empty. Runs in O(1):
 * detaching from src and prepending to dest only touch the nodes
 * directly involved, and dest's cached tail is either the moved node
 * itself (if dest was empty) or carried over unchanged from dest's
 * previous head.
 *
 * @param dest Pointer to the destination stack, receives the node.
 * @param src Pointer to the source stack, loses its top node.
 * @return void
 */
static void	move_top(t_stack **dest, t_stack **src)
{
	t_stack	*node;
	t_stack	*old_dest_head;

	node = *src;
	*src = node->next;
	if (*src)
	{
		(*src)->prev = NULL;
		(*src)->tail = node->tail;
	}
	old_dest_head = *dest;
	node->next = old_dest_head;
	node->prev = NULL;
	if (old_dest_head)
	{
		old_dest_head->prev = node;
		node->tail = old_dest_head->tail;
	}
	else
		node->tail = node;
	*dest = node;
}

/**
 * @brief Pushes the top of b onto the top of a.
 *
 * Does nothing if b is empty.
 *
 * @param a Pointer to the destination stack.
 * @param b Pointer to the source stack.
 * @param print 1 to print "pa\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_pa(t_stack **a, t_stack **b, int print, t_bench *bench)
{
	if (!*b)
		return ;
	move_top(a, b);
	if (bench)
		bench->pa++;
	if (print)
		write(1, "pa\n", 3);
}

/**
 * @brief Pushes the top of a onto the top of b.
 *
 * Does nothing if a is empty.
 *
 * @param a Pointer to the source stack.
 * @param b Pointer to the destination stack.
 * @param print 1 to print "pb\n" to stdout, 0 to stay silent.
 * @param bench Optional operation counter, or NULL if unused.
 * @return void
 */
void	ft_pb(t_stack **a, t_stack **b, int print, t_bench *bench)
{
	if (!*a)
		return ;
	move_top(b, a);
	if (bench)
		bench->pb++;
	if (print)
		write(1, "pb\n", 3);
}
