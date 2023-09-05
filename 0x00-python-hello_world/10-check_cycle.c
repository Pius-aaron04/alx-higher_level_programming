#include "lists.h"
#include <stdio.h>


/**
 * check_cycle - checks if there is a cycle in a list
 * @list: list to check
 * Return: 0 if no cycle found else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *temp = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (current)
	{
		temp = current->next->next;
		current = current->next;
		if (temp == current)
			return (1);
	}
	return (0);
}
