#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for a loopy linked list
 * @list: singly linked list
 * Return: 1 if cycle, else 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list)
	{
		slow = list;
		fast = list;
	}
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
