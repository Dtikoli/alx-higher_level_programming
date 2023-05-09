#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer the head list.
 * @number: integer value of list.
 * Return: address of the new node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *prev;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	tmp = *head;
	while (tmp && tmp->n < number)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	if (tmp == NULL)
	{
		prev->next = new;
		new->next = NULL;
		return (new);
	}
	else
	{
		prev->next = new;
		new->next = tmp;
		return (new);
	}

	return (NULL);
}
