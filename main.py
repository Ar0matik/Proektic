
with open('example_100kb.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    data = [lines[i].split(',') for i in range(1, len(lines), 2)]
    rows = [data[i][2] for i in range(len(data))]
def writeik(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        for row in data:
            file.write(','.join(row) + '\n')



domain_counts = {}
for i in rows:
    domain = i[i.find('@')+1:]
    if domain in domain_counts:
        domain_counts[domain] += 1
    else:
        domain_counts[domain] = 1


new_rows = [['domain', 'count']] + [[domain, str(count)] for domain, count in sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)]


writeik('finalchik.csv', new_rows)
