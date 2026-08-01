/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   small_sort_moves.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b, pvivas-f <clopez-b, pvivas-f@    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/01 14:05:56 by clopez-b, p       #+#    #+#             */
/*   Updated: 2026/08/01 14:05:57 by clopez-b, p      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/**
 * @brief Swaps the first two elements of an array, mirroring sa/sb.
 *
 * Pure array transform mirroring sa/sb, but operating on the small
 * fixed-size int arrays a t_state holds instead of the real
 * linked-list stacks. Used only by the BFS search over abstract
 * states; the real stacks are moved separately once the winning
 * sequence of moves is known.
 *
 * @param arr Array to modify in place.
 * @param len Number of valid elements in arr.
 * @return void
 */
void	arr_swap(int *arr, int len)
{
	int	tmp;

	if (len < 2)
		return ;
	tmp = arr[0];
	arr[0] = arr[1];
	arr[1] = tmp;
}

/**
 * @brief Rotates an array upward by one, mirroring ra/rb.
 *
 * The first element becomes the last, everything else shifts up by
 * one position. Used by the BFS search over abstract states.
 *
 * @param arr Array to modify in place.
 * @param len Number of valid elements in arr.
 * @return void
 */
void	arr_rotate(int *arr, int len)
{
	int	first;
	int	i;

	if (len < 2)
		return ;
	first = arr[0];
	i = 0;
	while (i < len - 1)
	{
		arr[i] = arr[i + 1];
		i++;
	}
	arr[len - 1] = first;
}

/**
 * @brief Rotates an array downward by one, mirroring rra/rrb.
 *
 * The last element becomes the first, everything else shifts down by
 * one position. Used by the BFS search over abstract states.
 *
 * @param arr Array to modify in place.
 * @param len Number of valid elements in arr.
 * @return void
 */
void	arr_reverse_rotate(int *arr, int len)
{
	int	last;
	int	i;

	if (len < 2)
		return ;
	last = arr[len - 1];
	i = len - 1;
	while (i > 0)
	{
		arr[i] = arr[i - 1];
		i--;
	}
	arr[0] = last;
}

/**
 * @brief Moves the first element of one array onto another, mirroring
 * pa/pb.
 *
 * Removes src[0], shifting the rest of src down by one, and inserts
 * that value at dest[0], shifting the rest of dest up by one. Used by
 * the BFS search over abstract states.
 *
 * @param dest Destination array, grown by one element.
 * @param dest_len Pointer to the number of valid elements in dest.
 * @param src Source array, shrunk by one element.
 * @param src_len Pointer to the number of valid elements in src.
 * @return void
 */
void	arr_push(int *dest, int *dest_len, int *src, int *src_len)
{
	int	val;
	int	i;

	if (*src_len == 0)
		return ;
	val = src[0];
	i = 0;
	while (i < *src_len - 1)
	{
		src[i] = src[i + 1];
		i++;
	}
	(*src_len)--;
	i = *dest_len;
	while (i > 0)
	{
		dest[i] = dest[i - 1];
		i--;
	}
	dest[0] = val;
	(*dest_len)++;
}
