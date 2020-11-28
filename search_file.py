import os

query = input("Enter query>>> ")

results = []

num = 1

for root, dirs, files in os.walk('.'):
    for i in files:
        if query in str(i):
            t = os.path.join(root, i)
            results.append(t)
            print(num,': '+t)
            num += 1

if results != []:
    want = int(input("Make a selection>>> "))
    os.startfile(results[want-1])
else:
    input("No results found :(")