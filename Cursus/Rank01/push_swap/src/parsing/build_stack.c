/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   build_stack.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:10:43 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:10:44 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Converts a raw strategy flag value into a t_strategy enum.
 *
 * @param strategy One of NONE, SIMPLE, MEDIUM, COMPLEX or ADAPTIVE.
 * @return The matching t_strategy value, or STRAT_NONE if unmatched.
 */
static t_strategy	int_to_strategy(int strategy)
{
	if (strategy == SIMPLE)
		return (STRAT_SIMPLE);
	if (strategy == MEDIUM)
		return (STRAT_MEDIUM);
	if (strategy == COMPLEX)
		return (STRAT_COMPLEX);
	if (strategy == ADAPTIVE)
		return (STRAT_ADAPTIVE);
	return (STRAT_NONE);
}

/**
 * @brief Parses the command-line flags and returns the chosen strategy.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector.
 * @return The requested t_strategy, or STRAT_NONE if flag parsing
 *         failed or no strategy flag was passed.
 */
t_strategy	ft_parse_strategy(int argc, char **argv)
{
	int	strategy;
	int	bench;

	strategy = NONE;
	bench = 0;
	if (parse_flags(argc, argv, &strategy, &bench) == -1)
		return (STRAT_NONE);
	return (int_to_strategy(strategy));
}

/**
 * @brief Checks whether --bench was passed on the command line.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector.
 * @return 1 if --bench was passed, 0 otherwise (including on any
 *         flag-parsing failure).
 */
int	ft_has_bench_flag(int argc, char **argv)
{
	int	strategy;
	int	bench;

	strategy = NONE;
	bench = 0;
	if (parse_flags(argc, argv, &strategy, &bench) == -1)
		return (0);
	return (bench);
}

/**
 * @brief Parses the command line and builds the initial stack.
 *
 * Parses flags, splits any space-separated numbers inside a single
 * argument, then builds the stack. Any parsing failure (bad flag, bad
 * number, out of range, duplicate) exits the whole program via
 * exit_error, matching the subject's "Error" requirement.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector: flags followed by numbers to sort.
 * @return The built stack, or NULL if no numbers were given.
 */
t_stack	*ft_build_stack(int argc, char **argv)
{
	int		strategy;
	int		bench;
	int		first_number;
	char	**numbers;
	t_stack	*a;

	strategy = NONE;
	bench = 0;
	first_number = parse_flags(argc, argv, &strategy, &bench);
	if (first_number == -1)
		exit_error(NULL, NULL);
	if (first_number >= argc)
		return (NULL);
	numbers = normalize_args(argc, argv, first_number);
	if (!numbers)
		exit_error(NULL, NULL);
	a = NULL;
	if (!parse_numbers(numbers, &a))
	{
		free_split(numbers);
		exit_error(a, NULL);
	}
	free_split(numbers);
	return (a);
}
