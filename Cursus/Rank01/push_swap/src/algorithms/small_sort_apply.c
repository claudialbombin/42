/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   small_sort_apply.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:29 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:30 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Applies the ss move (sa + sb) to an abstract BFS state.
 *
 * @param s State whose a and b arrays are swapped in place.
 * @return void
 */
static void	apply_ss(t_state *s)
{
	arr_swap(s->a, s->a_len);
	arr_swap(s->b, s->b_len);
}

/**
 * @brief Applies the rr move (ra + rb) to an abstract BFS state.
 *
 * @param s State whose a and b arrays are rotated in place.
 * @return void
 */
static void	apply_rr(t_state *s)
{
	arr_rotate(s->a, s->a_len);
	arr_rotate(s->b, s->b_len);
}

/**
 * @brief Applies the rrr move (rra + rrb) to an abstract BFS state.
 *
 * @param s State whose a and b arrays are reverse-rotated in place.
 * @return void
 */
static void	apply_rrr(t_state *s)
{
	arr_reverse_rotate(s->a, s->a_len);
	arr_reverse_rotate(s->b, s->b_len);
}

/**
 * @brief Applies one abstract push_swap move to a BFS state.
 *
 * move_id follows the same order as the subject's operation list:
 * 0 sa, 1 sb, 2 ss, 3 pa, 4 pb, 5 ra, 6 rb, 7 rr, 8 rra, 9 rrb, 10 rrr.
 *
 * @param move_id Identifier of the move to apply, 0 to 10.
 * @param s State to update in place.
 * @return void
 */
void	apply_move(int move_id, t_state *s)
{
	if (move_id == 0)
		arr_swap(s->a, s->a_len);
	else if (move_id == 1)
		arr_swap(s->b, s->b_len);
	else if (move_id == 2)
		apply_ss(s);
	else if (move_id == 3)
		arr_push(s->a, &s->a_len, s->b, &s->b_len);
	else if (move_id == 4)
		arr_push(s->b, &s->b_len, s->a, &s->a_len);
	else if (move_id == 5)
		arr_rotate(s->a, s->a_len);
	else if (move_id == 6)
		arr_rotate(s->b, s->b_len);
	else if (move_id == 7)
		apply_rr(s);
	else if (move_id == 8)
		arr_reverse_rotate(s->a, s->a_len);
	else if (move_id == 9)
		arr_reverse_rotate(s->b, s->b_len);
	else
		apply_rrr(s);
}
