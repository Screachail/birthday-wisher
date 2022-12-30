##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import smtplib
import ssl

# 1. Update the birthdays.csv
birthdays_dict = {
    'name': ['Kacper', 'Karolina', 'Kamil', 'Karol'],
    'email': ['bobrowski_stefan@yahoo.com', 'bobrowski_stefan@yahoo.com',
              'bobrowski_stefan@yahoo.com', 'bobrowski_stefan@yahoo.com'],
    'year': [2022, 2022, 2022, 2022],
    'month': [10, 10, 11, 10],
    'day': [6, 7, 8, 7]
}

df = pd.DataFrame(birthdays_dict)
df.to_csv("birthdays.csv", index=False)

birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv


now = dt.datetime.now()
now_tuple = (now.month, now.day)



birthdays_updated = {birthdays["name"]: (birthdays["month"], birthdays["day"]) for (index, birthdays) in birthdays.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

print(birthdays_updated)
print(now_tuple)

# split dictionary into keys and values
keys = []
values = []
for i in birthdays_updated:
    keys.append(i)
    values.append(birthdays_updated[i])
# printing keys and values separately
print("keys : ", str(keys))
print("values : ", str(values))

x = 0
for data in range(len(keys)):
    if now_tuple == values[x]:
        name = keys[x]
        letter_number = random.randint(1, 3)
        letter_source = f"letter_templates/letter_{letter_number}.txt"
        with open(letter_source) as letter:
            letter_content = letter.readlines()
            new_content = ""
            for line in letter_content:
                line = line.replace("[NAME]", f"{name}")
                new_content += line
            print(new_content)
        # 4. Send the letter generated in step 3 to that person's email address.

            ctx = ssl.create_default_context()
            password = "faxxkncxdwovlzqf"  # Your app password goes here
            sender = "bobrowski.stefan.87@gmail.com"  # Your e-mail address
            receiver = "bobrowski_stefan@yahoo.com"  # Recipient's address
            message = f"Subject: Happy Birthday! \n{new_content}"
            with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
        x += 1
    else:
        x += 1