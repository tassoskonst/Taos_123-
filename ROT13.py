alphabet="abcdefghijklmnopqrstuvwxyz"
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Arithmoi="0123456789"
alph=list(alphabet)
ALPH=list(ALPHABET)
Ar=list(Arithmoi)
keimeno=raw_input("Pliktrologiste to keimeno sas: ")
keim=list(keimeno)
keno=" "
ken=list(keno)
output=""
for i in range(len(keim)):
    if keim[i] in alph:
        for j in range(len(alph)):
            if keim[i]==alph[j]:
                if j + 13 > 25:
                    output=output + alph[j+13-26]
                else:
                    output=output + alph[j+13]
                    
    elif keim[i] in ALPH:
        for j in range(len(ALPH)):
            if keim[i]==ALPH[j]:
                if j + 13 > 25:
                    output=output + ALPH[j+13-26]
                else:
                    output=output + ALPH[j+13]

    elif keim[i] in Ar:
        for j in range(len(Ar)):
            if keim[i]==Ar[j]:
                output=output + Ar[j]

    elif keim[i] in ken:
        output= output + ken[0]



print output			