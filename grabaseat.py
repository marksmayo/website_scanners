import requests

# API URL
api_url = "https://www.grabaseat.co.nz/api/v3/greenlight-deals"

# Make a GET request to fetch the data
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Initialize lists for collecting details
    from_airport = []
    to_airport = []
    start_date = []
    end_date = []

    # Start building the HTML table
    html_table = "|Origin|Destination|Price|Seats Available|Date From|Date To|Journey|\n"
    html_table += "|--|--|--|--|--|--|--|\n"

    # Loop through the domestic and international deals to add rows to the table and collect details
    for deal_type in ['domesticDeals', 'internationalDeals']:
        for deal in data[deal_type]:
            # Correct the date formatting from mmdd to ddmm
            start_month = deal['displayFromDate'][5:7]
            start_day = deal['displayFromDate'][8:10]
            end_month = deal['displayToDate'][5:7]
            end_day = deal['displayToDate'][8:10]
            # Build table rows and collect data
            html_table += f"|{deal['originName']} ({deal['originIataCode']})|{deal['destinationName']} ({deal['destinationIataCode']})|{deal['currencySymbol']}{deal['price']}|{deal['seatCount']}|{start_day}{start_month}|{end_day}{end_month}|{deal.get('journeyType', '')} {deal.get('serviceClass', '')}|\n"
            from_airport.append("'" + deal['originIataCode'] + "'")
            to_airport.append("'" + deal['destinationIataCode'] + "'")
            start_date.append("'" + start_day + start_month + "'")
            end_date.append("'" + end_day + end_month + "'")

    # Print the HTML table
    print(html_table)

    # Print the details in the specified format
    print("fromairport = [", ", ".join(from_airport), "]")
    print("toairport   = [", ", ".join(to_airport), "]")
    print("startdate   = [" + ",".join(start_date) + "]")
    print("enddate     = [" + ",".join(end_date) + "]")
else:
    print("Failed to fetch data from the API.")
