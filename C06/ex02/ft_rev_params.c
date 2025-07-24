/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 10:43:18 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/24 10:44:11 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_param_name(char *name)
{
	int	i;

	i = 0;
	while (name[i] != '\0')
	{
		write(1, &name[i], 1);
		i++;
	}
	write(1, "\n", 1);
}

int	main(int argc, char *argv[])
{
	int	i;

	i = 1;
	while (argc - i > 0)
	{
		print_param_name(argv[argc - i]);
		i++;
	}
	return (0);
}
