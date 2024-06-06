class Building():
    total = 0
    def __init__(self):
        Building.total+=1

print(Building.total)

for i in range(40):
    a = Building()
    print(a.total)

print(Building.total)