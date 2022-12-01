lines = []
total = 0

with open("22/day1/input.txt", "r") as f:
    for line in f:
        if line.strip("\n") == "":
            lines.append(total)
            total = 0
        else:
           total += int(line.strip("\n"))

print(max(lines))