#!/usr/bin/python3
def remove_char_at(str, n):
  if 0 <= n < len(str):
      return str[:n] + str[n + 1:]
  else:
      return s

# Example usage:
original_string = "chicago"
new_string = remove_char_at(original_string, 3)
print("Original String:", original_string)
print("String after removing character at position 0:", new_string)
