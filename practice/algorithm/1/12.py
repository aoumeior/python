#!/usr/bin/python3

'You have a sequence of items,'
' and you’d like to determine the most frequently occurring items in the sequence.'

from collections import Counter

words = [
  'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes' 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
  'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
  'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(4)
# [('eyes', 7), ('look', 4), ('the', 4), ('into', 3)]


'add new words'

morewords = ['why','are','you','not','looking','in','my','eyes']

word_counts.update(morewords)

top_three = word_counts.most_common(4)

