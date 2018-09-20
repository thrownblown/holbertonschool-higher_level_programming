#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* reverse_listint - reveses the order of a linked list
* @head: ptr to head of linked list
*
* Return: ptr to new first node
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *new, *h = NULL;

	while (*head)
	{
		new = (*head)->next;
		(*head)->next = h;
		h = *head;
		*head = new;
	}
	*head = h;

	return (*head);
}

/**
 * is_palindrome - checks to see if linked list is the same coming and going
 * @head: ptr to start of list
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow;
	int i = 1;

	if (*head == NULL)
		return (1);

	fast = *head;
	slow = *head;


	while (i++)
	{
		if (fast == NULL || fast->next == NULL)
		{
			if (i % 2)
				fast = slow->next;
			else
				fast = slow;

			fast = reverse_listint(&fast);
			slow->next = NULL;
			i = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;

	}


	while (fast != NULL && *head != NULL)
	{
		if (fast->n != (*head)->n)
			return (0);
		fast = fast->next;
		*head = (*head)->next;
	}
	return (1);


}
