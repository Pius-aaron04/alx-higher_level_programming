#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head node
 * Return: 1 if list is a palindrome, 0 if otherwise
 */

int is_palindrome(listint_t **head)
{
	int i = 0, *numbers = NULL;
	listint_t *current = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	/* transverse list and stores data in an array of numbers */
	while (current)
	{
		numbers = realloc(numbers, (i + 1) * sizeof(int));
		if (numbers != NULL)
		{
			numbers[i] = current->n;
		}
		else
			return (0);
		i++;
		current = current->next;
	}

	current = *head;
	i--;
	for (; current; current = current->next, i--)
	{
		if ((int)numbers[i] != current->n)
			return (0);
	}
	return (1);
}
