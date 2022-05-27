# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
import string
common_punctuations = list(string.punctuation)
def find_anagram(word, anagram):
    #[assignment] Add your code here
    word_list , anagram_list= word.lower().split(), anagram.lower().split()

    #further definitions, to ensure spaces are included and otherwise
    word = ''
    for each_word in word_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                word += char

    anagram = ''
    for each_word in anagram_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                anagram += char

    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

print(find_anagram('Big man','nab-mig'))
print(find_anagram('ten','net'))
print(find_anagram('orange', 'soccer'))
