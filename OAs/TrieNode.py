from collections import deque

class TrieNode:
    def __init__(self):
        self.char = ["" for i in range(26)]
        self.wordEnd = False
        self.length = 0

    def update_count(self):
        self.length += 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                curr.char[ord(i) - 97] = TrieNode()
            curr = curr.char[ord(i) - 97]

        curr.wordEnd = True
        curr.update_count()

    def search(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                return False
            curr = curr.char[ord(i) - 97]

        return curr.wordEnd


    def runBfs(self, curr, prefix):
        result = []
        bfsStack = deque()
        bfsStack.append((curr, prefix))

        while bfsStack:
            size = len(bfsStack)

            for i in range(size):
                curr, prefix = bfsStack.popleft()
                if curr.wordEnd:
                    print(curr.length)
                    result.append(prefix)
                for j in range(26):
                    if curr.char[j]:
                        new_prefix = prefix + chr(j+97)
                        bfsStack.append((curr.char[j], new_prefix))

        return result

    # modify prefix
    def startsWith(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                return {}
            curr = curr.char[ord(i) - 97]

        group = self.runBfs(curr, word)

        result = {}

        for compl in group:
            result[compl] = word

        return result

class Solution:

    def __init__(self):
        pass

    def replaceWords(self, dictionary):
        # solved through BFS
        
        obj = Trie()

        letters = set()

        freq = Counter(dictionary)

        for word in dictionary:
            new_word = list(word)
            new_word.reverse()
            new_word = ''.join(new_word)
            letters.add(new_word[0])
            obj.insert(new_word)

        result = {}
        print(letters)
        for word in letters:
            group = obj.startsWith(word)
            for key, val in group.items():
                # if the key is not present 
                if key not in result:
                    result[key] = val
                # if the key is present then check length of the previous prefix
                # you can avoid this by sorting the dictionary words by length
                elif len(val) < len(result[key]):
                    result[key] = val
        print(result)

        final_result = {}
        for key, val in result.items():
            if val not in final_result:
                final_result[val] = [key[::-1]]
            else:
                final_result[val].append(key[::-1])

        print(final_result)

        return final_result.values()
        # final_sentence = []
        # for word in sentence.split(' '):
        #     if word in result:
        #         final_sentence.append(result[word])
        #     else:
        #         final_sentence.append(word)

        # return ' '.join(final_sentence)

# words = ["back","backdoor", "gammon", "backgammon", "comeback", "come", "door"]
# words = ["a", "a", "a", "a"]
words = ["cba", "a", "a", "b", "ba", "ca"]

obj = Solution()
print(obj.replaceWords(words))