/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:21:43 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 15:05:07 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_toupper(int c)
{
	if ((c >= 'a') && (c <= 'z'))
		return (c - 32);
	return (c);
}

// int	main(void)
// {
// 	printf("ft_toupper: prueba rápida\n");
// 	return (0);
// }
