/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_parser_num.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:11 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:12 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Counts how many space-separated numbers are in the arguments.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector.
 * @param first_number Index of the first argument holding numbers.
 * @return Total number of numbers found, or 0 if a split failed.
 */
int	count_numbers(int argc, char **argv, int first_number)
{
	char	**numbers;
	int		total;
	int		i;
	int		j;

	total = 0;
	i = first_number;
	while (i < argc && argv[i] != NULL)
	{
		numbers = ft_split(argv[i], ' ');
		if (!numbers)
			return (0);
		j = 0;
		while (numbers[j] != NULL)
		{
			total++;
			j++;
		}
		free_split(numbers);
		i++;
	}
	return (total);
}

/**
 * @brief Flattens the number arguments into one NULL-terminated array.
 *
 * Splits every argument on spaces and copies the resulting words into
 * a single freshly allocated array, so callers don't need to care
 * whether numbers arrived as separate arguments or packed into one.
 *
 * @param argc Argument count, including the program name.
 * @param argv Argument vector.
 * @param first_number Index of the first argument holding numbers.
 * @return Newly allocated, NULL-terminated array of number strings,
 *         or NULL on allocation or split failure.
 */
char	**normalize_args(int argc, char **argv, int first_number)
{
	int		total_numbers;
	int		i;
	int		index;
	char	**new_array;
	char	**split_tmp;

	total_numbers = count_numbers(argc, argv, first_number);
	new_array = malloc(sizeof(char *) * (total_numbers + 1));
	if (!new_array)
		return (NULL);
	i = first_number;
	index = 0;
	while (i < argc && argv[i] != NULL)
	{
		split_tmp = ft_split(argv[i], ' ');
		if (!split_tmp)
			return (NULL);
		copy_split(new_array, split_tmp, &index);
		free_split(split_tmp);
		i++;
	}
	new_array[index] = NULL;
	return (new_array);
}

/**
 * @brief Copies every string of a split array into a destination array.
 *
 * @param new_array Destination array, written starting at *index.
 * @param split_tmp NULL-terminated source array to copy from.
 * @param index Pointer to the current write position in new_array,
 *              advanced by the number of strings copied.
 * @return void
 */
void	copy_split(char **new_array, char **split_tmp, int *index)
{
	int	j;

	j = 0;
	while (split_tmp[j] != NULL)
	{
		new_array[*index] = ft_strdup(split_tmp[j]);
		(*index)++;
		j++;
	}
}

/**
 * @brief Frees every string of a NULL-terminated array and the array.
 *
 * @param split NULL-terminated array of strings to free, or NULL.
 * @return void
 */
void	free_split(char **split)
{
	int	i;

	i = 0;
	if (!split)
		return ;
	while (split[i] != NULL)
	{
		free(split[i]);
		i++;
	}
	free(split);
}
