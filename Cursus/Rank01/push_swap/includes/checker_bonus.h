/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker_bonus.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pvivas-f <pvivas-f@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:04:01 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 15:30:41 by pvivas-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CHECKER_BONUS_H
# define CHECKER_BONUS_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 1024
# endif

# include "push_swap.h"

void	checker_read_stdin(t_stack *a, t_stack *b);
int		checker_apply_line(char *line, t_stack **a, t_stack **b);
char	*get_next_line(int fd);
size_t	gnl_strlen(const char *s);
char	*gnl_strchr(const char *s, int c);
char	*gnl_strjoin(char *s1, char *s2);
char	*gnl_substr(const char *s, size_t start, size_t len);
char	*get_next_line(int fd);

#endif
