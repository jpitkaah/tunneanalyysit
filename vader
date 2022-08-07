from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import csv

good = 0
bad = 0
neutral = -1 #koodi luokittelee viimeisen tyhjän csv-tiedoston solun neutraaliksi, joten laskenta aloitetaan miinus yhdestä
tuntematon = 0

with open('aineisto.csv') as file_obj:
      

    reader_obj = csv.reader(file_obj)
      

    for row in reader_obj:

        vs = analyzer.polarity_scores(row)
        if vs["compound"]>0:
            #print(row, "positiivinen\n",) #poistamalla hashtagin (#) print-funktion edestä, saat näkyviin tekstin
            good += 1

            
        elif vs["compound"]<0:
            #print(row, "negatiivinen\n") #poistamalla hashtagin (#) print-funktion edestä, saat näkyviin tekstin
            bad += 1

            
        elif vs["compound"] == 0:
            #print(row, "neutraali\n") #poistamalla hashtagin (#) print-funktion edestä, saat näkyviin tekstin
            neutral += 1

            
        else:

            tuntematon += 1

yhteensa = good + bad + neutral   


print("pos: {} --- {:2.2%}".format(good, good / yhteensa))
print("neg: {} --- {:2.2%}".format(bad, bad / yhteensa))
print("neu: {} --- {:2.2%}".format(neutral, neutral / yhteensa))
print("Yhteensa:", yhteensa)
print("tuntemattomat:", tuntematon)
