#include "lists.h"

/**
 * check_cycle - find the loop in a linked list
 * @list: linked list
 * Return: 1 if there is cyle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *lag, *lead;

	if (!list)
		return (0);

	lag = lead = list;
	while (lag && lead && lead->next)
	{
		lag = lag->next;
		lead = lead->next->next;

		if (lag == lead)
			return (1);
	}
	return (0);
}

