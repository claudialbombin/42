/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:11:14 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:11:15 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Compares two null-terminated strings lexicographically.
 *
 * @param s1 First string to compare.
 * @param s2 Second string to compare.
 * @return 0 if equal; otherwise the difference between the first
 *         differing unsigned characters.
 */
int	ft_strcmp(const char *s1, const char *s2)
{
	int	i;

	i = 0;
	while (s1[i] && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

/**
 * @brief Allocates and returns a copy of a string.
 *
 * @param s String to duplicate.
 * @return Newly allocated copy of s, or NULL if allocation failed.
 */
char	*ft_strdup(const char *s)
{
	int		i;
	char	*result;

	i = 0;
	while (s[i])
		i++;
	result = malloc(sizeof(char) * (i + 1));
	if (!result)
		return (NULL);
	i = 0;
	while (s[i])
	{
		result[i] = s[i];
		i++;
	}
	result[i] = '\0';
	return (result);
}

/**
 * @brief Copies a string into a buffer, truncating to its size.
 *
 * @param dst Destination buffer.
 * @param src Source string to copy.
 * @param dstsize Total size of dst, including room for the null byte.
 * @return The length of src, so truncation can be detected by the
 *         caller.
 */
size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	len_src;
	size_t	i;

	len_src = ft_strlen(src);
	if (dstsize == 0)
		return (len_src);
	i = 0;
	while (src[i] && i < dstsize - 1)
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (len_src);
}

/**
 * @brief Allocates zero-initialized memory for an array.
 *
 * @param count Number of elements to allocate.
 * @param size Size in bytes of each element.
 * @return Pointer to the zeroed memory, or NULL on overflow or
 *         allocation failure.
 */
void	*ft_calloc(size_t count, size_t size)
{
	size_t			total_bytes;
	unsigned char	*temp;

	if (size != 0 && count > SIZE_MAX / size)
		return (NULL);
	total_bytes = count * size;
	temp = malloc(total_bytes);
	if (!temp)
		return (NULL);
	ft_memset(temp, 0, total_bytes);
	return (temp);
}

/**
 * @brief Fills a block of memory with a constant byte value.
 *
 * @param s Memory block to fill.
 * @param c Byte value to write, converted to unsigned char.
 * @param n Number of bytes to write.
 * @return s, unchanged.
 */
void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*p;

	p = (unsigned char *)s;
	while (n > 0)
	{
		*p = (unsigned char)c;
		p++;
		n--;
	}
	return (s);
}
