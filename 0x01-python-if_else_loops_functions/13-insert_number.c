#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts node to a sorted list
 * @head: pointer to the list
 * @number: value to insert
 * Return: address to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, current = *head, prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->next = NULL;
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (current)
	{
		if (new_node->n < current->n)
		{
			new_node->next = current;
			return (new_node);
		}
	}
	current->next = new_node;
	return (new_node);
}
