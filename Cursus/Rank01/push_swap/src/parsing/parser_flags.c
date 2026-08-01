/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser_flags.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:03 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:04 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Checks whether a flag was already set previously.
 *
 * @param flag Flag string being checked (eg. "--simple", "--bench").
 * @param strategy Strategy already selected so far, or NONE.
 * @param bench 1 if --bench was already seen, 0 otherwise.
 * @return 1 if flag duplicates an already-set strategy or --bench,
 *         0 otherwise.
 */
int	flag_duplicates(char *flag, int strategy, int bench)
{
	if (ft_strcmp(flag, "--simple") == 0
		|| ft_strcmp(flag, "--medium") == 0
		|| ft_strcmp(flag, "--complex") == 0
		|| ft_strcmp(flag, "--adaptive") == 0)
	{
		if (strategy != NONE)
			return (1);
	}
	else if (ft_strcmp(flag, "--bench") == 0)
	{
		if (bench == 1)
			return (1);
	}
	return (0);
}

/**
 * @brief Matches a flag string to a strategy and stores it.
 *
 * @param flag Flag string being checked.
 * @param strategy Pointer updated with the matching strategy value.
 * @return 1 if flag matched a strategy flag, 0 otherwise.
 */
int	set_strategy(char *flag, int *strategy)
{
	if (ft_strcmp(flag, "--simple") == 0)
		*strategy = SIMPLE;
	else if (ft_strcmp(flag, "--medium") == 0)
		*strategy = MEDIUM;
	else if (ft_strcmp(flag, "--complex") == 0)
		*strategy = COMPLEX;
	else if (ft_strcmp(flag, "--adaptive") == 0)
		*strategy = ADAPTIVE;
	else
		return (0);
	return (1);
}

/**
 * @brief Parses every leading "--flag" argument.
 *
 * Stops at the first argument that isn't a recognised flag, which is
 * assumed to be the start of the numbers to sort.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector.
 * @param strategy Pointer updated with the requested strategy.
 * @param bench Pointer updated to 1 if --bench was passed.
 * @return Index of the first non-flag argument, or -1 on an unknown
 *         or duplicate flag.
 */
int	parse_flags(int argc, char **argv, int *strategy, int *bench)
{
	int	i;

	i = 1;
	while (i < argc && argv[i] != NULL
		&& argv[i][0] == '-' && argv[i][1] == '-')
	{
		if (flag_duplicates(argv[i], *strategy, *bench))
			return (-1);
		if (!set_strategy(argv[i], strategy))
		{
			if (ft_strcmp(argv[i], "--bench") == 0)
				*bench = 1;
			else
				return (-1);
		}
		i++;
	}
	return (i);
}
