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

	while (h->next && h->n < number)
		if (h->next->n > number)
		{
			new->n = number;
			new->next = h->next;
			h->next = new;
		}
		else
			h = h->next;
	return (new);
}
