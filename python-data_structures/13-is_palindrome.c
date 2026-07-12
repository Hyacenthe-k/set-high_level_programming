#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the head of the list to reverse
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *next = NULL;

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
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half = NULL;
    listint_t *middle = NULL;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    second_half = reverse_list(slow);
    slow = *head;

    while (second_half != NULL)
    {
        if (slow->n != second_half->n)
        {
            is_pal = 0;
            break;
        }
        slow = slow->next;
        second_half = second_half->next;
    }

    if (middle != NULL)
    {
        /* Optional: restoring the list structure */
        middle = middle; 
    }

    return (is_pal);
}
