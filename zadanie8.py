file_object = open("zwierzeta.txt", 'r')
zwierzeta = []
for l in file_object:
    zwierzeta.append(l.strip())
file_object.close()


while True:
decyzja = raw_input("Podaj decyzje")
if decyzja == 'y':
    nazwa_zwierzeta=raw_input("Podaj nazwe zwierzecia: ")
if n in zwierzeta:
    print("to znam")
else:
    zwierzeta.append(nazwa_zwierzeta)
    print ("tego nie znam, ale przy kolejnej probie bede znac")


print(zwierzeta)


#file = open("zwierzeta2.txt", 'w')
for z in zwierzeta:
    out.write(z+n)
#file.write(str(zwierzeta))
#file.close()
