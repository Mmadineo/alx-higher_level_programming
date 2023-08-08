#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @i: integer
 * @nxt: points to the next node
 *
 */

typedef struct listint_s
{
	int i;
	struct listint_s *nxt;
} listint_t;

size_t print_listint(const listint_t *t);
listint_t *add_nodeint(listint_t **head, const int i);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
