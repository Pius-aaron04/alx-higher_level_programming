#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * _memcpy - copies memory block from a source to destination
 * memory block
 * @dest: destination memory
 * @src: source memory
 * @n: number of bytes
 * Return: dest
 */

char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int k;

	for (k = 0; k < n; k++)
		dest[k] = src[k];
	return (dest);
}

/**
 * _realloc - reallocates memory address
 * @ptr: pointer to be rallocated
 * @old_size: size to be changed
 * @new_size: size of memory to allocate
 * Return: void pointer
 */

void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *new_memory;

	if (new_size == old_size)
		return (ptr);
	if (ptr == NULL)
	{
		new_memory = malloc(new_size);
		return (new_memory);
	}
	if (new_size == 0 && ptr != NULL)
	{
		free(ptr);
		return (NULL);
	}
	new_memory = malloc(new_size);
	if (new_memory == NULL)
		return (NULL);
	_memcpy(new_memory, ptr, old_size);
	free(ptr);
	return (new_memory);
}

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
		return (0);

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
