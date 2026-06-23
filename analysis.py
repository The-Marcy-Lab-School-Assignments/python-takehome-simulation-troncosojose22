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


borough_open_counts = {}
borough_closed_counts = {}
for row in rows:
    borough = row['borough']
    if borough not in borough_open_counts:
        borough_open_counts[borough] = 0
        borough_closed_counts[borough] = 0
    if row['resolution_status'] == 'Open':
        borough_open_counts[borough] += 1
    else:
        borough_closed_counts[borough] += 1

sorted_complaints = sorted(complaint_counts.items(), key=lambda x: x[1], reverse=True)

most_open_borough = max(borough_open_counts, key=lambda k: borough_open_counts[k])
most_open_count = borough_open_counts[most_open_borough]

top_boroughs = sorted(borough_counts.items(), key=lambda x: (-x[1], x[0]))[:3]

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_count}\n")
    f.write("\n")
    f.write(f"Most common complaint type: {most_common} ({most_common_count} requests)\n")
    f.write("\n")
    f.write("Requests per borough:\n")
    for borough, count in sorted_boroughs:
        f.write(f"- {borough}: {count}\n")
    f.write("\n")
    f.write("Requests by complaint type:\n")
    for complaint, count in sorted_complaints:
        f.write(f"- {complaint}: {count}\n")
    f.write("\n")
    f.write(f"Borough with most open requests: {most_open_borough} ({most_open_count} open)\n")
    f.write("\n")
    f.write("Closure rate by borough:\n")
    for borough, total in sorted_boroughs:
        closed = borough_closed_counts[borough]
        rate = round(closed / total * 100, 1)
        f.write(f"- {borough}: {rate}%\n")
    f.write("\n")
    f.write("Top 3 boroughs by total requests:\n")
    for i, (borough, count) in enumerate(top_boroughs, start=1):
        f.write(f"{i}. {borough} ({count} requests)\n")

print("Output saved to output.txt")