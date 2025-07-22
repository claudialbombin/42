/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 10:53:16 by clopez-b          #+#    #+#             */
/*   Updated: 2025/07/14 11:15:59 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	auxresd;
	int	auxrest;

	auxresd = (*a / *b);
	auxrest = (*a % *b);
	*a = auxresd;
	*b = auxrest;
}
