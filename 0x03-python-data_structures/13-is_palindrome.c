#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *rev(listint_t **head)
{
	listint_t *temp, *current, *prev = NULL;
	temp = *head;

	if (*head == NULL)
		return (NULL);
	while (temp != NULL)
	{
		current = temp->next;
		temp->next = prev;
		prev = temp;
		temp = current;
	}
	return (prev);
}

int is_palindrome(listint_t **head)
{
	listint_t *copy;
	if (*head == NULL)
		return (0);
	copy = rev(head);
	if (copy == NULL)
		return (1);
	while(copy != NULL)
	{
		if (copy->n == (*head)->n)
		{
			*head = (*head)->next;
			copy = copy->next;
		}
		else
			return (0);
	}
	return (1);
}
