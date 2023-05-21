import smtplib
import ssl
from email.message import EmailMessage
from providers.sms_gateways import sms_gateways
import logging
from typing import List

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def create_email_message(url: str) -> EmailMessage:
    msg = EmailMessage()
    msg.set_content(f"""This is an alert for {url}, which is available to book.""")
    return msg


def send_email(sender_email: str, receiver_list: List[str], password: str, msg: EmailMessage):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_list, msg.as_string())
            logging.info(f'Alert sent to {",".join(e for e in receiver_list)}')
    except smtplib.SMTPAuthenticationError:
        logging.error(
            f"Error authenticating. If you're using your email password, try creating an app password "
            f"https://support.google.com/accounts/answer/185833 and use that.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")


def send_alert(url: str, email: str, password: str, phone_provider_pairs: List[str]):
    logging.info("Sending alerts ...")
    sender_email = email
    receivers_list = [f'{e.split(":")[0]}@{sms_gateways[e.split(":")[1]]}' for e in phone_provider_pairs
                      if e.split(":")[1] in sms_gateways]
    msg = create_email_message(url)
    send_email(sender_email, receivers_list, password, msg)
