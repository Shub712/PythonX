
cats = []

while True:
    print("Enter the name of cat " + str(len(cats)+1)+
          " (or Enter Nothing to stop): ") 
    
    name = input()
    if name == "":
        break
    cats.append(name) # list concatenation
print("cats name are : ")

for name in cats:
    print(' ' + name)
    