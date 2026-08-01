/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   small_sort_bfs.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:49 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:50 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Checks whether two abstract BFS states are identical.
 *
 * @param x First state to compare.
 * @param y Second state to compare.
 * @return 1 if both a and b arrays match exactly, 0 otherwise.
 */
static int	states_equal(t_state *x, t_state *y)
{
	int	i;

	if (x->a_len != y->a_len || x->b_len != y->b_len)
		return (0);
	i = 0;
	while (i < x->a_len && x->a[i] == y->a[i])
		i++;
	if (i < x->a_len)
		return (0);
	i = 0;
	while (i < x->b_len && x->b[i] == y->b[i])
		i++;
	return (i == x->b_len);
}

/**
 * @brief Checks whether a state is the fully sorted goal state.
 *
 * @param s State to check.
 * @param size Expected number of elements in the sorted stack.
 * @return 1 if b is empty and a holds ranks 0..size-1 in order,
 *         0 otherwise.
 */
static int	is_goal(t_state *s, int size)
{
	int	i;

	if (s->b_len != 0 || s->a_len != size)
		return (0);
	i = 0;
	while (i < size && s->a[i] == i)
		i++;
	return (i == size);
}

/**
 * @brief Checks whether a state has already been discovered by BFS.
 *
 * @param states Array of states discovered so far.
 * @param count Number of valid entries in states.
 * @param next Candidate state to look up.
 * @return 1 if an equal state is already in states, 0 otherwise.
 */
static int	already_visited(t_state *states, int count, t_state *next)
{
	int	i;

	i = 0;
	while (i < count)
	{
		if (states_equal(&states[i], next))
			return (1);
		i++;
	}
	return (0);
}

/**
 * @brief Expands a BFS state by trying every possible move from it.
 *
 * For each of the 11 moves, applies it to a copy of states[head] and,
 * if the resulting state hasn't been seen before, appends it to
 * states with its parent and move recorded.
 *
 * @param states Array of discovered states, grown in place.
 * @param count Pointer to the number of valid entries in states.
 * @param head Index of the state to expand.
 * @return void
 */
static void	expand_state(t_state *states, int *count, int head)
{
	int		move_id;
	t_state	next;

	move_id = 0;
	while (move_id < 11 && *count < MAX_SMALL_STATES)
	{
		next = states[head];
		apply_move(move_id, &next);
		if (!already_visited(states, *count, &next))
		{
			next.parent = head;
			next.move = move_id;
			states[*count] = next;
			(*count)++;
		}
		move_id++;
	}
}

/**
 * @brief Finds the shortest move sequence to sort a small stack.
 *
 * Breadth-first search over every reachable (a, b) arrangement,
 * starting from "start". BFS visits states in non-decreasing order of
 * move count, so the first time the goal is dequeued it has
 * necessarily been reached by the shortest possible sequence of moves.
 *
 * @param states Array used to store every discovered state, indexed
 *               from 0; filled in by this function.
 * @param start Starting abstract state.
 * @param size Number of elements to sort.
 * @return Index in states of the goal state (usable to walk
 *         parent/move back to the start), or -1 if never found.
 */
int	bfs_solve(t_state *states, t_state *start, int size)
{
	int	count;
	int	head;

	states[0] = *start;
	states[0].parent = -1;
	states[0].move = -1;
	count = 1;
	head = 0;
	while (head < count)
	{
		if (is_goal(&states[head], size))
			return (head);
		expand_state(states, &count, head);
		head++;
	}
	return (-1);
}
