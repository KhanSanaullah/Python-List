Number =["First","Second","Third","Fourth"]
print('No'in Number)

for index,item in enumerate(Number):
    print(index,item)

for item in Number:
    print(item)
print('First Index of List'+Number[0])
print('Last Index of List '+Number[-1])
Number.append('Fifth')
print('')
print(Number[2:-1])

Number.insert(0,'Zero')

print(Number)

List2 ={'Math', 'Art'}

#Add 2nd List into first
Number.extend(List2)

print(Number)

Number.remove('First')

#pop remove and then return the last item
Popitem = Number.pop()

#Sort a List

Number.sort()
print(Popitem)
print(Number)

NoList =[1,2,5,6]
print(min(NoList))

print(sum(NoList))