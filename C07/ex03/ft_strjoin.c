/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 13:00:12 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/25 11:25:00 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	len;
    
    len = 0;
	while (str[len])
		len++;
	return (len);
}

int	get_total_length(int size, char **strs, char *sep)
{
	int	i;
	int	len;

    i = 0;
    len = 0;
	while (i < size)
	{
		len += ft_strlen(strs[i]);
		if (i < size - 1)
			len += ft_strlen(sep);
		i++;
	}
	return (len);
}

void	fill_result(char *result, int size, char **strs, char *sep)
{
	int	i;
	int	pos;
    int j;

    i = 0;
    pos = 0;
	while (i < size)
	{
		j = 0;
		while (strs[i][j])
			result[pos++] = strs[i][j++];
		if (i < size - 1)
		{
			j = 0;
			while (sep[j])
				result[pos++] = sep[j++];
		}
		i++;
	}
	result[pos] = '\0';
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		total_length;
	char	*result;

	if (size <= 0)
	{
		result = (char *)malloc(1);
		if (result)
			result = NULL;
		return (result);
	}
	total_length = get_total_length(size, strs, sep);
	result = (char *)malloc(total_length + 1);
	if (!result)
		return (NULL);
	fill_result(result, size, strs, sep);
	return (result);
}
/*
#include <stdio.h>

int main(void)
{
    char *strs[] = {"Hello", "World", "42"};
    char *sep = ", cg ";
    char *result;

    result = ft_strjoin(3, strs, sep);
    if (result)
    {
        printf("%s\n", result);
        free(result);
    }
    else
    {
        printf("Memory allocation failed\n");
    }
    return 0;
}*/