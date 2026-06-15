import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_count = 0
for row in rows:
    if row['resolution_status'] == 'Open':
        open_count += 1

complaint_counts = {}
for row in rows:
    complaint = row['complaint_type']
    if complaint not in complaint_counts:
        complaint_counts[complaint] = 0
    complaint_counts[complaint] += 1

most_common = max(complaint_counts, key=lambda k: complaint_counts[k])
most_common_count = complaint_counts[most_common]

borough_counts = {}
for row in rows:
    borough = row['borough']
    if borough not in borough_counts:
        borough_counts[borough] = 0
    borough_counts[borough] += 1

sorted_boroughs = sorted(borough_counts.items())

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_count}\n")
    f.write("\n")
    f.write(f"Most common complaint type: {most_common} ({most_common_count} requests)\n")
    f.write("\n")
    f.write("Requests per borough:\n")
    for borough, count in sorted_boroughs:
        f.write(f"- {borough}: {count}\n")

print("Output saved to output.txt")