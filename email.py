#!/usr/bin evn python3

"""A tiny email program to send spam to someone"""
__author__ = "mararp's program personalized for knmarvel"
import os
import sys
import smtplib

if sys.version_info[0] != 3:
    raise Exception("This program requires python3 interpreter")

EMAIL_ADDR = os.environ["EMAIL_ADDR"]
EMAIL_PASS = os.environ["EMAIL_PASS"]

# Setup a gmail app password to bypass 2FA process
# get the password into this program
# use the stmplib import to send email

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDR, EMAIL_PASS)

    # compose the email message
    subject = "email from python"
    body = "hiss hiss hiss."
    msg = f"Subject: {subject}\n\n{body}"

    # do actual send
    smtp.sendmail(EMAIL_ADDR, "kenzie.academy@mailinator.com", msg)
