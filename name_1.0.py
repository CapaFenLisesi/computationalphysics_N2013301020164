a='    #    \n   # #   \n  #####  \n #     # \n#       #\n '

b='######## \n#       #\n######## \n#       #\n######## \n '

c='#########\n#        \n#        \n#        \n#########\n '

d='#######  \n#      # \n#       #\n#      # \n#######  \n '

e='#########\n#        \n#########\n#        \n#########\n '

f='#########\n#        \n#########\n#        \n#        \n '

g='#########\n#        \n#     ###\n#       #\n#########\n '

h='#       #\n#       #\n#########\n#       #\n#       #\n '
  
i='   ###   \n    #    \n    #    \n    #    \n   ###   \n '

j='  #####  \n    #    \n    #    \n #  #    \n ####    \n '

k='#       #\n#      # \n######   \n#      # \n#       #\n '
  
l='#        \n#        \n#        \n#        \n#########\n '

m='  #   #  \n # # # # \n#   #   #\n#   #   #\n#   #   #\n '

n='##      #\n# #     #\n#   #   #\n#     # #\n#      ##\n '

o='   ###   \n  #   #  \n #     # \n  #   #  \n   ###   \n '

p='#########\n#       #\n#########\n#        \n#        \n '

q='   ###   \n  #   #  \n #  #  # \n  #   #  \n   ###  #\n '

r='######## \n#       #\n######## \n#       #\n#       #\n '

s='   ###   \n  #      \n   ###   \n      #  \n   ###   \n '

t='#########\n    #    \n    #    \n    #    \n    #    \n '

u='#       #\n#       #\n#       #\n#       #\n ####### \n '

v='#       #\n #     # \n  #   #  \n   # #   \n    #    \n '

w='#       #\n#   #   #\n # # # # \n  #   #  \n  #   #  \n '

x='#       #\n #     # \n  #####  \n #     # \n#       #\n '

y='#       #\n #     # \n  #####  \n    #    \n    #    \n '

z='#########\n      #  \n    #    \n  #      \n#########\n '

#This is the input interface;
letter_1=str(raw_input("Pleas enter letter 1: "))
letter_2=str(raw_input("Pleas enter letter 2: "))
letter_3=str(raw_input("Pleas enter letter 3: "))

#This is the dictionary that links the input letters to the corresponding fonts;
mydict=dict()
mydict['a']=a
mydict['b']=b
mydict['c']=c
mydict['d']=d
mydict['e']=e
mydict['f']=f
mydict['g']=g
mydict['h']=h
mydict['i']=i
mydict['j']=j
mydict['k']=k
mydict['l']=l
mydict['m']=m
mydict['n']=n
mydict['o']=o
mydict['p']=p
mydict['q']=q
mydict['r']=r
mydict['s']=s
mydict['t']=t
mydict['u']=u
mydict['v']=v
mydict['w']=w
mydict['x']=x
mydict['y']=y
mydict['z']=z

#These statements store the corresponding fonts into string letterm_i;
letterm_1=mydict[letter_1]
letterm_2=mydict[letter_2]
letterm_3=mydict[letter_3]


row_1=[0]  #This list stores each row of the string of letter 1;
mark_1=[0] #This list stores each index of \n in the string of letter 1; 
index_1=0  #This is a looping index;
count_1=0  #This variable counts '\n' in the string of letter 1;

#This loop picks out each row of the string of letter 1, and stores it in row_1;
while index_1<len(letterm_1):
    if letterm_1[index_1]=='\n':
        count_1=count_1+1
        mark_1.append(index_1+1)
        keep_1=letterm_1[mark_1[count_1-1]:mark_1[count_1]]
        row_1.append(keep_1[:-1])
    index_1=index_1+1

row_2=[0]
mark_2=[0]
index_2=0
count_2=0
while index_2<len(letterm_2):
    if letterm_2[index_2]=='\n':
        count_2=count_2+1
        mark_2.append(index_2+1)
        keep_2=letterm_2[mark_2[count_2-1]:mark_2[count_2]]
        row_2.append(keep_2[:-1])
    index_2=index_2+1

row_3=[0]
mark_3=[0]
index_3=0
count_3=0
while index_3<len(letterm_3):
    if letterm_3[index_3]=='\n':
        count_3=count_3+1
        mark_3.append(index_3+1)
        keep_3=letterm_3[mark_3[count_3-1]:mark_3[count_3]]
        row_3.append(keep_3[:-1])
    index_3=index_3+1

row=[0] #I combine each row of letter a and letter b\n together, and store them in this list;
       
row.append(row_1[1]+'        '+row_2[1]+'        '+row_3[1])
row.append(row_1[2]+'        '+row_2[2]+'        '+row_3[2])
row.append(row_1[3]+'        '+row_2[3]+'        '+row_3[3])
row.append(row_1[4]+'        '+row_2[4]+'        '+row_3[4])
row.append(row_1[5]+'        '+row_2[5]+'        '+row_3[5])

#This loop prints the fonts;
i=1
while i<=5:
    print row[i]
    i=i+1
