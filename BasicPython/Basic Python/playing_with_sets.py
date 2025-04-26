sets = []
with open("q2-input.txt", "r") as file:
    for line in file:
        sets.append(line)
sets_split = [set(x.strip().split(",")) for x in sets]
ans = set()
for i in range(len(sets_split)):
    ans = ans.union(sets_split[i])

print(len(ans))