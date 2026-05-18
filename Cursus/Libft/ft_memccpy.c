/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:26:32 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 15:06:43 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	*ft_memccpy(void *dest, const void *src, int c, unsigned int n)
{
	unsigned int		i;
	unsigned char		*d;
	const unsigned char	*s;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	i = 0;
	while (i < n)
	{
		d[i] = s[i];
		if (s[i] == (unsigned char)c)
			return ((void *)&d[i + 1]);
		i++;
	}
	return (0);
}

// int	main(void)
// {
// 	printf("ft_memccpy: prueba rápida\n");
// 	return (0);
// }
}
