/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/08 16:05:44 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	handle_unknown(char c)
{
	int	ret;
	int	ret2;

	ret = ft_putchar_count('%');
	if (ret == -1)
		return (-1);
	ret2 = ft_putchar_count(c);
	if (ret2 == -1)
		return (-1);
	return (ret + ret2);
}

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
	return (handle_unknown(c));
}
	// if (c == 'a')
	// 	return (ft_putstr_count("amazing "));

static int	print_next(const char *format, int *i, va_list args)
{
	int	ret;

	if (format[*i] == '%' && format[*i + 1])
	{
		ret = handle_format(format[*i + 1], args);
		*i += 2;
	}
	else
	{
		ret = ft_putchar_count(format[*i]);
		*i += 1;
	}
	return (ret);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;
	int		i;
	int		ret;

	if (!format)
		return (-1);
	va_start(args, format);
	count = 0;
	i = 0;
	while (format[i])
	{
		ret = print_next(format, &i, args);
		if (ret == -1)
		{
			va_end(args);
			return (-1);
		}
		count += ret;
	}
	va_end(args);
	return (count);
}
