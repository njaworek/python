import math


IMIE= 'Natalia'
ilosc = [3, 1, 1, 2, 5, 6, 8]
ilosc2 = [3, 1, 1, 2, 5, 6, 8]
b = 1
c = 2
d = 5
e = 1
taniec = ['tango', 'rumba' , 'samba']
wynik = c+d
koniec = 'mnozenie wynosi'
marka = 'BMW'
poczatek = 'Moja ulubona marka to '

marka_h = marka.lower()
pojemnosc =  1.3

#sortowanie pliku
for i in ilosc:
    ilosc.sort()
print(ilosc)

#wyswietlanie tablicy
for t in taniec:
    print(t)



print(taniec[1])

#przypisywanie indexu do tablicy
for idx in range(len(taniec) ):
    print ("index: " + str(idx) + taniec[idx]);

#wyswietlanie
print ('Hello World!' +' ' +IMIE)
print "%s %d" % (koniec, wynik)
print ( poczatek + marka + ' i auto jest ' + str(d) + ' drzwiowe')
print (marka_h)
print (marka, pojemnosc * 2)
print ('Moj kot ma ' +str(c)+ 'lata ostatnio zjadl duzo i zamiast wazyc ' +str(d)+ ' kilo, wazy ' +str(d*2) )




#wyciaganie danych ze slownika
#def definiuje funkcje
def print_dict(p):
    for key, value in p.iteritems():
        print("{0}:{1}".format(key, value))
#    for key in pracownik:
#        print("{0}:{1}".format(key, pracownik[key]))


# tu mamy podwojne _ podkreslenia jesli wejdzie do main to ma wykonac funkcje
if __name__ == "__main__":
#slowniki peirwsze key potem value
    pracownik = {'name': 'kowalski', 'ID' : '32432423' , 'user' : 'akowalski'}

    print_dict(pracownik)
    print_dict(pracownik)




# otwieranie pliku i dopisywanie do niego w-write r-read
file_object  = open("produkty.txt", "w")
file_object.write("Hello World")
file_object.close()
