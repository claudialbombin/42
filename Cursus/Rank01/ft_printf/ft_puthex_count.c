/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 00:00:00 by clopez-b         ###   ########.fr       */
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

	count = 0;
	if (n >= 16)
		count += ft_puthex_count(n / 16, is_upper);
	count += ft_putchar_count(hex_char(n % 16, is_upper));
	return (count);
}
