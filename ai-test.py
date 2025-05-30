
def insert_word_into_trie(trie, word, frequency):
    """
    Inserts a word with its frequency into the trie.
    :param trie: The root of the trie (a dictionary).
    :param word: The word to insert.
    :param frequency: The frequency of the word.
    """
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['$'] = frequency  # '$' marks the end of the word and stores frequency

# Example usage:
dictionary = [
    {"word": "project", "frequency": 200},
    {"word": "prompt", "frequency": 150},
    {"word": "product", "frequency": 180},
    {"word": "program", "frequency": 170}
]

trie = {}
for entry in dictionary:
    insert_word_into_trie(trie, entry["word"], entry["frequency"])

# trie now contains all words and their frequencies
