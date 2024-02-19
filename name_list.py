with open('names.txt', 'w') as file:
    name_list = [
        'Abdullah KESKIN', 'Ahmet Suat Tanıs', 'Anıl Aytac Ayyıldız','Asiye Kevser Yılmaz','Dilara Jiyan Eser', 'Elif Busra Tabanca', 
        'Emine Çoskun','Emir YILMAZ', 'Gül Karamahmutoglu', 'Gulen Yesilyurt', 'Halit Eren', 'Hanife Cennet ALKAN','Hulya Gökdemir', 
        'Mehmet Turgut Aksel','Merve Koyunyerli', 'Meryem Ozgun', 'Muhsine TASCI', 'Nesibe Kaya', 'Oguzhan Selmi', 'Onur Bülgü' 'Özlem Akman',
        'Recep Kızıl', 'Rumeysa Coskun','Salim İla','Sevda Yılmaz', 'Süleyman Kulaksız','Tuba Bezek', 'Yasemin Karasakal Coban', 'Zehra Senturk', 'Zekine Zeliha Koc Demirci'
    ]
    
    for name in name_list:
        file.write(f"{name}\n")