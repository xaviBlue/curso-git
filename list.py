[1,'Hello',1.34,True,[1,2,3]]

colors=['red','black','green']

numbers_list=list((1,2,3,4))
#print(numbers_list)

#r=list(range(1,11))
#print(r)

print(len(colors))
print(colors[-1])
print('green'in colors)
#print(colors)
#colors[1]='red'
#print(colors)

colors.extend(('violet','yellow'))
colors.extend(('pink','blueS'))
colors.insert(1,'orange')
colors.insert(len(colors),'bluesea')
print(colors)
colors.pop()
print(colors)
colors.remove('green')
print(colors)
#colors.clear()
#colors.sort()
#colors.sort(reverse=True)
print(colors.index('orange'))
print(colors.count('red'))
