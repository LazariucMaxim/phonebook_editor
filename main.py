from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for i, row in enumerate(contacts_list):
    contacts_list[i][:3] = list(" ".join(row[:3]).split(" "))[:3]
text = "\n".join(map(lambda x: ", ".join(x), contacts_list))
# print(text)
pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s?\(?([^,\)\d\s]*)\s?(\d*)\)?"
result = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", text)  # +7(999)999-99-99 доб.9999
contacts_list_v2 = list(map(lambda x: list(map(lambda y: y.strip(), x.split(", "))), result.split("\n")))
contacts_list_v2.sort()
contacts_list_v3 = []
for lastname, firstname, surname, organization, position, phone, email in contacts_list_v2:
    if contacts_list_v3 == [] or lastname != contacts_list_v3[-1][0] or firstname != contacts_list_v3[-1][1]:
        contacts_list_v3.append([lastname, firstname, surname, organization, position, phone, email])
    else:
        if surname != "":
            contacts_list_v3[-1][2] = surname
        if organization != "" and organization != contacts_list_v3[-1][3]:
            if contacts_list_v3[-1][3] != "":
                contacts_list_v3[-1][3] += "; "
            contacts_list_v3[-1][3] += organization
        if position != "" and position != contacts_list_v3[-1][4]:
            if contacts_list_v3[-1][4] != "":
                contacts_list_v3[-1][4] += "; "
            contacts_list_v3[-1][4] += position
        if phone != "" and phone != contacts_list_v3[-1][5]:
            if contacts_list_v3[-1][5] != "":
                contacts_list_v3[-1][5] += "; "
            contacts_list_v3[-1][5] += phone
        if email != "" and email != contacts_list_v3[-1][6]:
            if contacts_list_v3[-1][6] != "":
                contacts_list_v3[-1][6] += "; "
            contacts_list_v3[-1][6] += email

pprint(contacts_list_v3)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_v3)
