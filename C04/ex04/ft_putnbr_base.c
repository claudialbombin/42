/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 13:20:14 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/20 13:20:29 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putnbr_base(int nbr, char *base)
{
	char	digit;
	int		base_len;

	base_len = 0;
	while (base[base_len])
	{
		base_len++;
	}
	if (nbr < 0)
	{
		write(1, "-", 1);
		nbr = -nbr;
	}
	if (nbr >= base_len)
		ft_putnbr_base(nbr / base_len, base);
	digit = base[nbr % base_len];
	write(1, &digit, 1);
}
