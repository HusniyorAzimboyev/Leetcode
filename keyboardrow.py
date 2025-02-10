def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    correctWords = []
    for word in words:
        wordlower = word.lower()
        for row in rows:
            correct = 0
            for letter in list(wordlower):
                if letter not in list(row):
                    break
                else:
                    correct+=1
            if correct == len(wordlower):
                correctWords.append(word)
    return correctWords
result = findWords(["Hello","Alaska","Dad","Peace"])
print(result)