from tqdm import tqdm
from datetime import datetime
import json
import subprocess
import time


def test_coupon_code(code):
    curl_command = [
        "curl",
        "https://themarket.com/api/coupon/fe/check",
        "-X",
        "POST",
        "-H",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "-H",
        "Accept: application/json",
        "-H",
        "Accept-Language: en-GB,en;q=0.5",
        "-H",
        "Accept-Encoding: gzip, deflate, br",
        "-H",
        "Referer: https://themarket.com/nz/checkout",
        "-H",
        "Access-Token: YOUR_TOKEN",
        "-H",
        "Content-Type: application/json",
        "-H",
        "Origin: https://themarket.com",
        "-H",
        "DNT: 1",
        "-H",
        "Connection: keep-alive",
        "-H",
        "Cookie: YOUR_COOKIE",
        "-H",
        "Sec-Fetch-Dest: empty",
        "-H",
        "Sec-Fetch-Mode: cors",
        "-H",
        "Sec-Fetch-Site: same-origin",
        "-H",
        "TE: trailers",
        "--data-raw",
        f'{{"CultureCode":"EN","CouponReference":"{code}","MerchantId":0}}',
    ]

    process = subprocess.Popen(
        curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return stdout.decode("utf-8")
    else:
        # Handling the case if curl command itself fails.
        return f"Error: {stderr.decode('utf-8')}"


codes = [
    "5XMAS",
    "10XMAS",
    "15XMAS",
    "5LABOUR",
    "10LABOUR",
    "15LABOUR",
    "APRCLUB",
    "AUGCLUB",
    "AUTUMN5",
    "AUTUMN10",
    "BXD5",
    "CLUB5",
    "CLUB5DEC",
    "CLUB10",
    "CLUB10A",
    "CLUB10B",
    "CLUB15",
    "CLUBJOY",
    "CLUBPERKS",
    "CLUBRMHC",
    "CLUBSAVE",
    "CLUBSAVE5",
    "CLUBSAVE10",
    "CLUBSAVER",
    "DECCLUB",
    "DONE5",
    "DONE10",
    "EASTER5",
    "EASTER10",
    "EXCLU10",
    "EXCLUSIVE10",
    "FEBCLUB",
    "FEST",
    "GET5",
    "JANCLUB",
    "JUBILEE5",
    "JUBILEE8",
    "JUBILEE10",
    "JULCLUB",
    "JUNCLUB",
    "KIWI5",
    "KIWI10",
    "LUCKY13",
    "MARCLUB",
    "MAYCLUB",
    "MC5",
    "MC10",
    "MC15",
    "MCLUB5",
    "MCLUB10",
    "MCLUB11",
    "MCLUB15",
    "MCLUB20",
    "MCLUB30",
    "NOVCLUB",
    "NYMC10",
    "OCTCLUB",
    "SASDEC23",
    "SAVE5",
    "SAVE10",
    "SAVING5",
    "SAVING10",
    "SAVING20",
    "SAVING30",
    "SAVVY10",
    "SEPCLUB",
    "SORTED5",
    "SORTED10",
    "SORTED15",
    "SPRING5",
    "SPRING10",
    "SUMMER5",
    "SUMMER10",
    "WEEKEND5",
    "WEEKEND10",
    "WKND5",
    "WKND10",
]  # Replace with your list of codes

print("Number of codes to check: " + str(len(codes)))

for code in tqdm(codes):
    response = test_coupon_code(code)
    response_data = json.loads(response)
    time.sleep(30)
    if "AppCode" in response_data:
        print(f"Code: {code}")
    else:
        available_from = response_data.get("AvailableFrom", "N/A")
        available_to = response_data.get("AvailableTo", "N/A")
        coupon_amount = response_data.get("CouponAmount", "N/A")
        coupon_percent = response_data.get("CouponPercent", "N/A")
        coupon_reference = response_data.get("CouponReference", "N/A")

        if available_to != "N/A":
            available_to_date = datetime.strptime(available_to, "%Y-%m-%dT%H:%M:%S.%f")
            if available_to_date.date() > datetime.now().date():
                valid_status = " - VALID!"
            else:
                valid_status = ""
        else:
            valid_status = ""
        print(
            f"Code: {code} - Available From: {available_from}, Available To: {available_to}, Coupon Amount: {coupon_amount}, Coupon Percent: {coupon_percent}, Coupon Reference: {coupon_reference}{valid_status}"
        )
