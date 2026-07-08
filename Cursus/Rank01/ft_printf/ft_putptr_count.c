/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putptr_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/08 16:00:18 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putptr_count(unsigned long n)
{
	int	count;
	int	ret;

	if (n == 0)
		return (ft_putstr_count("0x0"));
	count = ft_putstr_count("0x");
	if (count == -1)
		return (-1);
	ret = ft_puthex_count(n, 0);
	if (ret == -1)
		return (-1);
	return (count + ret);
}
