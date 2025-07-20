/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 13:52:36 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/20 18:54:08 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}

int	ft_check_base(char *base)
{
	int	i;
	int	j;
	int	len;

	i = 0;
	len = ft_strlen(base);
	if (len < 2)
		return (0);
	while (i < len)
	{
		if (base[i] == '+' || base[i] == '-' || base[i] == ' ' ||
			(base[i] >= '\t' && base[i] <= '\r'))
			return (0);
		j = i + 1;
		while (j < len)
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

int	ft_get_index(char c, char *base)
{
	int	i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

int	ft_atoi_base(char *str, char *base)
{
	int	sign;
	int	result;
	int	base_len;
	int	index;

	sign = 1;
	result = 0;
	if (!ft_check_base(base))
		return 0;
	base_len = ft_strlen(base);
	while (*str == ' ' || (*str >= '\t' && *str <= '\r'))
		str++;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign *= -1;
			str++;
	}
	index = ft_get_index(*str, base);
	while (index >= 0)
		result = result * base_len + index;
		str++;
		index = ft_get_index(*str, base);
	return (result * sign);
}
