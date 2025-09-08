/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/19 17:31:57 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/19 17:40:11 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(char *str, char *to_find)
{
	char	*h;
	char	*n;

	if (!*to_find)
		return (str);
	while (*str)
	{
		h = str;
		n = to_find;
		while (*h && *n && (*h == *n))
		{
			h++;
			n++;
		}
		if (!*n)
			return (str);
		str++;
	}
	return (0);
}
