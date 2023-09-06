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
	listint_t *new_node, *current, *prev = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->next = NULL;
	new_node->n = number;
	if (prev == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (prev->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = prev->next;
	while (current)
	{
		if (number < current->n)
		{
			new_node->next = current;
			prev->next = new_node;
			return (new_node);
		}
		prev = current;
		current = current->next;
	}
	current = new_node;
	return (new_node);
}
