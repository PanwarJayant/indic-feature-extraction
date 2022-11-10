from tqdm import tqdm

# MAPPING SWARAS AND MATRAS
hindiSwaras = ['अं','अः','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ']
hindiMatras = [chr(2306), chr(2307)]

for x in range(2366,2372):
  hindiMatras.append(chr(x))

hindiMatras.append(chr(2375))
hindiMatras.append(chr(2376))
hindiMatras.append(chr(2379))
hindiMatras.append(chr(2380))

print(len(hindiSwaras))
hindiMatraSwaraMapping = {}

for i in range(12):
    hindiMatraSwaraMapping[hindiMatras[i]]=hindiSwaras[i]

# LOAD HINDI-100 SAMANANTHAR DATASET
with open("./en-hi_dump/dumphi_lakh.txt", mode='rt', encoding='utf-8') as file:
  text = file.read()
sents = text.strip().split('\n')

newsents = []
for x in tqdm(range(0,len(sents))):
  sent = sents[x]
  sent = sent.replace("।", "")
  newsent = ""
  words = sent.split(' ')
  for word in words:
    #print(word)      
    matraSuffix = ''
    for ch in word:
      if ch in hindiMatraSwaraMapping:
        matraSuffix += hindiMatraSwaraMapping[ch]
    neword = word + matraSuffix
    newsent += neword + " "
  newsent = newsent.strip()
  newsents.append(newsent)

# print(newsents)

newtext = '\n'.join(newsents)
with open("./en-hi_dump/dumphi2_lakh.txt", 'w') as file:
  file.write(newtext)