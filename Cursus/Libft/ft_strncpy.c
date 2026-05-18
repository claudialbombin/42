/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 13:14:23 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 14:49:19 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncpy(char *dest, const char *src, int len)
{
	int	i;

	i = 0;
	while ((src[i]) && (i < len))
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}


// #include <stdio.h>

// int	main(void)
// {
// 	char dest[20];
// 	const char *src = "hola mundo";

// 	ft_strncpy(dest, src, 5);
// 	printf("dest (len 5): '%s'\n", dest); // espera: 'hola'

// 	ft_strncpy(dest, src, 12);
// 	printf("dest (len 12): '%s'\n", dest); // espera: 'hola mundo'

// 	return (0);
// }
