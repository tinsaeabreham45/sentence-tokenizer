import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import state_union, stopwords
from nltk.tag import pos_tag

sentence = input('Give Me A sentence: ')
# Tokenize the sentence
tokenized_sent = word_tokenize(sentence.lower())
pos_tagged_sent = pos_tag(tokenized_sent)
# filtering the adjective 
adj_list = [word for (word, pos) in pos_tagged_sent if pos.startswith('JJ')]
# Filtering the nouns
Noun_list =[word for (word, pos) in pos_tagged_sent if pos.startswith('NN')]
# Filtering the verb
Verb_list = [word for (word, pos) in pos_tagged_sent if pos.startswith('VBZ')]

determiner_list = [word for (word, pos) in pos_tagged_sent if pos.startswith('BT')]
pre_lists = [word for (word, pos) in pos_tagged_sent if pos.startswith('IN')]

print("the only Nouns here are: ")
for i in Noun_list:
        print("- {}".format(i))
print("The only Verbs Here are: ")
for i in Verb_list:
        print("- {}".format(i))
print("the only adjectives here are: ")
for i in adj_list:
    print("- {}".format(i))
print("the only Preposition here are: ")
for i in pre_lists:
    print("- {}".format(i))


