"""
ID: yscript1
LANG: PYTHON3
TASK: namenum
"""

alpha_to_num = {
    'A':'2','B':'2','C':'2',
    'D':'3','E':'3','F':'3',
    'G':'4','H':'4','I':'4',
    'J':'5','K':'5','L':'5',
    'M':'6','N':'6','O':'6',
    'P':'7','R':'7','S':'7',
    'T':'8','U':'8','V':'8',
    'W':'9','X':'9','Y':'9'
}

def name_to_digi(name):
    s = ''
    for c in name:
        if c in alpha_to_num:
            s = s + alpha_to_num[c]
        else:
            return ''   # there may be 'Q' or 'Z' in name
    return s

with open('dict.txt') as f:
    lines = f.readlines()

digi_dict = {}
for line in lines:
    name = line.strip()
    digi = name_to_digi( name )
    if digi == '':
        continue
    if digi in digi_dict:
        digi_dict[digi].append(name)
    else:
        digi_dict[digi]=[name]

fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

digi = fin.readline().strip()
if digi in digi_dict:
    for name in digi_dict[digi]:
        fout.write(name + '\n')
else:
    fout.write('NONE\n')

fout.close()
# for k in digi_dict:
#     if len(digi_dict[k]) > 1:
#         print(k, digi_dict[k])
#print(digi_dict)
#print(digi_dict['4734'])
#fin = open ('test.in', 'r')
# fout = open ('test.out', 'w')
# x = list(map(int, fin.readline().split()))
# total = sum(x)
# fout.write (str(total) + '\n')
# fout.close()