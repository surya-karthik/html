phrase = "Don't Panic!"

Plist = list (phrase)

print (phrase)
print(Plist)

for i in range(4):
 Plist.pop()
 
Plist.pop(0)
Plist.remove("'")

Plist.extend([Plist.pop(), Plist.pop()])

Plist.insert(2, Plist.pop(3))



new_phrase = ''.join(Plist)
print(Plist)
print(new_phrase)

