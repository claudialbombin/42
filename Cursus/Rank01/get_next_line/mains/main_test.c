/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_test.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/16 22:59:50 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

/*
** Mandatory test entry point.
** It opens one file, keeps pulling lines until EOF, and prints each line
** exactly as returned by get_next_line so the tester can verify formatting.
*/
static void	print_file(int fd)
{
	char	*line;

	line = get_next_line(fd);
	while (line)
	{
		printf("%s", line);
		free(line);
		line = get_next_line(fd);
	}
}

/*
** The main function only validates the command line, opens the file, calls
** the reader helper, and closes the descriptor when the stream is finished.
*/
int	main(int argc, char **argv)
{
	int		fd;

	if (argc != 2)
	{
		printf("Usage: %s <file>\n", argv[0]);
		return (1);
	}
	fd = open(argv[1], O_RDONLY);
	if (fd < 0)
	{
		printf("Error: could not open %s\n", argv[1]);
		return (1);
	}
	print_file(fd);
	close(fd);
	return (0);
}
