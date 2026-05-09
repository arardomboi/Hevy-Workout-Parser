#imports
import csv
from datetime import datetime

#class
class ExerciseEntry:
    def __init__(self, date, exercise):
        self.date = date
        self.exercise = exercise
        self.weight_reps = []

    def add_set(self, weight, reps):
        self.weight_reps.append([weight, reps])

#helpers
def parse_date(value):
    if not value:
        return None
    
    # Remove time if present via 'T' or space for ISO format check
    date_str = value.split('T')[0].split(' ')[0]

    # 1. Try ISO format (YYYY-MM-DD) -> DD/MM/YYYY
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        pass

    # 2. Updated: Try 'Sep 17, 2024, 4:39 PM' format -> DD/MM/YYYY
    # Use %b for abbreviated months (Sep) instead of %B (September)
    try:
        return datetime.strptime(value, '%b %d, %Y, %I:%M %p').strftime('%d/%m/%Y')
    except ValueError:
        pass

    return value  # Fallback

def parse_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def parse_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

#functions
def readCSV(file):
    print(file)
    grouped = {}
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = parse_date(row.get('start_time', ''))
            exercise = row.get('exercise_title', '').strip()
            weight = parse_float(row.get('weight_kg', ''))
            reps = parse_int(row.get('reps', ''))

            if not exercise:
                continue

            key = (date, exercise)
            if key not in grouped:
                grouped[key] = ExerciseEntry(date, exercise)
            grouped[key].add_set(weight, reps)
    
    endData = groupData(list(grouped.values()))
    return endData

def groupData(entries):
    # Dictionary to hold { "Exercise Name": [ExerciseEntry, ExerciseEntry, ...] }
    grouped_by_exercise = {}

    for entry in entries:
        if entry.exercise not in grouped_by_exercise:
            grouped_by_exercise[entry.exercise] = []
        grouped_by_exercise[entry.exercise].append(entry)

    # Sort the entries within each exercise by actual date
    for exercise in grouped_by_exercise:
        grouped_by_exercise[exercise].sort(
            key=lambda x: datetime.strptime(x.date, '%d/%m/%Y')
        )

    return grouped_by_exercise

if __name__ == '__main__':
    tempFile = 'workouts.csv'
    # data is now a dictionary: { exercise_name: [ExerciseEntry, ...] }
    data = readCSV(tempFile)

    # To print it out:
    for exercise_name, entries in data.items():
        print(f"\n--- {exercise_name} ---")
        for e in entries:
            print(f"{e.date}: {e.weight_reps}")