import operator
a={1:3,4:5,6:7,0:0,5:6,1:2}
b=sorted(a.items(), key=operator.itemgetter(1))
print('ascending order:',b)
c=dict(sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order:',c)