camelot_lines = []
with open('camelot.txt','r') as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)
