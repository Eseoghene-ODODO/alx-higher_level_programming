#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to head node of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	/* Find middle node */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* Reverse second half */
	prev = NULL;
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	/* Compare first and second half */
	fast = *head;
	while (prev != NULL)
	{
		if (fast->n != prev->n)
		{
			return (0);
		}
		fast = fast->next;
		prev = prev->next;
	}

	return (1);
}
