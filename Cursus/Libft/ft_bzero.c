/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 10:23:53 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 14:53:24 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_bzero(void *s, size_t n)
{
	size_t		i;
	char		*ptr;

	ptr = (char *)s;
	i = 0;
	while (i < n)
	{
		ptr[i] = 0;
		i++;
	}
}


// int	main(void)
// {
// 	char buf[10];

// 	memset(buf, 'A', sizeof(buf));
// 	buf[8] = '\0';
// 	printf("antes: %s\n", buf); // espera: AAAAAAAA

// 	ft_bzero(buf, 5);
// 	// muestra bytes como enteros para ver ceros
// 	printf("despues: ");
// 	for (int i = 0; i < 9; i++)
// 		printf("%d ", (unsigned char)buf[i]);
// 	printf("\n"); // espera primeros 5 valores 0

// 	return (0);
// }

