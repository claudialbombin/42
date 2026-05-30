/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#             */
/*   Updated: 2026/05/18 17:09:47 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_is_in_set(char c, const char *set)
{
	while (*set)
	{
		if (*set == c)
			return (1);
		set++;
	}
	return (0);
}

static char	*ft_copy_range(const char *s, unsigned int start, unsigned int end)
{
	char			*res;
	unsigned int	i;

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

char	*ft_strtrim(char const *s, char const *set)
{
	char			*result;
	unsigned int	start;
	unsigned int	end;

	if (!s || !set)
		return (NULL);
	start = 0;
	end = 0;
	while (s[end] != '\0')
		end++;
	while (s[start] && ft_is_in_set(s[start], set))
		start++;
	while (end > start && ft_is_in_set(s[end - 1], set))
		end--;
	result = ft_copy_range(s, start, end);
	return (result);
}

// int	main(void)
// {
// 	printf("ft_strtrim: prueba rápida\n");
// 	return (0);
// }
