/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_count.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 00:00:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putstr_count(char *s)
{
	int	count;

	if (!s)
		return (ft_putstr_count("(null)"));
	count = 0;
	while (s[count])
	{
		write(1, &s[count], 1);
		count++;
	}
	return (count);
}
