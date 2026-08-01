/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:03:36 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:03:45 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Builds the "[bench] strategy: ..." label for the report.
 *
 * For forced flags the label is fixed, but for --adaptive it repeats
 * the same disorder thresholds used inside ft_adaptive_sort, since
 * that function only sorts, it doesn't report which internal method
 * it picked. Stacks of SMALL_N_MAX elements or fewer always go
 * through ft_optimal_sort instead (see execute_strategy), so their
 * label overrides everything else, chosen strategy included.
 *
 * @param strategy Strategy requested on the command line.
 * @param disorder Disorder index computed before sorting.
 * @param size Number of elements in the stack.
 * @return Static string with the human-readable strategy label.
 */
static char	*strategy_label(t_strategy strategy, double disorder, int size)
{
	if (size <= SMALL_N_MAX)
		return ("Optimal (exhaustive search)");
	if (strategy == STRAT_SIMPLE)
		return ("Simple / O(n^2)");
	if (strategy == STRAT_MEDIUM)
		return ("Medium / O(n * sqrt(n))");
	if (strategy == STRAT_COMPLEX)
		return ("Complex / O(n log n)");
	if (disorder < 0.2)
		return ("Adaptive / O(n)");
	if (disorder < 0.5)
		return ("Adaptive / O(n * sqrt(n))");
	return ("Adaptive / O(n log n)");
}

/**
 * @brief Runs whichever sorting strategy the user picked.
 *
 * Falls back to the adaptive strategy by default. bench always
 * points at a valid, zero-initialized struct - the counters just go
 * unused (and unprinted) when --bench wasn't passed.
 *
 * Stacks of SMALL_N_MAX elements or fewer always go through the
 * exhaustive-search optimal sort instead, regardless of the chosen
 * strategy: at that size the state space is tiny enough to search in
 * full, so there's no reason to settle for any strategy's
 * general-purpose (and here, non-optimal) behaviour.
 *
 * @param a Pointer to the main stack to sort.
 * @param b Pointer to the auxiliary (initially empty) stack.
 * @param strategy Strategy requested on the command line.
 * @param bench Bench counters, updated as moves are performed.
 * @return void
 */
static void	execute_strategy(t_stack **a, t_stack **b, t_strategy strategy,
		t_bench *bench)
{
	if (ft_stack_size(*a) <= SMALL_N_MAX)
		ft_optimal_sort(a, b, bench);
	else if (strategy == STRAT_SIMPLE)
		ft_simple_sort(a, b, bench);
	else if (strategy == STRAT_MEDIUM)
		ft_medium_sort(a, b, bench);
	else if (strategy == STRAT_COMPLEX)
		ft_complex_sort(a, b, bench);
	else
		ft_adaptive_sort(a, b, bench);
}

/**
 * @brief Entry point: parses arguments, sorts, and prints the moves.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector: flags followed by numbers to sort.
 * @return 0 on success (including the no-argument case); the program
 *         exits with status 1 via exit_error on any parsing failure.
 */
int	main(int argc, char **argv)
{
	t_stack		*a;
	t_stack		*b;
	t_bench		bench;
	t_strategy	strategy;
	double		disorder;

	if (argc <= 1)
		return (0);
	a = ft_build_stack(argc, argv);
	b = NULL;
	strategy = ft_parse_strategy(argc, argv);
	disorder = compute_disorder(a);
	ft_bench_init(&bench);
	execute_strategy(&a, &b, strategy, &bench);
	if (ft_has_bench_flag(argc, argv))
		ft_print_bench(disorder,
			strategy_label(strategy, disorder, ft_stack_size(a)), &bench);
	ft_free_stack(&a);
	ft_free_stack(&b);
	return (0);
}
