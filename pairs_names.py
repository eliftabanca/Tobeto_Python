#This bot makes grouping easier for pairs in the lesson.
#It puts 5 different people for each pair, creating a total of 6 pairs.
import random
def get_names():
    return ['Abdullah KESKIN', 'Ahmet Suat Tanıs', 'Anıl Aytac Ayyıldız','Asiye Kevser Yılmaz','Dilara Jiyan Eser',
              'Elif Busra Tabanca', 'Emine Çoskun','Emir YILMAZ', 'Gül Karamahmutoglu', 'Gulen Yesilyurt', 'Halit Eren',
              'Hanife Cennet ALKAN','Hulya Gökdemir', 'Mehmet Turgut Aksel', 'Merve Koyunyerli', 'Meryem Ozgun',
              'Muhsine TASCI', 'Nesibe Kaya', 'Oguzhan Selmi', 'Onur Bülgü' 'Özlem Akman', 'Recep Kızıl', 'Rumeysa Coskun',
              'Salim İla','Sevda Yılmaz', 'Süleyman Kulaksız','Tuba Bezek', 'Yasemin Karasakal Coban', 'Zehra Senturk',
              'Zekine Zeliha Koc Demirci']


x = 1
for i in range(6):
    pairs = random.sample(get_names(), 5)
    print(f"{x}. Pair: {','.join(pairs)} ")
    x += 1
    for people in pairs:
        get_names().remove(people)
