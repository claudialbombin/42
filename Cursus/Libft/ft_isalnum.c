/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:17:01 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 14:54:11 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalnum(int c)
{
	if (((c >= '0') && (c <= '9')) || ((c >= 'A') && (c <= 'Z'))
		|| ((c >= 'a') && (c <= 'z')))
		return (1);
	return (0);
}


// int	main(void)
// {
// 	int tests[] = {'a', 'Z', '5', '!', '\n', 0};
// 	int i = 0;

// 	while (tests[i])
// 	{
// 		printf("char '%c' (%d) -> isalnum: %d\n", tests[i], tests[i], ft_isalnum(tests[i]));
// 		i++;
// 	}
// 	return (0);
// }

