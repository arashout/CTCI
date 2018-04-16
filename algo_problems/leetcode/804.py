def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    def getMorseCodeOfLetter(letter):
        morseCodeAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        i = ord(letter) - ord('a')
        return morseCodeAlphabet[i]
    
    def transformation(w):
        result = ""
        for l in w:
            result += getMorseCodeOfLetter(l)
        return result
    
    uniqueMorseWords = {}
    for word in words:
        uniqueMorseWords[transformation(word)] = True
    
    return len(uniqueMorseWords)