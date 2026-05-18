/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clopez-b <clopez-b@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#             */
/*   Updated: 2025/10/08 22:28:26 by clopez-b         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

t_list	*ft_lstmap(t_list *lst, t_list *(*f)(t_list *elem))
{
	t_list	*new_list;
	t_list	*new_node;
	t_list	*head;

	if (!lst || !f)
		return (NULL);
	head = NULL;
	new_list = NULL;
	while (lst)
	{
		new_node = f(lst);
		if (!new_node)
			return (head);
		if (!head)
		{
			head = new_node;
			new_list = head;
		}
		else
		{
			new_list->next = new_node;
			new_list = new_list->next;
		}
		lst = lst->next;
	}
	return (head);
}
