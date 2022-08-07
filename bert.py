from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import csv

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

good = -1
bad = 0
neutral = 0
tuntematon = 0


with open('aineisto.csv') as file_obj:
      

    reader_obj = csv.reader(file_obj)

      

    for row in reader_obj:

        s = ''.join(row)
        tokens = tokenizer.encode(s, return_tensors='pt')
        result = model(tokens)
        result.logits
        pisteet = int(torch.argmax(result.logits))+1

        if pisteet <= 2:

            bad += 1

        elif pisteet == 3:

            neutral += 1

        else:
        
            good += 1


print("positiiviset:",good,"negatiiviset:", bad,"neutraalit:", neutral)
print("pos %:", good / (good + bad + neutral)*100)
print("neg %:", bad / (good + bad + neutral)*100)
print("neut %:", neutral / (good + bad + neutral)*100)
