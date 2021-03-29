def normalize(name):
    name = name[:1].upper()+name[1:].lower()   #为了避免名字为'',切取不到数据,首字母的index用[:1]而非[0]
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)