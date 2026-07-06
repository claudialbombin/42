/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/06 00:00:00 by clopez-b          #+#    #+#             */
/*   Updated: 2026/07/06 12:02:53 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*append_buffer(char *saved, char *buf)
{
	char	*tmp;

	tmp = saved;
	saved = gnl_strjoin(tmp, buf);
	free(tmp);
	return (saved);
}

static char	*fill_buffer(int fd, char *saved)
{
	char	*buf;
	ssize_t	bytes_read;

	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
		return (NULL);
	bytes_read = 1;
	while (!gnl_strchr(saved, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buf, BUFFER_SIZE);
		if (bytes_read < 0)
		{
			free(buf);
			free(saved);
			return (NULL);
		}
		buf[bytes_read] = '\0';
		saved = append_buffer(saved, buf);
		if (!saved)
			break ;
	}
	free(buf);
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
	static char	*saved;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (!saved)
		saved = gnl_substr("", 0, 0);
	saved = fill_buffer(fd, saved);
	if (!saved || !*saved)
	{
		free(saved);
		saved = NULL;
		return (NULL);
	}
	line = extract_line(saved);
	saved = keep_remainder(saved);
	return (line);
}
