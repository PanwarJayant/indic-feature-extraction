import random
from sklearn.model_selection import train_test_split

with open("en-hi_dump/dumpen_lakh.txt", mode='rt', encoding='utf-8') as file:
  eng_text = file.read()
with open("en-hi_dump/dumphi2_lakh.txt", mode='rt', encoding='utf-8') as file:
  indic_text = file.read()
eng_sents = eng_text.strip().split("\n")
indic_sents = indic_text.strip().split("\n")

eng_train, eng_test, hi_train, hi_test = train_test_split(eng_sents, indic_sents, test_size=0.2)

# print(eng_train[0:5])
# print(hi_train[0:5])
# print(indic_sents[0:5])

with open("./final2.0/eng_train.txt", 'w') as f:
  for sent in eng_train:
    f.write(sent+'\n')

with open("./final2.0/eng_test.txt", 'w') as f:
  for sent in eng_test:
    f.write(sent+'\n')

with open("./final2.0/hi_train.txt", 'w') as f:
  for sent in hi_train:
    f.write(sent+'\n')

with open("./final2.0/hi_test.txt", 'w') as f:
  for sent in hi_test:
    f.write(sent+'\n')