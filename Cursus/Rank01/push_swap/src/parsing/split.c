/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:09 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:10 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Measures the length of a word up to a separator.
 *
 * @param str String to scan, starting at the first character of a word.
 * @param c Separator character that ends the word.
 * @return Number of characters before the next occurrence of c, or
 *         before the terminating null byte.
 */
static int	ft_word_len(char const *str, char c)
{
	int	i;

	i = 0;
	while (str[i] && str[i] != c)
		i++;
	return (i);
}

/**
 * @brief Counts the words in a string, separated by a character.
 *
 * @param s String to scan.
 * @param c Separator character between words.
 * @return Number of words found in s.
 */
static int	ft_count_words(char const *s, char c)
{
	int	count;
	int	i;

	i = 0;
	count = 0;
	while (s[i])
	{
		while (s[i] && s[i] == c)
			i++;
		if (s[i])
		{
			count++;
			i += ft_word_len(s + i, c);
		}
	}
	return (count);
}

/**
 * @brief Frees a partially filled array of strings and the array itself.
 *
 * @param tab Array of allocated strings to free.
 * @param i Number of valid entries in tab (from index 0).
 * @return NULL, so callers can return its result directly.
 */
static void	*free_all(char **tab, int i)
{
	while (i--)
	{
		if (tab[i])
			free(tab[i]);
	}
	free(tab);
	return (NULL);
}

/**
 * @brief Fills a pre-allocated array with the words of a string.
 *
 * @param str Array to fill; must be large enough for every word plus
 *            a terminating NULL.
 * @param s String to split.
 * @param c Separator character between words.
 * @return 1 on success; 0 if an allocation failed (str is freed via
 *         free_all in that case).
 */
static int	ft_fill_str(char **str, char const *s, char c)
{
	int	i;
	int	subs_len;

	i = 0;
	while (*s)
	{
		while (*s && *s == c)
			++s;
		if (*s)
		{
			subs_len = ft_word_len(s, c);
			str[i] = ft_calloc(subs_len + 1, sizeof(char));
			if (!str[i])
				return (free_all(str, i), 0);
			ft_strlcpy(str[i], s, subs_len + 1);
			s += subs_len;
			i++;
		}
	}
	str[i] = NULL;
	return (1);
}

/**
 * @brief Splits a string into an array of words on a separator.
 *
 * @param s String to split.
 * @param c Separator character between words.
 * @return Newly allocated, NULL-terminated array of newly allocated
 *         words, or NULL on failure (invalid input or allocation
 *         failure).
 */
char	**ft_split(char const *s, char c)
{
	char	**str;

	if (!s)
		return (NULL);
	str = ft_calloc((ft_count_words(s, c) + 1), sizeof(char *));
	if (!str)
		return (NULL);
	if (!ft_fill_str(str, s, c))
		return (NULL);
	return (str);
}
