Number =["First","Second","Third","Fourth"]

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


print(Popitem)
print(Number)