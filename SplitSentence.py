

import spacy

CD = spacy.load('en_core_web_sm')
sentence = "He eats cheese, but he won't eat ice cream."
doc = CD(sentence)

for token in doc:
    ancestors = [t.text for t in token.ancestors] 
    children = [t.text for t in token.children]
    print(token.text, "\t", token.i, "\t", 
          token.pos_, "\t", token.dep_, "\t", 
          ancestors, "\t", children)