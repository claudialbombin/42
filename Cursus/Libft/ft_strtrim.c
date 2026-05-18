/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#             */
/*   Updated: 2026/05/18 15:08:41 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_isspace(char c)
{
	return (c == ' ' || c == '\n' || c == '\t');
}

static char	*ft_copy_range(const char *s, unsigned int start, unsigned int end)
{
	char            *res;
	unsigned int    i;

	res = (char *)malloc((end - start + 1) * sizeof(char));
	if (!res)
		return (NULL);
	i = 0;
	while (start < end)
	{
		res[i] = s[start];
		i++;
		start++;
	}
	res[i] = '\0';
	return (res);
}

char	*ft_strtrim(char const *s)
{
	char			*result;
	unsigned int	start;
	unsigned int	end;
	unsigned int	i;

	if (!s)
		return (NULL);
	start = 0;
	end = 0;
	while (s[end] != '\0')
		end++;
	while (s[start] && ft_isspace(s[start]))
		start++;
	while (end > start && ft_isspace(s[end - 1]))
		end--;
	result = ft_copy_range(s, start, end);
	return (result);
}

// int	main(void)
// {
// 	printf("ft_strtrim: prueba rápida\n");
// 	return (0);
// }
