import csv
from pathlib import Path

def save_to_csv(weight, height, bmi):
    file_path = Path("data/bmi_log.csv")
    file_path.parent.mkdir(exist_ok = True)
    with file_path.open("a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([weight,height,bmi])