/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/18 19:03:39 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 19:05:01 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_is_negative(int n)
{
	if (n < 0)
		ft_putchar('N');
	else
		ft_putchar('P');
}

/*
int main(void)
{
    ft_is_negative(-5);
    ft_putchar('\n');
    ft_is_negative(0);
    ft_putchar('\n');
    ft_is_negative(42);
    ft_putchar('\n');
    return (0);
}
*/