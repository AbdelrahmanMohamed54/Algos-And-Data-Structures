def brute_force(text, pattern):
  """
  Brute-force pattern matching algorithm.

  Args:
    text: The text to search.
    pattern: The pattern to search for.

  Returns:
    The index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.
  """

  i = 0
  j = 0

  while i < len(text) and j < len(pattern):
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      i = i - j + 1
      j = 0

  if j == len(pattern):
    return i - j
  else:
    return -1


def kmp(text, pattern):
  """
  KMP pattern matching algorithm.

  Args:
    text: The text to search.
    pattern: The pattern to search for.

  Returns:
    The index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.
  """

  pi = [0 for _ in range(len(pattern))]

  for i in range(1, len(pattern)):
    j = pi[i - 1]

    while j > 0 and pattern[i] != pattern[j]:
      j = pi[j - 1]

    if pattern[i] == pattern[j]:
      j += 1

    pi[i] = j

  i = 0
  j = 0

  while i < len(text) and j < len(pattern):
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      if j == 0:
        i += 1
      else:
        j = pi[j - 1]

  if j == len(pattern):
    return i - j
  else:
    return -1


def boyer_moore(text, pattern):
  """
  Boyer-Moore pattern matching algorithm.

  Args:
    text: The text to search.
    pattern: The pattern to search for.

  Returns:
    The index of the first occurrence of the pattern in the text, or -1 if the pattern is not found.
  """
  bad_character_table = [len(pattern) for _ in range(256)]

  for i in range(len(pattern)):
    bad_character_table[ord(pattern[i])] = len(pattern) - i - 1

  i = len(pattern) - 1
  j = len(text) - 1

  while i >= 0 and j >= 0:
    if text[j] == pattern[i]:
      i -= 1
      j -= 1
    else:
      j -= bad_character_table[ord(text[j])]

  if i < 0:
    return j + 1
  else:
    return -1
