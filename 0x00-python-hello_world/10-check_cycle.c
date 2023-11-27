#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *s2;
  listint_t *prev;

  s2 = list;
  prev = list;
  while (list && s2 && s2->next)
  {
    list = list->next;
    s2 = s2->next->next;

    if (list == s2)
    {
      list = prev;
      prev =  s2;
      while (1)
      {
        s2 = prev;
        while (s2->next != list && s2->next != prev)
        {
          s2 = s2->next;
        }
        if (s2->next == list)
          break;

        list = list->next;
      }
      return (1);
    }
  }

  return (0);
}
