#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

def ll_get(head, index):
    """Return the ListItem for the index'th item"""
    cur = head
    i = 0
    while i < index:
        i += 1
        cur = cur.next
        if not cur:
            return None
    return cur

ListItem = namedtuple('FooBar', ['next', 'value'])

head = ListItem(None, 'Hello')

# Add new linkage to world

new = ListItem(None, 'World')
head = ListItem(new, head.value)

print(ll_get(head, 1).value)
