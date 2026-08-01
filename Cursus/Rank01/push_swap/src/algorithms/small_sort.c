/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   small_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:06:05 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:06:06 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Builds the initial BFS state from stack a.
 *
 * Reads a's values (already ranked 0..size-1 by assign_ranks) into a
 * fresh abstract state with an empty b, ready to hand to bfs_solve.
 *
 * @param a Stack already ranked via assign_ranks.
 * @param size Number of elements in a.
 * @return The starting t_state for the BFS search.
 */
static t_state	build_start_state(t_stack *a, int size)
{
	t_state	s;
	int		i;

	i = 0;
	while (i < size)
	{
		s.a[i] = a->index;
		a = a->next;
		i++;
	}
	s.a_len = size;
	s.b_len = 0;
	s.parent = -1;
	s.move = -1;
	return (s);
}

/**
 * @brief Sorts a small stack (size <= SMALL_N_MAX) with the fewest moves.
 *
 * Guarantees the shortest possible sequence of moves for any stack of
 * SMALL_N_MAX elements or fewer, by exhaustively searching every
 * reachable (a, b) arrangement (at most a few hundred for n <= 5).
 * Values only matter by relative order here, so they are mapped to
 * ranks 0..size-1 first, exactly like complex_sort/medium_sort do.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param bench Optional operation counters, or NULL if unused.
 * @return void
 */
void	ft_optimal_sort(t_stack **a, t_stack **b, t_bench *bench)
{
	t_state		states[MAX_SMALL_STATES];
	t_state		start;
	t_stacks	st;
	int			goal;

	if (ft_stack_size(*a) <= 1)
		return ;
	assign_ranks(*a);
	start = build_start_state(*a, ft_stack_size(*a));
	goal = bfs_solve(states, &start, ft_stack_size(*a));
	st.a = a;
	st.b = b;
	st.bench = bench;
	if (goal >= 0)
		apply_solution(states, goal, &st);
}
