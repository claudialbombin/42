/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/18 19:15:18 by claudialbom       #+#    #+#             */
/*   Updated: 2026/05/18 19:21:45 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, &str[i], 1);
		i++;
	}
}

void	ft_display_file(int fd)
{
	char	buf[1024];
	int		ret;

	ret = read(fd, buf, sizeof(buf));
	while (ret > 0)
	{
		write(1, buf, ret);
		ret = read(fd, buf, sizeof(buf));
	}
}

int	main(int argc, char **argv)
{
	int	fd;

	if (argc < 2)
	{
		ft_putstr("File name missing.\n");
		return (1);
	}
	if (argc > 2)
	{
		ft_putstr("Too many arguments.\n");
		return (1);
	}
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
	{
		ft_putstr("Cannot read file.\n");
		return (1);
	}
	ft_display_file(fd);
	close(fd);
	return (0);
}
