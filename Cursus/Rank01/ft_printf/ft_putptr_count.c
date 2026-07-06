/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putptr_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 00:00:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putptr_count(unsigned long n)
{
	int	count;

	if (n == 0)
		return (ft_putstr_count("(nil)"));
	count = ft_putstr_count("0x");
	count += ft_puthex_count(n, 0);
	return (count);
}
