/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/20 11:06:00 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static void	gnl_reset(char **saved)
{
	free(*saved);
	*saved = NULL;
}

static char	*fill_buffer(int fd, char *saved)
{
	char		*buf;
	ssize_t		bytes_read;
	char		*tmp;

	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
		return (gnl_reset(&saved), NULL);
	bytes_read = 1;
	while (!gnl_strchr(saved, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buf, BUFFER_SIZE);
		if (bytes_read < 0)
			return (gnl_reset(&saved), free(buf), NULL);
		buf[bytes_read] = '\0';
		tmp = saved;
		saved = gnl_strjoin(tmp, buf);
		free(tmp);
		if (!saved)
			break ;
	}
	free(buf);
	if (bytes_read < 0)
		return (gnl_reset(&saved), NULL);
	return (saved);
}

static char	*extract_line(char *saved)
{
	char	*nl;
	size_t	len;

	nl = gnl_strchr(saved, '\n');
	if (nl)
		len = (size_t)(nl - saved) + 1;
	else
		len = gnl_strlen(saved);
	return (gnl_substr(saved, 0, len));
}

static char	*keep_remainder(char *saved)
{
	char	*nl;
	char	*rest;

	nl = gnl_strchr(saved, '\n');
	if (!nl)
	{
		free(saved);
		return (NULL);
	}
	rest = gnl_substr(saved, (size_t)(nl - saved) + 1, gnl_strlen(nl + 1));
	free(saved);
	return (rest);
}

char	*get_next_line(int fd)
{
	static char	*saved[MAX_FD];
	char		*line;

	if (fd < 0 || fd >= MAX_FD || BUFFER_SIZE <= 0)
		return (NULL);
	if (!saved[fd])
		saved[fd] = gnl_substr("", 0, 0);
	if (!saved[fd])
		return (NULL);
	saved[fd] = fill_buffer(fd, saved[fd]);
	if (!saved[fd] || !*saved[fd])
		return (gnl_reset(&saved[fd]), NULL);
	line = extract_line(saved[fd]);
	if (!line)
		return (gnl_reset(&saved[fd]), NULL);
	saved[fd] = keep_remainder(saved[fd]);
	return (line);
}
