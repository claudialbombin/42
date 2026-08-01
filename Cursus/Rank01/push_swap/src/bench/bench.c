/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:06:46 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:06:47 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Sums every operation counter into a single total.
 *
 * @param bench Bench counters to sum.
 * @return Total number of operations performed.
 */
static int	total_ops(t_bench *bench)
{
	return (bench->sa + bench->sb + bench->ss + bench->pa + bench->pb
		+ bench->ra + bench->rb + bench->rr + bench->rra + bench->rrb
		+ bench->rrr);
}

/**
 * @brief Prints the sa/sb/ss/pa/pb bench counters line to stderr.
 *
 * @param bench Bench counters to print.
 * @return void
 */
static void	print_line_swap_push(t_bench *bench)
{
	ft_put_str_fd("[bench] sa: ", 2);
	ft_put_nbr_fd(bench->sa, 2);
	ft_put_str_fd(" sb: ", 2);
	ft_put_nbr_fd(bench->sb, 2);
	ft_put_str_fd(" ss: ", 2);
	ft_put_nbr_fd(bench->ss, 2);
	ft_put_str_fd(" pa: ", 2);
	ft_put_nbr_fd(bench->pa, 2);
	ft_put_str_fd(" pb: ", 2);
	ft_put_nbr_fd(bench->pb, 2);
	ft_put_str_fd("\n", 2);
}

/**
 * @brief Prints the ra/rb/rr/rra/rrb/rrr bench counters line to stderr.
 *
 * @param bench Bench counters to print.
 * @return void
 */
static void	print_line_rotate(t_bench *bench)
{
	ft_put_str_fd("[bench] ra: ", 2);
	ft_put_nbr_fd(bench->ra, 2);
	ft_put_str_fd(" rb: ", 2);
	ft_put_nbr_fd(bench->rb, 2);
	ft_put_str_fd(" rr: ", 2);
	ft_put_nbr_fd(bench->rr, 2);
	ft_put_str_fd(" rra: ", 2);
	ft_put_nbr_fd(bench->rra, 2);
	ft_put_str_fd(" rrb: ", 2);
	ft_put_nbr_fd(bench->rrb, 2);
	ft_put_str_fd(" rrr: ", 2);
	ft_put_nbr_fd(bench->rrr, 2);
	ft_put_str_fd("\n", 2);
}

/**
 * @brief Prints the full --bench report to stderr.
 *
 * Matches the subject's example format. "strategy" comes in already
 * built as one string (eg. "Adaptive / O(n^2)") because the exact
 * label depends on which internal method got picked, and that
 * decision is made in main.c, not here.
 *
 * @param disorder Disorder index computed before sorting.
 * @param strategy Human-readable strategy label already built by
 *                  the caller.
 * @param bench Bench counters to print.
 * @return void
 */
void	ft_print_bench(double disorder, char *strategy, t_bench *bench)
{
	ft_put_str_fd("[bench] disorder: ", 2);
	ft_put_percent_fd(disorder, 2);
	ft_put_str_fd("\n[bench] strategy: ", 2);
	ft_put_str_fd(strategy, 2);
	ft_put_str_fd("\n[bench] total_ops: ", 2);
	ft_put_nbr_fd(total_ops(bench), 2);
	ft_put_str_fd("\n", 2);
	print_line_swap_push(bench);
	print_line_rotate(bench);
}
