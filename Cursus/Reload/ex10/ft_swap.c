/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/18 19:06:31 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 19:17:49 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

/*
#include <stdio.h>

int main(void)
{
    int x = 5;
    int y = 10;
    
    printf("Antes: x = %d, y = %d\n", x, y);
    ft_swap(&x, &y);
    printf("Después: x = %d, y = %d\n", x, y);
    return (0);
}
*/