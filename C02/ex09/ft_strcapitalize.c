/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/15 18:51:54 by clopez-b          #+#    #+#             */
/*   Updated: 2025/07/22 13:46:41 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_str_is_lowercase(char str)
{
	if (!(str >= 'a' && str <= 'z'))
		return (0);
	return (1);
}

int	ft_str_is_numeric(char str)
{
	if (!(str >= '0' && str <= '9'))
		return (0);
	return (1);
}

int	ft_str_is_alpha(char str)
{
	if (!((str >= 'a' && str <= 'z')
			|| (str >= 'A' && str <= 'Z')))
		return (0);
	return (1);
}

int	ft_str_is_uppercase(char str)
{
	if (!(str >= 'A' && str <= 'Z'))
		return (0);
	return (1);
}

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (ft_str_is_uppercase(str[i]))
			str[i] += 32;
		i++;
	}
	i = 0;
	while (str[i] != '\0')
	{
		if (!ft_str_is_alpha(str[i - 1]) && !ft_str_is_numeric(str[i - 1]))
		{
			if (ft_str_is_lowercase(str[i]))
				str[i] -= 32;
		}
		i++;
	}
	return (str);
}
