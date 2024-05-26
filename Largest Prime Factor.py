#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def largest_prime_factor(target):
  i = 2
  while i * i <= target:
      if (target % i) != 0:
          i += 1
      else:
          target //= i
  return target

