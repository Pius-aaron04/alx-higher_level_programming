#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head node
 * Return: 1 if list is a palindrome, 0 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *prev;
	listint_t *slow = *head, *second_half, *current;
	int i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast)
	{
		slow = slow->next;
		i++;
		fast = fast->next->next;
	}
	second_half = NULL;
	current = slow;

	while (current)
	{
		prev = current;
		current = current->next;
		prev->next = second_half;
		second_half = prev;
	}
	slow = *head;
	while (second_half)
	{
		if (second_half->n != slow->n)
			return (0);
		second_half = second_half->next;
		slow = slow->next;
	}
	return (1);

}
