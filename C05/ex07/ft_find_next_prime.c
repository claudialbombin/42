/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 10:13:49 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/21 10:16:58 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_find_next_prime(int nb)
{
	int	is_prime;
	int	i;

	if (nb < 2)
		return (2);
	while (1)
	{
		is_prime = 1;
		i = 2;
		while (i * i <= nb)
		{
			if (nb % i == 0)
			{
				is_prime = 0;
				break ;
			}
			i++;
		}
		if (is_prime)
			return (nb);
		nb++;
	}
}
