import requests
import time


source = "Hi!\n\n"
for char in source:
    print(char, end='')
    time.sleep(0.2)


site = input("Enter the website address:")
files = input("Enter the file name:")

response = requests.get(site).text

with open(f"{files}.html", "w", encoding="utf-8") as file:
    file.write(response)

print('The file was saved successfully')