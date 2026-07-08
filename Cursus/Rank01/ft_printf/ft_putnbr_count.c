/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/08 16:00:37 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	putnbr_recursive(unsigned long n)
{
	int	count;
	int	ret;

	count = 0;
	if (n >= 10)
	{
		ret = putnbr_recursive(n / 10);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	ret = ft_putchar_count((n % 10) + '0');
	if (ret == -1)
		return (-1);
	return (count + ret);
}

int	ft_putnbr_count(int n)
{
	int				count;
	int				ret;
	unsigned long	nb;

	count = 0;
	if (n < 0)
	{
		ret = ft_putchar_count('-');
		if (ret == -1)
			return (-1);
		count += ret;
		nb = (unsigned long)(-(long)n);
	}
	else
		nb = (unsigned long)n;
	ret = putnbr_recursive(nb);
	if (ret == -1)
		return (-1);
	return (count + ret);
}
