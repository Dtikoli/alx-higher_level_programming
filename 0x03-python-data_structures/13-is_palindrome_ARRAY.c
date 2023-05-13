#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	size_t len = 0, i;
	int *node_data;

	if (!head) /* non-existing list is not a palindrome*/
		return (0);

	if (!*head || !(*head)->next)
		return (1); /* empty or single node list is palindrome */

	while (tmp) /* find length of list */
	{
		tmp = tmp->next;
		len += 1;
	}

	node_data = malloc(sizeof(int) * len);
	if (!node_data)
		return (0);
	tmp = *head;
	for (i = 0; i < len; i++) /* pull node data into array to compare */
	{
		node_data[i] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (node_data[i] != node_data[len - i - 1])
		{
			free(node_data); /* free alloc'ed memory on exit*/
			return (0);
		}
	}
	free(node_data); /* free alloc'ed memory at the end of loop */
	return (1);
}
