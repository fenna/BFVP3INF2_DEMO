#############
#strings
#############


#strings:

seq = 'GAATTCAACTG'
step = 2
startseq = 'AT'

print(seq)
print('a sequence has a start position and an end position [start:end]')
print('[{}:] makes: {}'.format(2,seq[2:]))
print('[{}:{}] makes: {}'.format(0,8,seq[0:8]))
print('[:{}] makes: {}'.format(8,seq[:8]))
print('[{}:{}] makes: {}'.format(-3,-1,seq[-3:-1]))
print('[{}:{}] makes: {}'.format(2,-2,seq[2:-2]))
print('[::{}] makes: {}'.format(step,seq[::step]))
print('[::{}] makes: {}'.format(step-1,seq[::step-1]))
print('[2::{}] makes: {}'.format(step-1,seq[2::step-1]))

#position of element where the string starts in the sequence

seq.strip()
print('the startposition of the startsequence AT is : {}'.format(seq.find(startseq)))

print('sequence:{}, length: {}, min: {}, max: {}'.format(seq, len(seq), min(seq), max(seq)))
print('number of A: {}'.format(seq.count('A')))
print('index of first A {}:'.format(seq.index('A')))

print(30*'*')


#strings kun je in combinatie met functies gebruiken
#len is functie lengte
#count is functie die aantal letters telt
#lower maakt lowercase

sequence = "AGTCTGAAGT"
print('sequence: {}'.format(sequence))
print('length of sequence {}'.format(len(sequence)))
print('G count:{}'.format(sequence.count('G')))
print('C count:{}'.format(sequence.count('G')))

gc = sequence.count('G') + sequence.count('C')
gc_percentage= gc *100 / len(sequence)
print('gc percentage:{}'.format(gc_percentage))


sequence = sequence.lower()

# ik kan door een string heen loopen
for letter in sequence:
    print(letter)

for letter in sequence:
    print(letter, end='')
print('\n')


valid_char = 'GATC'
for x in 'ACRGYWCCNA':
    if x in valid_char:
        print(x)
    else:
        print('invalid character: {}'.format(x))


#############
#Lists
#############
print(30*'*')

L1 = [] #empty list
for letter in 'ACRGYWCCNA':
    if letter in valid_char:
       L1.append(letter) #voeg letter aan  list toe

#print de gehele list
print('this is L1: {}'.format(L1))

# ik kan ook door de list heen loopen
for item in L1:
    print(item)


# ik kan ook door de list heen loopen met index
for index,item in enumerate(L1):
    print(index,item)

# ik kan lijsten sorteren
L2 = sorted(L1)
print(L2)

# ik kan een list omzetten naar een string
sequence = ''.join(L2)
print(sequence)

#############
#Dictionaries
#############
print(30*'*')

## amino acids weight
aaWeights = {'gly':75,
             'ala':89,
             'glu':100,
             'his':155,
             'pro':115,
             'tyr':181}

#veranderen
aaWeights['glu']=147
print(aaWeights)

#verwijderen
del aaWeights['gly']
print(aaWeights)

#toevoegen
aaWeights['gly']=75
print(aaWeights)

print('\n')


L3 = ['His','his','glu','tyr','Gly','Ala','pro']

#omzetten naar lower cases
for index,item in enumerate(L3):
    L3[index] = item.lower()

print('lower case list: {} '.format(L3))

#opzoeken gewicht (via dict) bij amino acid uit list
for aa in L3:
    weight = aaWeights[aa]
    print('amino acid weight of {} is {}'.format(aa, weight))

#sorteren op alfabeth
L4 = sorted(L3)
print('gesorteerd op alphabeth: {} '.format(L4))

#sorteren list op gewicht

def aaSorter(aa):
    return aaWeights[aa]

L5 = sorted(L3, key=aaSorter)
print('gesorteerd op gewicht: {} '.format(L5))

for aa in sorted(aaWeights.keys()):
    print(aa)

L6 = list(aaWeights.values())
print(L6)

for aa in sorted(aaWeights.values()):
    print(aa)

for aa in sorted(aaWeights.items()):
    print(aa)

print('\n')


enzymes = {
        "EcoRI":"GAATTC",
        "BamHI":"GGATCC",
        "XbaI":"TCTAGA",
        "BbsI":"GAAGAC",
        "HindIII":"AAGCTT",
        "AfeI":"AGCGCT",
        "PmlI":"CACGTG"
    }



#############
#Tuples
#############
print(30*'*')

#tuples are immutable
student_tuples = [('john', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'C', 10)]

print(student_tuples)
print(student_tuples[0])
print(student_tuples[1])
print(student_tuples[2])

#sorteren
print(sorted(student_tuples, key= lambda student: student[2]))
print(sorted(student_tuples, key= lambda student: student[1]))
print(sorted(student_tuples, key= lambda student: student[0]))
