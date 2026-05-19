/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/18 19:07:31 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 19:17:49 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}

/*
#include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 3;
    int division;
    int resto;
    
    ft_div_mod(a, b, &division, &resto);
    printf("%d / %d = %d, resto = %d\n", a, b, division, resto);
    return (0);
}
*/