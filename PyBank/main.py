import pandas as pd

# Load the data
df = pd.read_csv('Resources/budget_data.csv')

# Open the text file to write results
with open('analysis/analysis.txt', 'w') as file:
    # Create a function to print to both console and file
    def print_to_file(message):
        print(message)  # Print to console
        file.write(message + '\n')  # Write to file

    # Print header to both console and file
    print_to_file("Financial Analysis")
    print_to_file("----------------------------\n")

    # Total number of months
    df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')
    num_months = df['Date'].nunique()
    print_to_file(f"Total number of months: {num_months}")

    # Net total amount of Profit/Losses
    net_total = df['Profit/Losses'].sum()
    print_to_file(f"Net total amount of Profit/Losses over the entire period: ${net_total}")

    # Average change in Profit/Losses
    df['Change in Profit/Losses'] = df['Profit/Losses'].diff()
    average_change = df['Change in Profit/Losses'].mean()
    print_to_file(f"Average change in Profit/Losses over the entire period: ${average_change:.2f}")

    # Greatest increase in profits
    max_increase = df['Change in Profit/Losses'].max()
    max_increase_date = df.loc[df['Change in Profit/Losses'] == max_increase, 'Date'].iloc[0]
    print_to_file(f"Greatest increase in profits: ${max_increase} on {max_increase_date.strftime('%b-%y')}")

    # Greatest decrease in profits
    max_decrease = df['Change in Profit/Losses'].min()
    max_decrease_date = df.loc[df['Change in Profit/Losses'] == max_decrease, 'Date'].iloc[0]
    print_to_file(f"Greatest decrease in profits: ${max_decrease} on {max_decrease_date.strftime('%b-%y')}")