#importa il modulo di python che gestisce i file csv e le operazioni su di essi
import csv
#inizializzo i contenitori delle righe come array vuoti
csList = [];
unList = [];

#apro in sola lettura l'origine dati in csv ed aggiungo le singole righe del file csv come coppia chiave-valore
with open("express.csv") as csData:
    reader = csv.DictReader(csData, delimiter=";")
    for row in reader:
            csList.append(row);
        
with open("unloco.csv") as unloco:
    reader = csv.DictReader(unloco, delimiter=";")
    for row in reader:
            unList.append(row);
#determino gli indici per il loop ed il controllo delle righe completate
compLines = 0;
ps = 0;

#apro il file di output in scrittura
with open("xpressOut.csv", 'w') as outfile:
#scrivo la prima riga con le intestazioni delle righe (che sono poi le chiavi delle righe che ho scritto negli array)
    outfile.write("Name;VAT Number;Address;City;State/Province;Post Code;Country;UNLOCO; \n");
    #ps (processed lines) viene utilizzato come indice
    while (ps < len(csList)):
        entry=csList[cs];
        #passo ogni UNLOCODE nell'array e controllo se nella riga del csv (entry) che sto esaminando ora c'è una corrispondenza and ed or, ovvero cerco se trova il country code E se trova il port name O il proper name. per essere sicuro ci sia la corrispondenza, trasformo il dato di entrambi i csv in uppercase
        for code in unList:
            if entry['Country'] == code['Country Code'] and (str.upper(entry['City']) == str.upper(code['Port Name']) or str.upper(entry['City']) == str.upper(code['Proper Name'])):
                #se trova una corrispondenza copia il codice unloco ed aumenta il contatore delle righe completate
                entry['UNLOCO'] = code['Code']
                compLines +=1;
        #compongo la stringa prendendo i valori dalle varie chiavi della riga, aggiungendo un ; tra ogni valore ed il newline alla fine di tutto
        strng = entry['Name'] + ';' + entry['VAT Number'] + ';' + entry['Address'] + ';' + entry['City'] + ';' + entry['State/Province'] + ';' + entry['Post Code'] + ';' + entry['Country'] + ';' + entry['UNLOCO'] + ';\n'
        #scrivo la stringa composta nel file di output ed aumento il contatore delle processed lines
        outfile.write(strng);
        ps +=1;
#alla fine stampo a video le linee processate e quelle completate
print("Total lines: " + str(len(csList)) + "; \n Completed lines: " + str(compLines))
