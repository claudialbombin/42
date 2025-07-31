/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/31 14:57:35 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/31 16:13:15 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	is_separator(char c, char *charset)
{
	while (*charset)
	{
		if (c == *charset)
			return (1);
		charset++;
	}
	return (0);
}

int	count_words(char *str, char *charset)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*str)
	{
		if (is_separator(*str, charset))
			in_word = 0;
		else if (!in_word)
		{
			in_word = 1;
			count++;
		}
		str++;
	}
	return (count);
}

char	*get_next_word(char **str, char *charset)
{
	char	*start;
	char	*word;
	int		len;
	int		i;

	len = 0;
	while (**str && is_separator(**str, charset))
		(*str)++;
	start = *str;
	while (**str && !is_separator(**str, charset))
	{
		(*str)++;
		len++;
	}
	word = (char *)malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = start[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

char	**ft_split(char *str, char *charset)
{
	char	**result;
	int		word_count;
	int		i;

	if (!str)
		return (NULL);
	word_count = count_words(str, charset);
	result = (char **)malloc(sizeof(char *) * (word_count + 1));
	if (!result)
		return (NULL);
	i = 0;
	while (i < word_count)
	{
		result[i] = get_next_word(&str, charset);
		if (!result[i])
			return (NULL);
		i++;
	}
	result[i] = 0;
	return (result);
}
/*
int ft_strlen(char *str)
{
    int len = 0;
    
    while (str[len])
        len++;
    return (len);
}

int main(int argc, char **argv)
{
	if (argc == 3)
	{
		char	**result;
		int		i;
		
		i = 0;
		**result = ft_split(argv[1], argv[2]);
		for (int i; result[i]; i++)
		{
			write(1, result[i], ft_strlen(result[i]));
			write(1, "\n", 1);
			free(result[i]);
		}
		free(result);
	}
	return (0);
}*/