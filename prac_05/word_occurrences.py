"""
Word Occurrences
Estimate: 20 minutes
Actual:   24 minutes
"""

text_counts = {}
user_input = input("Text: ")
list_of_texts = user_input.split()
for text in sorted(list_of_texts):
    if text not in text_counts.values():
        text_counts[text] = 1
    else:
        text_counts[text] += 1
    max_width = max(len(text) for text in list_of_texts)
    print(f"{text:{max_width}}:{text_counts[text]}")
