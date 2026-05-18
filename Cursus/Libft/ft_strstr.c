/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 21:55:51 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 15:06:43 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(const char *str, const char *to_find)
{
	int	i;
	int	j;

	if (!*to_find)
		return ((char *)str);

// int	main(void)
// {
// 	printf("ft_strstr: prueba rápida\n");
// 	return (0);
// }
	i = 0;
	while (str[i])
	{
		j = 0;
		while (str[i + j] && to_find[j] && (str[i + j] == to_find[j]))
			j++;
		if (!to_find[j])
			return ((char *)&str[i]);
		i++;
	}
	return (0);
}
