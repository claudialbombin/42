/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 00:00:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	putnbr_recursive(unsigned long n)
{
	int	count;

	count = 0;
	if (n >= 10)
		count += putnbr_recursive(n / 10);
	count += ft_putchar_count((n % 10) + '0');
	return (count);
}

int	ft_putnbr_count(int n)
{
	int				count;
	unsigned long	nb;

	count = 0;
	if (n < 0)
	{
		count += ft_putchar_count('-');
		nb = (unsigned long)(-(long)n);
	}
	else
		nb = (unsigned long)n;
	count += putnbr_recursive(nb);
	return (count);
}
