/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   exec_instr_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pvivas-f <pvivas-f@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:10:04 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 15:18:18 by pvivas-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "checker_bonus.h"

/**
 * @brief Applies one of the first 6 instructions (sa/sb/ss/pa/pb/ra).
 *
 * Reuses the real ft_* stack ops with print off and no bench, exactly
 * as they're already meant to be called silently (see the algorithms,
 * which do the same during internal rotations).
 *
 * @param line Instruction line to match.
 * @param a Pointer to stack a.
 * @param b Pointer to stack b.
 * @return 1 if line matched and was applied, 0 otherwise.
 */
static int	checker_apply_first(char *line, t_stack **a, t_stack **b)
{
	if (ft_strcmp(line, "sa") == 0)
		ft_sa(a, 0, NULL);
	else if (ft_strcmp(line, "sb") == 0)
		ft_sb(b, 0, NULL);
	else if (ft_strcmp(line, "ss") == 0)
		ft_ss(a, b, 0, NULL);
	else if (ft_strcmp(line, "pa") == 0)
		ft_pa(a, b, 0, NULL);
	else if (ft_strcmp(line, "pb") == 0)
		ft_pb(a, b, 0, NULL);
	else if (ft_strcmp(line, "ra") == 0)
		ft_ra(a, 0, NULL);
	else
		return (0);
	return (1);
}

/**
 * @brief Applies one of the other 5 instructions (rb/rr/rra/rrb/rrr).
 *
 * Split out from checker_apply_first so neither function runs over
 * the norm's line limit.
 *
 * @param line Instruction line to match.
 * @param a Pointer to stack a.
 * @param b Pointer to stack b.
 * @return 1 if line matched and was applied, 0 otherwise.
 */
static int	checker_apply_second(char *line, t_stack **a, t_stack **b)
{
	if (ft_strcmp(line, "rb") == 0)
		ft_rb(b, 0, NULL);
	else if (ft_strcmp(line, "rr") == 0)
		ft_rr(a, b, 0, NULL);
	else if (ft_strcmp(line, "rra") == 0)
		ft_rra(a, 0, NULL);
	else if (ft_strcmp(line, "rrb") == 0)
		ft_rrb(b, 0, NULL);
	else if (ft_strcmp(line, "rrr") == 0)
		ft_rrr(a, b, 0, NULL);
	else
		return (0);
	return (1);
}

/**
 * @brief Applies one instruction line to the real stacks.
 *
 * @param line Instruction line to match (empty, unknown word, wrong
 *             case and trailing garbage are all treated as invalid).
 * @param a Pointer to stack a.
 * @param b Pointer to stack b.
 * @return 0 if line isn't one of the 11 valid instructions, so the
 *         caller can treat it as the subject's "instruction doesn't
 *         exist or is malformed" error case; 1 otherwise.
 */
int	checker_apply_line(char *line, t_stack **a, t_stack **b)
{
	if (checker_apply_first(line, a, b))
		return (1);
	return (checker_apply_second(line, a, b));
}
