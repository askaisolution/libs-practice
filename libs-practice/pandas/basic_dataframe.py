import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Get basic info
print("\nInfo:")
print(df.info())
