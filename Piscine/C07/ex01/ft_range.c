/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 12:05:26 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/25 11:25:33 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*range;
	int	i;
	int	size;

	if (min >= max)
		return (NULL);
	size = max - min;
	range = (int *)malloc(size * sizeof(int));
	if (!range)
		return (NULL);
	i = 0;
	while (i < size)
	{
		range[i] = min + i;
		i++;
	}
	return (range);
}
/*int main(void)
{
    int *range;
    int i;
    int size;

    range = ft_range(5, 11);
    if (range)
    {
        size = 6; // 11 - 5
        for (i = 0; i < size; i++)
            printf("%d ", range[i]);
        free(range);
    }
    else
        printf("Range is NULL\n");
    return (0);
}*/