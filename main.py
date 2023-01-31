##################### Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# print(message)
now = dt.datetime.now()
now_day = now.day
now_month = now.month
today = (now_day, now_day)
# birthdaydic = {
#     (birthday_month, birthday_day): datarow
# }
# print(birthdaydic)

data = pandas.read_csv("birthdays.csv")
new_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(new_dic)

if today in new_dic:
    message = f"letter_templates/letter_{random.randint(1,3)}.text"
    with open(message) as letter:
        birthday_person = new_dic[today]
        content = letter.read()
        content = content.replace("[Name]", birthday_person["name"])

# print(test1)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="shahadM20@yahoo.com", password="xXsiki4763u")
        connection.sendmail(
            from_addr= "shahadM20@yahoo.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! \n\n\n {content} ;)"
        )

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



