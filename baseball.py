import sys
positions=[]

def assign(index, assignedSoFar):
    if index==10:
        print(True)
        sys.exit(0)
    for p in positions[index]:
        if p not in assignedSoFar:
            assign(index+1,assignedSoFar | {p})
for i in range(10):
    parts=input().split(":")
    positions.append(parts[1].replace(' ','').split(','))

assign(0,set())
print(False)