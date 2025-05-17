import csv
import os

# File paths
input_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "financial_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
previous_value = None
changes = []
months = []

greatest_increase = ["", float('-inf')]
greatest_decrease = ["", float('inf')]

# Read CSV file
with open(input_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip header

    for row in reader:
        date = row[0]
        current_value = int(row[1])
        total_months += 1
        net_total += current_value

        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)
            months.append(date)

            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        previous_value = current_value

# Calculate average change
average_change = sum(changes) / len(changes)

# Prepare output
output_lines = []
output_lines.append("Financial Analysis")
output_lines.append("----------------------------")
output_lines.append(f"Total Months: {total_months}")
output_lines.append(f"Total: ${net_total}")
output_lines.append(f"Average Change: ${average_change:.2f}")
output_lines.append(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
output_lines.append(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print to terminal
for line in output_lines:
    print(line)

# Write to output text file
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as file:
    for line in output_lines:
        file.write(line + "\n")
