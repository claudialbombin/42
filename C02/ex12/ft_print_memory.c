/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_memory.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 11:25:43 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/20 12:03:27 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	imprimir_char(char c)
{
	write(1, &c, 1);
}

void	imprimir_direccion(unsigned long num)
{
	char	*hex;
	char	dir[16];
	int		i;

	hex = "0123456789abcdef";
	i = 15;
	while (i >= 0)
	{
		dir[i] = hex[num % 16];
		num /= 16;
		i--;
	}
	write(1, dir, 16);
}

void	imprimir_hex(unsigned char *bloque, int size)
{
	char	*hex;
	int		i;

	hex = "0123456789abcdef";
	i = 0;
	while (i < 16)
	{
		if (i < size)
		{
			imprimir_char(hex[bloque[i] / 16]);
			imprimir_char(hex[bloque[i] % 16]);
		}
		else
			write(1, "  ", 2);
		if (i % 2 == 1)
			imprimir_char(' ');
		i++;
	}
}

void	imprimir_ascii(unsigned char *bloque, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (bloque[i] >= 32 && bloque[i] <= 126)
			imprimir_char(bloque[i]);
		else
			imprimir_char('.');
		i++;
	}
}

void	*ft_print_memory(void *dir, unsigned int size)
{
	unsigned int	i;
	unsigned char	*p;

	i = 0;
	p = (unsigned char *)dir;
	if (size == 0)
		return (dir);
	while (i < size)
	{
		imprimir_direccion((unsigned long)(p + i));
		write(1, ": ", 2);
		if (size - i >= 16)
			imprimir_hex(p + i, 16);
		else
			imprimir_hex(p + i, size - i);
		if (size - i >= 16)
			imprimir_ascii(p + i, 16);
		else
			imprimir_ascii(p + i, size - i);
		write(1, "\n", 1);
		i += 16;
	}
	return (dir);
}
