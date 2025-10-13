import csv
import random
from datetime import datetime, timedelta

# Original rows
rows = [
    ["2/13/2021","5:56 AM","1.57","Texas","Pearson","6","15.38","24.27","3"],
    ["2/9/2021","7:15 AM","1.38","New York","Crest Line","3","10.8","20.91","0"],
    ["10/27/2022","1:27 PM","5.85","Wisconsin","Vahlen","2","13.69","25.68","0"],
    ["5/8/2022","11:07 AM","4.07","Texas","Moulton","7","10.22","26.33","1"],
    ["1/28/2022","7:33 AM","1.31","Missouri","Arizona","5","11.63","25.96","1"]
]

states = ["Texas","New York","Wisconsin","Missouri","California","Florida","Illinois","Ohio","Georgia","Arizona","Colorado","Washington"]
streets = ["Maple","Oakridge","Bayview","Elm","Hawthorne","Riverside","Grand","Pine","Cedar","Highland","Park","Lincoln","Walnut","Birch","Willow","Chestnut","Adams","Jefferson","Madison","Monroe"]
time_formats = ["%I:%M %p"]

def random_time():
    hour = random.randint(5, 20)
    minute = random.choice([0,5,10,15,20,25,30,35,40,45,50,55])
    dt = datetime(2021,1,1,hour,minute)
    return dt.strftime("%-I:%M %p") if hasattr(dt, "strftime") else dt.strftime("%I:%M %p")

def random_date(start_year=2019, end_year=2023):
    start = datetime(start_year,1,1)
    end = datetime(end_year,12,31)
    delta = end - start
    rand_days = random.randint(0, delta.days)
    d = start + timedelta(days=rand_days)
    return d.strftime("%-m/%-d/%Y")

def gen_row():
    date = random_date(2019, 2023)
    time_start = random_time()
    duration_hours = round(random.uniform(0.5, 6.0), 2)
    state = random.choice(states)
    starting_street_name = random.choice(streets)
    group_size = random.randint(1, 8)
    avg_speed_mph = round(random.uniform(8.0, 16.0), 2)
    # Ensure top speed > avg speed by 3-15 mph, cap at ~35
    top_speed_mph = round(min(avg_speed_mph + random.uniform(3.0, 15.0), 40.0), 2)
    rest_breaks = random.choices([0,1,2,3,4], weights=[50,25,15,7,3])[0]
    return [date, time_start, f"{duration_hours:.2f}", state, starting_street_name, str(group_size),
            f"{avg_speed_mph:.2f}", f"{top_speed_mph:.2f}", str(rest_breaks)]

# Generate 195 additional rows
for _ in range(195):
    rows.append(gen_row())

# Write CSV
header = ["date","time_start","duration_hours","state","starting_street_name","group_size","avg_speed_mph","top_speed_mph","rest_breaks"]
output_filename = "expanded_data_200_rows.csv"
with open(output_filename, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {output_filename}")