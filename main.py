# Before to run this program this program run this commands:
# python3 -m venv venv
# pip3 install pandas
import pandas 
import datetime as dt
import os
import random
import smtplib

MY_EMAIL = "" #Put your email here
MY_PASSWORD = "" #Put your AppPassword (take a look in google account -> Security --> App Password)

def get_random_letter():
    """ This function loop inside the letter_templates folder and choose a random lettert.txt file """
    folder_path = 'letter_templates'
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    random_file = random.choice(files)
    return random_file

# Current year, month, day
now = dt.datetime.now()
current_month = now.month
current_day = now.day

#Get data from the birthdays.csv file
data_birthdays = pandas.read_csv("birthdays.csv")
dict_birthdays = data_birthdays.to_dict(orient="records")

for user in dict_birthdays:
    random_file = get_random_letter()
    #Check if today is the user's birthday
    if user["month"] == current_month and user["day"] == current_day:
        # Open a random letter file
        with open(f"letter_templates/{random_file}", 'r') as f:
            content = f.read()
            content = content.replace('[NAME]', user["name"])
        # Start the logic to send the eamil to the user
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=user["email"], 
                msg=f"Subject:Happy Birthday!\n\n{content}."
            )