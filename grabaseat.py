import requests

# API URL
api_url = "https://www.grabaseat.co.nz/api/v3/greenlight-deals"

# Make a GET request to fetch the data
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Start building the HTML table
    html_table = "|Origin|Destination|Price|Seats Available|Date From|Date To|Journey|\n"
    html_table += "|--|--|--|--|--|--|--|\n"

    # Loop through the deals to add rows to the table
    for deal in data['domesticDeals']:
        html_table += f"|{deal['originName']} ({deal['originIataCode']})|{deal['destinationName']} ({deal['destinationIataCode']})|{deal['currencySymbol']}{deal['price']}|{deal['seatCount']}|{deal['displayFromDate']}|{deal['displayToDate']}|\n"

    # Loop through the deals to add rows to the table
    for deal in data['internationalDeals']:
        html_table += f"|{deal['originName']} ({deal['originIataCode']})|{deal['destinationName']} ({deal['destinationIataCode']})|{deal['currencySymbol']}{deal['price']}|{deal['seatCount']}|{deal['displayFromDate']}|{deal['displayToDate']}|{deal['journeyType']}| {deal['serviceClass']}|\n"


    # Print the HTML table
    print(html_table)
else:
    print("Failed to fetch data from the API.")
