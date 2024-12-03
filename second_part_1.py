def is_safe(report):
    # Check if all differences are between 1 and 3
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    # Check if the report is strictly increasing or decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing

def count_safe_reports(file_path):
    safe_count = 0

    # Read and process the file
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1

    return safe_count

# Input file path
file_path = "second.txt"  # Replace with the path to your file

# Count and print the number of safe reports
safe_reports = count_safe_reports(file_path)
print(f"Number of Safe Reports: {safe_reports}")
