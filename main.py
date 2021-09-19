from handler import *
from pprint import pprint
from siever import sieve
import os

contacts = ionize('contacts from isaacugochukwu007@gmail.com.txt')
c_m_contacts = {}
to_be_popped = []
filed = 'contacts from isaacugochukwu007@gmail.com.txt'
for num, details in contacts.items():

    if 'C.M' in details[3]:
        c_m_contacts[num] = details
        to_be_popped.append(num)

print(c_m_contacts)
print(len(to_be_popped))
print(to_be_popped)

with open('c_m_contacts.vcf', 'w') as file:
    for num, details in c_m_contacts.items():
        for detail in details:
            file.write(f'{detail}')

for inmates in to_be_popped:
    contacts.pop(inmates)

with open('clean_contacts.vcf', 'w') as file:
    for num, details in contacts.items():
        for detail in details:
            file.write(f'{detail}')


filter_files = [file.name for file in os.scandir('filters')]

count = 0
for file in filter_files:
    result = sieve(filed, f"filters/{file}")

    filed = results[0]
    count += result[1]
    print(count)

with open('updated_contacts', 'w') as file:
    for num, details in contacts.items():
        for detail in details:
            file.write(f'{detail}')
