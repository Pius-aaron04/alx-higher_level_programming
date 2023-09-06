/**
 * check_cycle - checks for cycle in a linked list
 * @list: list to check
 * Return: 0 if none found otherwise 1
#include "lists.h"

int check_cycle(listint_t *list) 
{
	listint_t *tortoise = list;
	listint_t *hare = list;


	if (list == NULL || list->next == NULL)
		return (0);
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}

	return (0);
}

