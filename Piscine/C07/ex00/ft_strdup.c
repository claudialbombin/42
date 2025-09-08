/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 11:46:41 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/25 11:35:49 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strdup(char *s1)
{
	char	*copy;
	int		i;

	if (!s1)
		return (0);
	i = 0;
	while (s1[i])
		i++;
	copy = (char *)malloc((i + 1) * sizeof(char));
	if (!copy)
		return (NULL);
	i = 0;
	while (s1[i])
	{
		copy[i] = s1[i];
		i++;
	}
	copy[i] = '\0';
	return (copy);
}
int main(void)
{
    char *str = "Hello, World!";
    char *dup = ft_strdup(str);
    if (dup)
    {
        // Print the duplicated string
        int i = 0;
        while (dup[i])
        {
            write(1, &dup[i], 1);
            i++;
        }
        free(dup); // Free the allocated memory
    }
    else
    {
        write(1, "Memory allocation failed\n", 25);
    }
    return (0);
}