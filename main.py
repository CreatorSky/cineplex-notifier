import argparse
import logging
import sys

from utils.selenium_utils import has_booking_started
from utils.selenium_utils import has_new_booking_added
from utils.email_utils import send_alert
from providers.sms_gateways import sms_gateways

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

if __name__ == "__main__":
    operators = list(sms_gateways.keys())

    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument("--url", "-u", help="URL of the movie", required=True)
    parser.add_argument("--email", "-e", help="Email (Gmail)", required=True)
    parser.add_argument("--password", "-p", help="App Password (https://support.google.com/accounts/answer/185833)",
                        required=True)
    parser.add_argument("--phone", metavar="phone_provider",
                        help="Phone number and provider pairs separated by commas. "
                             "Format: number1:provider1,number2:provider2,...",
                        required=True)
    
    args = parser.parse_args()

    url = args.url
    email = args.email
    password = args.password
    phone_provider_pairs = args.phone.split(",")

    if not url.startswith("https://www.cineplex.com"):
        raise ValueError("Invalid URL provided. Please provide a valid Cineplex URL.")

    if any(":" not in pair for pair in phone_provider_pairs):
        raise ValueError("Invalid phone provider pair format. "
                         "Please provide phone number and provider pairs in the format "
                         "'number:provider' separated by commas.")

    if any(e.split(':')[1] not in sms_gateways for e in phone_provider_pairs):
        raise ValueError(f"Invalid provider(s){phone_provider_pairs}. Only the following providers are supported: {operators}")

    # if has_booking_started(url):
    #     send_alert(url, email, password, phone_provider_pairs)

    if has_new_booking_added(35397, 7420, "2023-07-26hbT00:00:00"):
        send_alert(url, email, password, phone_provider_pairs)
