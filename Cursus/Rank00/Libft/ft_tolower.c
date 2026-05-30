/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:21:13 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 14:58:09 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_tolower(int c)
{
	if ((c >= 'A') && (c <= 'Z'))
		return (c + 32);
	return (c);
}

// int	main(void)
// {
// 	printf("ft_tolower: prueba rápida\n");
// 	return (0);
// }
