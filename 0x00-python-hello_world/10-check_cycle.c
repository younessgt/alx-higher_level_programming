#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - function that checks
 * if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	if (list == NULL)
		return (0);
	head = list;
	while (list->next != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}
	return (0);
}
