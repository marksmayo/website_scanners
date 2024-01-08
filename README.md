# website_scanners
random tools for scraping/accessing websites

For The Market
 - go to a sample checkout page
 - enter a fake discount code, and open dev tools to see the network hit /fe/check
 - right click copy curl command
 - store in notepad so you have an access token and cookie.

 - next open themarket_discount_codes.py and replace YOUR_TOKEN and YOUR_COOKIE with the ones from your curl response.
 - run python themarket_discount_codes.py.

 It intentional executes slowly to not hit their rate limiting.
 Valid, current dated codes will be flagged as "VALID!" in the output.

For Dominos
 - run python dominos.py

it should produce output in table markdown format.
