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
	listint_t *move1, *move2;

	if (list == NULL)
		return (0);
	move1 = list;
	move2 = list;
	while (move1 != NULL && move2 != NULL && move2->next != NULL)
	{
		move1 = move1->next;
		move2 = move2->next->next;
		if (move1 == move2)
			return (1);
	}
	return (0);
}
