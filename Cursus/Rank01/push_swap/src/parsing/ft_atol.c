/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atol.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:10:49 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:10:50 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Reads consecutive decimal digits and applies a sign.
 *
 * Clamps to LONG_MAX / LONG_MIN on overflow instead of wrapping.
 *
 * @param str String being parsed.
 * @param i Pointer to the current index into str, advanced past
 *          every digit consumed.
 * @param sign 1 for positive, -1 for negative.
 * @return The parsed value, signed and clamped to the long range.
 */
static long	read_digits(const char *str, int *i, int sign)
{
	long	result;
	int		digit;

	result = 0;
	while (str[*i] >= '0' && str[*i] <= '9')
	{
		digit = str[*i] - '0';
		if (result > (LONG_MAX - digit) / 10)
		{
			if (sign == 1)
				return (LONG_MAX);
			return (LONG_MIN);
		}
		result = result * 10 + digit;
		(*i)++;
	}
	return (result * sign);
}

/**
 * @brief Converts a string to a long, skipping leading whitespace.
 *
 * @param str Null-terminated string to convert.
 * @return The parsed long value, clamped to LONG_MAX / LONG_MIN on
 *         overflow.
 */
long	ft_atol(const char *str)
{
	int	i;
	int	sign;

	i = 0;
	sign = 1;
	while (str[i] == ' ' || (str[i] >= '\t' && str[i] <= '\r'))
		i++;
	if (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	return (read_digits(str, &i, sign));
}
