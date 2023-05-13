#include "lists.h"

/**
 * _palim - matches and returns true if palindrome
 * @head1: ptr to head of list1
 * @head2: ptr to head of list2
 * Return: 0 if not, 1 if yes
 */
int _palim(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1 = head1;
	listint_t *tmp2 = head2;

	while (tmp2 != NULL)
	{
		if (tmp2->n != tmp1->n)
			return (0);
		tmp2 = tmp2->next;
		tmp1 = tmp1->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses linked list starting at ptr given
 * @head: ptr to the head of the linked list
 * Return: return head of reversed list (tail of original list)
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int ret;
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *detached = NULL;
	listint_t *reversed = NULL;

	if (!head) /* non-existing list is not */
		return (0);
	if (!*head || !(*head)->next) /* empty or single list is palindrome */
		return (1);

	while (fast != NULL && fast->next != NULL) /*find midpoint */
	{
		detached = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		detached = slow;
		slow = slow->next;
	}

	reversed = reverse_listint(&slow); /* reverse midpt to compare */
	ret = _palim(*head, reversed);

	reversed = reverse_listint(&reversed); /* reverse midpt & reattach */
	detached->next = reversed;

	return (ret);
}
