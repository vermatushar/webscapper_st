import pandas as pd
import requests

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('./data/master.csv')

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Define the URL to send the JSON data
url = 'https://masystech.webhook.office.com/webhookb2/44498912-eabf-411f-9da8-34b10c20abf7@303f4a70-08fa-479e-9437-9fb716426a8f/IncomingWebhook/0f4f61b50d1044dd814530878f87ecbe/419cc1f3-eaec-4d94-8cbd-25e076276fa5'

# Set the headers for the request
headers = {'Content-Type': 'application/json'}

# Send a POST request with the JSON data as the payload
response = requests.post(url, headers=headers, json=json_data)

# Check the response status code
if response.status_code == 200:
    print('JSON data sent successfully!')
else:
    print('Error sending JSON data. Status code:', response.status_code)
