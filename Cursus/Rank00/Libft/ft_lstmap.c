/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: claudialbombin <claudialbombin@student.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/08 22:28:17 by clopez-b          #+#    #+#             */
/*   Updated: 2026/05/18 15:15:43 by claudialbom      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static void	ft_lstmap_add_back(t_list **head, t_list **tail, t_list *new_node)
{
	if (!*head)
		*head = new_node;
	else
		(*tail)->next = new_node;
	*tail = new_node;
}

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
		ft_lstmap_add_back(&head, &new_list, new_node);
		lst = lst->next;
	}
	return (head);
}
// int	main(void)
// {
// 	printf("ft_lstmap: prueba rápida\n");
// 	return (0);
// }
