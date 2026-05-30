/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsplit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#             */
/*   Updated: 2026/05/18 15:15:23 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

static int	ft_count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			in_word = 1;
			count++;
		}
		else if (*s == c)
			in_word = 0;
		s++;
	}
	return (count);
}

static char	*ft_get_word(char const *s, char c, int *pos)
{
	char	*word;
	int		start;
	int		len;

	while (s[*pos] == c)
		(*pos)++;
	start = *pos;
	len = 0;
	while (s[*pos] && s[*pos] != c)
	{
		len++;
		(*pos)++;
	}
	word = (char *)malloc((len + 1) * sizeof(char));
	if (!word)
		return (NULL);
	len = 0;
	while (s[start + len] && s[start + len] != c)
	{
		word[len] = s[start + len];
		len++;
	}
	word[len] = '\0';
	return (word);
}

static void	ft_free_arr(char **arr, int n)
{
	while (n > 0)
		free(arr[--n]);
	free(arr);
}

char	**ft_strsplit(char const *s, char c)
{
	char	**arr;
	int		words;
	int		pos;
	int		i;

	if (!s)
		return (NULL);
	words = ft_count_words(s, c);
	arr = (char **)malloc((words + 1) * sizeof(char *));
	if (!arr)
		return (NULL);
	pos = 0;
	i = 0;
	while (i < words)
	{
		arr[i] = ft_get_word(s, c, &pos);
		if (!arr[i])
		{
			ft_free_arr(arr, i);
			return (NULL);
		}
		i++;
	}
	arr[i] = NULL;
	return (arr);
}

// int	main(void)
// {
// 	printf("ft_strsplit: prueba rápida\n");
// 	return (0);
// }
