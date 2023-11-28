#include "lists.h"

/**
 * insert_node - function that inserts a new node
 * at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *h;
	listint_t *h_prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (current == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		h_prev = h;
		h = h->next;
	}

	current->n = number;

	if (*head == NULL)
	{
		current->next = NULL;
		*head = current;
	}
	else
	{
		current->next = h;
		if (h == *head)
			*head = current;
		else
			h_prev->next = current;
	}

	return (current);
}
