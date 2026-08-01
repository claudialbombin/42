/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:06:41 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:06:42 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Computes the length of a null-terminated string.
 *
 * @param s String to measure.
 * @return Number of characters before the terminating null byte.
 */
static int	ft_len(char *s)
{
	int	len;

	len = 0;
	while (s[len])
		len++;
	return (len);
}

/**
 * @brief Writes a string to a file descriptor.
 *
 * @param s String to write.
 * @param fd File descriptor to write to.
 * @return void
 */
void	ft_put_str_fd(char *s, int fd)
{
	write(fd, s, ft_len(s));
}

/**
 * @brief Writes a non-negative integer to a file descriptor.
 *
 * @param n Non-negative integer to write.
 * @param fd File descriptor to write to.
 * @return void
 */
void	ft_put_nbr_fd(int n, int fd)
{
	char	buf[12];
	int		len;

	len = 0;
	if (n == 0)
		buf[len++] = '0';
	while (n > 0)
	{
		buf[len++] = '0' + (n % 10);
		n = n / 10;
	}
	while (len > 0)
		write(fd, &buf[--len], 1);
}

/**
 * @brief Writes a value in [0, 1] as a percentage to a file descriptor.
 *
 * Formats it as "XX.XX%", rounded to two decimal places.
 *
 * @param value Value between 0.0 and 1.0 to format.
 * @param fd File descriptor to write to.
 * @return void
 */
void	ft_put_percent_fd(double value, int fd)
{
	int	scaled;

	scaled = (int)(value * 10000 + 0.5);
	ft_put_nbr_fd(scaled / 100, fd);
	ft_put_str_fd(".", fd);
	if (scaled % 100 < 10)
		ft_put_str_fd("0", fd);
	ft_put_nbr_fd(scaled % 100, fd);
	ft_put_str_fd("%", fd);
}

/**
 * @brief Zero-initializes every bench counter.
 *
 * No memset allowed, so every counter gets zeroed by hand. Called
 * once in main before any sorting happens.
 *
 * @param bench Bench struct to initialize.
 * @return void
 */
void	ft_bench_init(t_bench *bench)
{
	bench->sa = 0;
	bench->sb = 0;
	bench->ss = 0;
	bench->pa = 0;
	bench->pb = 0;
	bench->ra = 0;
	bench->rb = 0;
	bench->rr = 0;
	bench->rra = 0;
	bench->rrb = 0;
	bench->rrr = 0;
}
