#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: A pointer to the head of the linked list
 * @number: The number to insert into the list
 *
 * Return: A pointer to the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node;
  listint_t *current;

  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);

  new_node->n = number;

  /* Check if new node should be head */
  if (*head == NULL || (*head)->n >= number)
  {
    new_node->next = *head;
    *head = new_node;
    return (new_node);
  }

  /* Find position where number should be inserted */
  current = *head;
  while (current->next != NULL && current->next->n < number)
  {
    current = current->next;
  }

  /* Insert new node between current and current->next */
  new_node->next = current->next;
  current->next = new_node;

  return (new_node);
}
