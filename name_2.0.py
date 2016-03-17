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
word=str(raw_input("Please enter your name: "))

#Following codes store the letters of 'word'
loop_1=0 #looping index
word_list=[] #This list stores the letters
while loop_1<len(word):
    word_list.append(word[loop_1])
    loop_1=loop_1+1

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

#Following codes links elements in word_list to corresponding strings
loop_2=0    #looping index
string_list=[]    #This list stores strings
while loop_2<len(word):
    string_list.append(mydict[word_list[loop_2]])
    loop_2=loop_2+1

#The following function disintegrate a string
def disintegrate(string):
    row=[0]    
    mark=[0]
    index=0
    count=0
    while index<len(string):
        if string[index]=='\n':
            count=count+1
            mark.append(index+1)
            keep=string[mark[count-1]:mark[count]]  
            row.append(keep[:-1])
        index=index+1
    row.remove(0)
    return row

#The following codes disintegrate elements in string_list
loop_3=0
row=[]
while loop_3<len(word):
    row.append(disintegrate(string_list[loop_3]))
    loop_3=loop_3+1


#The following function combines same row of the strings together
def combination(liz,rownum):
    loop=0
    combrow=''
    while loop<len(liz):
        combrow=combrow+' '+liz[loop][rownum]
        loop=loop+1
    return combrow

whole_row=[]
loop_4=0
while loop_4<5:
    whole_row.append(combination(row,loop_4))
    print whole_row[loop_4]
    loop_4=loop_4+1

