/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 11:05:55 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/20 11:10:14 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr_non_printable(char *str)

{
	char	*hex;
	int		i;
	int		j;

	hex = "0123456789abcdef";
	i = 0;
	while (str[i])
	{
		if (str[i] < 32 || str[i] > 126)
		{
			write(1, "\\", 1);
			j = str[i];
			write(1, &hex[j / 16], 1);
			write(1, &hex[j % 16], 1);
		}
		else
		{
			write(1, &str[i], 1);
		}
		i++;
	}
}
