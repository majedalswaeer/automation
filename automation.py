import re
#_________________________________________________________________________
numbers_patterns = r"\d{3}[-.]\d{3}[-.]\d{3}[-.]\d{4}|\d{10}|\(\d{3}\)\d{3}[-.]\d{4}|[+]\d{1}[-.]\d{3}[-.]\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4}"
emails_pattern = r'[\w\-\.]+@+[\w\-\.]+\w'
#_________________________________________________________________________

with open("potential-contacts.txt" ,"r") as file:
    my_file = file.read()

#_________________________________________________________________________

my_emails = re.findall(emails_pattern , my_file)

my_emails.sort()
cleaned_emails = []
for email in my_emails:
    if email not in cleaned_emails:
        cleaned_emails.append(email)

with open("cleaned_emails.txt","w+") as file:
    for cleaned_email in cleaned_emails:
        file.write(f"{cleaned_email}\n")

#_________________________________________________________________________

phone_nums = re.findall(numbers_patterns,my_file)
phone_nums.sort()
modified_phone_num = []

for phone_num in phone_nums:
    if phone_num not in modified_phone_num:
        phone_num.replace("(","").replace(")","-").replace(".","-")
        modified_phone_num.append(phone_num)

with open("cleaned_numbers.txt","w+") as file:
    for a_num in modified_phone_num:
        a_num = a_num + '\n'
        file.write(a_num)

#_________________________________________________________________________

