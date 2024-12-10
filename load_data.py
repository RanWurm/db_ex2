import os
import re
import subprocess
import time

lines = [
    "Oh, Ofir, the king of the database realm,",
    "With SQL queries, you steady the helm.",
    "Indexes bow as your commands take flight,",
    "Tables align to your every insight.",
    "",
    "From schemas to joins, you're always supreme,",
    "Ruling the data with logic and dream.",
    "No NULL can escape your sharp, watchful eye,",
    "Your queries, so perfect, make coders sigh.",
    "",
    "Constraints you enforce, relationships you bind,",
    "In the world of databases, you're one of a kind.",
    "So here's to Ofir, with wisdom so vast—",
    "The king of databases, long may he last!"
]



def natural_sort_key(s):
    """
    Sorts strings like q1.py, q2_3.py in the natural order.
    Extracts numeric portions to sort them numerically.
    """
    return [int(num) if num.isdigit() else num for num in re.split(r'(\d+)', s)]


def execute_scripts():
    # Get the current folder (the folder containing this script)
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Get all files in the current folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.py') and f.startswith('q')]

    # Sort files naturally
    sorted_files = sorted(files, key=natural_sort_key)

    # Execute each file in sorted order
    for file in sorted_files:
        file_path = os.path.join(folder_path, file)
        print(f"Executing {file_path}...")
        try:
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while executing {file_path}: {e}")



if __name__ == "__main__":
    for line in lines:
        print(line)
        time.sleep(2)
    execute_scripts()
