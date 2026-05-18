/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:19:40 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 14:51:30 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *str)
{
	int	i;
	int	sign;
	int	result;

	i = 0;
	sign = 1;
	result = 0;
	while ((str[i] == ' ') || (str[i] == '\n') || (str[i] == '\t')
		|| (str[i] == '\v') || (str[i] == '\f') || (str[i] == '\r'))
		i++;
	if ((str[i] == '-') || (str[i] == '+'))
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while ((str[i] >= '0') && (str[i] <= '9'))
	{
		result = result * 10 + (str[i] - '0');
		i++;
	}
	return (result * sign);
}


// #include <stdio.h>

// int	main(void)
// {
// 	const char *tests[] = {
// 		"123",
// 		"   456",
// 		"-42",
// 		"+77",
// 		"\t\n  -0012abc",
// 		"2147483647",
// 		"-2147483648",
// 		"0",
// 		"abc123",
// 		NULL
// 	};
// 	int i = 0;

// 	while (tests[i])
// 	{
// 		printf("input: '%s' => atoi: %d\n", tests[i], ft_atoi(tests[i]));
// 		i++;
// 	}
// 	return (0);
// }

