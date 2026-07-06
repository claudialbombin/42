/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 00:00:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	handle_format(char c, va_list args)
{
	if (c == 'c')
		return (ft_putchar_count((char)va_arg(args, int)));
	if (c == 's')
		return (ft_putstr_count(va_arg(args, char *)));
	if (c == 'p')
		return (ft_putptr_count((unsigned long)va_arg(args, void *)));
	if (c == 'd' || c == 'i')
		return (ft_putnbr_count(va_arg(args, int)));
	if (c == 'u')
		return (ft_putunbr_count(va_arg(args, unsigned int)));
	if (c == 'x')
		return (ft_puthex_count(va_arg(args, unsigned int), 0));
	if (c == 'X')
		return (ft_puthex_count(va_arg(args, unsigned int), 1));
	if (c == '%')
		return (ft_putchar_count('%'));
	return (ft_putchar_count('%') + ft_putchar_count(c));
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;
	int		i;

	if (!format)
		return (-1);
	va_start(args, format);
	count = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
		{
			count += handle_format(format[i + 1], args);
			i += 2;
		}
		else
		{
			count += ft_putchar_count(format[i]);
			i++;
		}
	}
	va_end(args);
	return (count);
}
