from collections import defaultdict
from operator import index


def load_doc(filename):
    with open(filename, mode='rt', encoding='utf-8') as file:
        text = file.read()
    return text


def get_sents(text):
    sents = text.strip().split('\n')
    return sents


def isindicValid(indicSentence) -> bool:
    for c in indicSentence:
        if c >= 'A' and c <= 'Z':
            return False
        if c >= 'a' and c <= 'z':
            return False
        if ord(c) >= 161 and ord(c) <= 255:
            return False
    return True


def isEnglishValid(englishSentence) -> bool:
    for c in englishSentence:
        if ord(c) >= 161 and ord(c) <= 255:
            return False
        else:
            return True


def get_x_sents(sents, hi_sents):
    final_sents = []
    indexes = []
    nums = 0
    for s in range(0, len(sents)):
        length = len(sents[s].split())
        if(length >= 20 and isEnglishValid(sents[s]) and isindicValid(hi_sents[s]) and length <= 100):
            nums += 1
            final_sents.append(sents[s])
            indexes.append(s)
        if(nums == 100):
            break
    return final_sents, indexes


def dump_eng_doc(filename, text):
    with open(filename, 'w') as file:
        file.write(text)


def dump_hi_doc(filename, sents, indexes):
    final_sents = []
    for i in indexes:
        final_sents.append(sents[i])
    text = '\n'.join(final_sents)
    with open(filename, 'w') as file:
        file.write(text)


filename = "v3/v2/en-ml/test.txt"
text = load_doc(filename)
sents = get_sents(text)

hi_filename = "v3/v2/en-ml/thi.txt"
hi_text = load_doc(hi_filename)
hi_sents = get_sents(hi_text)
final_sents, indexes = get_x_sents(sents, hi_sents)
dump_eng_doc("dumpen_hundred.txt", '\n'.join(final_sents))
dump_hi_doc("dumpml_hundred.txt", hi_sents, indexes)
