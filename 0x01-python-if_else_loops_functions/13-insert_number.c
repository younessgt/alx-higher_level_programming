#include "lists.h"
/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: pointer to pointer of type listint_t
 * @number: data of the node
 * Return: adress of the new node or NUll if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;
	listint_t *stock;

	stock = *head;
	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (stock != NULL)
	{
		if (new->n > stock->n)
		{
			temp = stock;
			stock = stock->next;
		}
		else
		{
			new->next = stock;
			temp->next = new;
			return (new);
		}
	}
	return (NULL);
}
