#include "lists.h"
listint_t *reverse_list(listint_t *head);
#include <stddef.h>

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;

    while (head != NULL)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *middle = NULL;
    listint_t *p1, *p2;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        middle = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = reverse_list(slow);
    p1 = *head;
    p2 = second_half;

    while (p2 != NULL)
    {
        if (p1->n != p2->n)
        {
            is_pal = 0;
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    reverse_list(second_half);
    return (is_pal);
}
