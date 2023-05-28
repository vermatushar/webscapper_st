import pandas as pd
import requests

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('./data/master.csv')

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Define the URL to send the JSON data
url = '...'
# Set the headers for the request
headers = {'Content-Type': 'application/json'}

# Send a POST request with the JSON data as the payload
response = requests.post(url, headers=headers, json=json_data)

# Check the response status code
if response.status_code == 200:
    print('JSON data sent successfully!')
else:
    print('Error sending JSON data. Status code:', response.status_code)
