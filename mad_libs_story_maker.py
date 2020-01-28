"""
### Mad Libs Story Maker
Ever played [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs)? If you haven't, 
here are the basics:

"Mad Libs consist of a book that has a short story on each page with many key 
words replaced with blanks. Beneath each blank is specified a lexical or other 
category, such as "noun," "verb," "place," or "part of the body." One player 
asks the other players, in turn, to contribute some word for the specified type 
for each blank, but without revealing the context for that word. Finally, the 
completed story is read aloud. The result is usually comic, surreal and somewhat 
nonsensical."

- Create a Mad Libs style game, where the program asks the user for certain 
types of words, and then prints out a story with the words that the user inputted.
- The story doesn't have to be too long, but it should have some sort of story 
line.
- Tip: it's easiest to write out a quick story on a piece of paper or a word 
document, and then go back through and see which words the user should be able 
to change.
- Subgoals:
  - If the user has to put in a name, change the first letter to a capital 
  letter.
  - Change the word "a" to "an" when the next word in the sentence begins with 
  a vowel.
  
    "___________! he said ________ as he jumped into his convertible
     exclamation           adverb
                                                     
  ______ and drove off with his _________ wife."
   noun                         adjective
"""
word_type = ['exclamation', 'adverb', 'noun', 'adjective']
words_used = dict()

def mad_libs(word):
    print("\n{0}! he said {1} as he jumped into his convertible {2} and drove off with his {3} wife.".format(word['exclamation'].capitalize(), word['adverb'], word['noun'], word['adjective']))


if __name__ == '__main__':
    
    for i in word_type:
        words_used[i] = input("Enter a word for the {0} category: ".format(i))
    mad_libs(words_used)