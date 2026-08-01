/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   nodes.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:01 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:02 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Allocates a new stack node holding the given value.
 *
 * @param value Value to store in the new node.
 * @return The newly allocated node (index 0, next/prev/tail NULL), or
 *         NULL if allocation failed.
 */
t_stack	*create_node(int value)
{
	t_stack	*node;

	node = malloc(sizeof(t_stack));
	if (!node)
		return (NULL);
	node->value = value;
	node->index = 0;
	node->next = NULL;
	node->prev = NULL;
	node->tail = NULL;
	return (node);
}

/**
 * @brief Appends a node at the end of a list.
 *
 * Keeps *tail up to date so the caller doesn't have to walk the whole
 * list again for the next append, and links node->prev to the
 * previous tail so the list stays properly doubly-linked.
 *
 * @param head Pointer to the list's head, set if the list was empty.
 * @param tail Pointer to the list's tail, updated to node.
 * @param node Node to append; its next pointer is not touched here.
 * @return void
 */
void	add_node(t_stack **head, t_stack **tail, t_stack *node)
{
	node->prev = *tail;
	if (!*head)
		*head = node;
	else
		(*tail)->next = node;
	*tail = node;
}
