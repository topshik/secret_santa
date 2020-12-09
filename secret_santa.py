import smtplib
from email.message import EmailMessage

import numpy as np
import pandas as pd

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"  # yep, there must be smth more secure
LETTER_SUBJECT = "Secret Santa 20XX"


class Person:
    def __init__(self, name, email, wishlist, allergies):
        self.name = name
        self.email = email
        self.wishlist = wishlist
        self.allergies = allergies


# check that no one has oneself as a recipient
def check_permutation(people, people_permutation):
    for i in range(len(people)):
        if people[i].name == people_permutation[i].name:
            return True

    return False


def send_message(email_to, content):
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["Subject"] = LETTER_SUBJECT
    msg["To"] = email_to
    msg.set_content(content)
    server.send_message(msg)


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(EMAIL, PASSWORD)

source = pd.read_csv("data.csv", encoding="utf-8", sep=",", header=None)
source = source.fillna("None")
people = [Person(source.iloc[i, 1],
                 source.iloc[i, 2],
                 source.iloc[i, 3],
                 source.iloc[i, 4]) for i in range(1, source.shape[0])]

recipients = np.random.permutation(people)
while check_permutation(people, recipients):
    recipients = np.random.permutation(people)

# send letters to everyone
for i in range(len(people)):
    content = f"Hi!\n\nYour recipient is {recipients[i].name}.\n\n" \
              f"You can take into account their wishes: {recipients[i].wishlist}.\n\n " \
              f"Please pay attention if person has any allergies: {recipients[i].allergies}."
    footer = "\n\nKind regards,\nSecret Santa Scheduler"
    # print(content + footer + "\n\n\n\n\n\n\n")
    send_message(people[i].email, content + footer)

server.quit()
