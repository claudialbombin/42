/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_test_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/20 11:07:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../get_next_line_bonus.h"
#include <fcntl.h>
#include <stdio.h>

/*
** Bonus test helper.
** The prefix makes the output readable when the tester alternates between
** two file descriptors, which is the core behavior the bonus must preserve.
*/
static void	print_file(int fd, char *prefix)
{
	char	*line;

	line = get_next_line(fd);
	while (line)
	{
		printf("%s%s", prefix, line);
		free(line);
		line = get_next_line(fd);
	}
}

/*
** The bonus main opens two independent descriptors and reads them one after
** the other. That setup checks that each descriptor keeps its own buffer and
** does not leak state into the other stream.
*/
int	main(int argc, char **argv)
{
	int		fd1;
	int		fd2;

	if (argc != 3)
	{
		printf("Usage: %s <file1> <file2>\n", argv[0]);
		return (1);
	}
	fd1 = open(argv[1], O_RDONLY);
	fd2 = open(argv[2], O_RDONLY);
	if (fd1 < 0 || fd2 < 0)
	{
		printf("Error: could not open one of the files\n");
		return (1);
	}
	print_file(fd1, "[fd1] ");
	print_file(fd2, "[fd2] ");
	close(fd1);
	close(fd2);
	return (0);
}
