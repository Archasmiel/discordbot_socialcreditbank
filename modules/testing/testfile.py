

"""
db.truncate()
u = []
c = []
with open('../../data/savedusers.txt', 'r') as f:
    for i in f:
        u.append(i.rstrip())
with open('../../data/creditusers.txt', 'r') as f:
    for i in f:
        c.append(int(i.rstrip()))
print(u)
print(c)
for i in range(len(u)):
    insert(u[i], c[i])
# update('<@!458555990162276352>', -9999901)
"""
print(get_usrcredit('<@!458555990162276352>'))
print(db.all())
