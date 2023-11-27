import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_weakness(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
                if node.is_end:
                    return True  # Return True if the current position indicates the end of a word
            else:
                break
        return False

def has_all_uppercase(text):
    return bool(re.search(r'^[A-Z]+$', text))

def has_all_lowercase(text):
    return bool(re.match(r'^[a-z]+$', text))

def has_all_numbers(text):
    return bool(re.match(r'^[0-9]+$', text))

def getPasswordStrength(passwords, dict_words):
    trie = Trie()
    for word in dict_words:
        trie.insert(word)

    result = []
    for password in passwords:
        is_weak = False

        if has_all_uppercase(password) or has_all_numbers(password) or has_all_lowercase(password):
        	result.append("weak")
        	continue

        for i in range(len(password)):
            if trie.search_weakness(password[i:]):
                is_weak = True
                break
        if is_weak:
            result.append("weak")
        else:
            result.append("strong")
    return result

# Example usage
# passwords = ["password123", "hello123", "strongpassword", "weakpass"]

passwords = ["iliketoCode", "teaMakesMehappy", "abracaDabra", "pasSword", "blackcoffeelSthebest", "12345","YUIOYES","qwertyuiop"]
dict_words = ["coding", "happy", "coffee"]
result = getPasswordStrength(passwords, dict_words)
print("Password Strengths:", result)
