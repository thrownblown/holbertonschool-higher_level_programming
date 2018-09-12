#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: start of list
 * @number: number to be inserted
 * Return: ptr to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h, *new = NULL;

	h = *head;
	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);
	new->n = number;
	while (h->next && h->n < number)
		if (h->next->n >= number)
		{
			new->next = h->next;
			h->next = new;
			return (new);
		}
		else
			h = h->next;
	if (h->n <= number)
		h->next = new;
	else
		return (NULL);
	return (new);
}
