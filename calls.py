import requests
import csv

# Define the API endpoint URL, date range, and API key
endpoint_url = "https://api.hubspot.com/crm/v3/objects/calls"
createdate = "2023-01-01T00:00:00.000Z"
closedate = "2023-01-31T23:59:59.999Z"
api_key = "pat-na1-0234b5dc-627f-4bad-887c-449363cdb8d9"

# Set the headers and parameters for the API request
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
params = {"created_after": createdate, "created_before": closedate, "limit": 100}

# Make the API request to extract the data
response = requests.get(endpoint_url, headers=headers, params=params)

# Check if the API request was successful
if response.status_code == 200:
    data = response.json()
    deals = data.get("results", [])

    # Get all unique property names and add createdAt and updatedAt
    properties = set().union(*(deal.get("properties", {}).keys() for deal in deals))
    properties.update(["createdAt", "updatedAt"])

    # Prepare the column names
    columns = ["id"] + list(properties)

    # Save the extracted data to a CSV file
    with open("calls_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)

        # Write the data rows
        for deal in deals:
            row = [deal.get("id")]
            row.extend(deal.get("properties", {}).get(column, deal.get(column, "")) for column in columns[1:])
            writer.writerow(row)

    print("Data extraction successful. The data has been saved to calls_data.csv.")
else:
    print("Failed to extract data. Please check the API endpoint and credentials.")
