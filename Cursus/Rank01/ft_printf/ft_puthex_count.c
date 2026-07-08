/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/08 16:01:06 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static char	hex_char(unsigned long digit, int is_upper)
{
	if (is_upper)
		return ("0123456789ABCDEF"[digit]);
	return ("0123456789abcdef"[digit]);
}

int	ft_puthex_count(unsigned long n, int is_upper)
{
	int	count;
	int	ret;

	count = 0;
	if (n >= 16)
	{
		ret = ft_puthex_count(n / 16, is_upper);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	ret = ft_putchar_count(hex_char(n % 16, is_upper));
	if (ret == -1)
		return (-1);
	return (count + ret);
}
