/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_program_name.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/24 10:23:52 by claudialbom       #+#    #+#             */
/*   Updated: 2025/07/24 10:32:02 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_program_name(char *name)
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
	if (argc)
		print_program_name(argv[0]);
	return (0);
}
