from datetime import datetime


# 1. Создайте словарь email,
email = {
    "subject": " Quarterly Report ",
    "from": " Alice.Cooper@Company.ru ",
    "to": "  bob_smith@Gmail.com  ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

# 2. Добавьте дату отправки

email["date"] = send_date = datetime.now().strftime("%y-%m-%d")


#3. Нормализуйте e-mail адреса отправителя и получателя:

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

#4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email["from"].split('@')[0]
domain = email["from"].split('@')[-1]

# Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
 #Сохраните в новый ключ словаря: email["short_body"].

email["body"] = email["body"][:10] + "..."

# Списки доменов: создайте список личных доменов

domain_personal = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru','company.ru']
domain_corporate = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
domain_personal = list(set(domain_personal))
domain_corporate = list(set(domain_corporate))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.

common_domains = set(domain_personal) & set(domain_corporate)

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки
# вхождения домена отправителя в список корпоративных доменов.

sender_domain = email["from"].split('@')[1].strip().lower()
is_corporate = sender_domain in domain_corporate


# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел. Сохраните
# в email["clean_body"].

email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

email["sent_text"] = f'Кому: {email["to"]}, от {email["from"]} Тема: {email["subject"]}, дата {email["date"]} {email["clean_body"]}'


# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

text_length = len(email["sent_text"])
pages = (text_length + 499) // 500

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет
# хранится что тема письма содержит данные.

is_subject_empty = not email["subject"]
is_body_empty = not email["body"]


# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

login, domain = email["from"].split('@')
email["masked_from"] = login[:2] + "***@" + domain

#14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".

domain_personal.remove("list.ru")
domain_personal.remove("bk.ru")

print(email)
print(is_corporate, pages, is_subject_empty, is_subject_empty)