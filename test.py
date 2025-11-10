import re
from datetime import datetime


# Часть A
# Нормализация email адресов
def normalize_addresses(email_dict):
    new_dict = email_dict.copy()
    if 'from' in new_dict:
        new_dict['from'] = new_dict['from'].lower().strip()
    if 'to' in new_dict:
        new_dict['to'] = new_dict['to'].lower().strip()
    return new_dict

#Сокращенная версия тела письма
def add_short_body(email_dict):
    new_dict = email_dict.copy()
    text = new_dict.get('body', '')
    new_dict['short_body'] = text[:10] + "..."
    return new_dict

# Очистка текста письма
def clean_body_text(text):
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    return text

#Формирование итогового текста письма
def build_sent_text(email_dict):
    result = f"Кому: {email_dict['to']}, от {email_dict['from']}\n"
    result += f"Тема: {email_dict['subject']}, дата {email_dict['date']}\n"
    result += f"{email_dict['clean_body']}"
    return result

#Проверка пустоты темы и тела
def check_empty_fields(email_dict):
    subject_empty = not email_dict.get('subject', '').strip()
    body_empty = not email_dict.get('body', '').strip()
    return subject_empty, body_empty

#Маска email отправителя
def mask_sender_email(login, domain):
    return f"{login[:2]}***@{domain}"

#Создать функцию которая проверит корректности email адресов. Адрес считается корректным, если:
#Eсодержит символ @;
#оканчивается на один из доменов: .com, .ru, .net.
def get_correct_email(emails_list):
    good_emails = []
    for email in emails_list:
        email = email.strip().lower()
        if "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net")):
            good_emails.append(email)
    return good_emails

#Создание словаря письма
def create_email(sender, recipient, subject, body):
    return {
        'sender': sender,
        'recipient': recipient,
        'subject': subject,
        'body': body
    }


def add_send_date(email_dict):
    new_dict = email_dict.copy()
    today = datetime.now()
    new_dict['date'] = today.strftime("%Y-%m-%d")
    return new_dict

#Добавление даты отправки
def extract_login_domain(email):
    parts = email.split('@')
    return parts[0], parts[1]


# Часть B

def sender_email(recipient_list, subject, message, sender="default@study.com"):
    # 1. Проверить что есть получатели
    if len(recipient_list) == 0:
        return []

    # 2. Проверить email адреса
    sender_ok = get_correct_email([sender])
    recipients_ok = get_correct_email(recipient_list)

    if len(sender_ok) == 0 or len(recipients_ok) == 0:
        return []

    good_sender = sender_ok[0]

    # 3. Проверить что тема и сообщение не пустые
    check_dict = {'subject': subject, 'body': message}
    subject_bad, body_bad = check_empty_fields(check_dict)
    if subject_bad or body_bad:
        return []

    # 4. Убрать отправку себе
    final_recipients = []
    for r in recipients_ok:
        if r != good_sender:
            final_recipients.append(r)

    if len(final_recipients) == 0:
        return []

    # 5. Почистить текст
    clean_subj = clean_body_text(subject)
    clean_msg = clean_body_text(message)

    # Нормализовать адреса
    norm_recipients = []
    for r in final_recipients:
        norm_dict = normalize_addresses({'to': r})
        norm_recipients.append(norm_dict['to'])

    norm_sender_dict = normalize_addresses({'from': good_sender})
    norm_sender = norm_sender_dict['from']

    # 6. Создать письма
    all_emails = []

    for recipient in norm_recipients:
        # Создаем письмо
        email_data = create_email(norm_sender, recipient, clean_subj, clean_msg)

        # Добавляем дату
        email_data = add_send_date(email_data)

        # Маскируем отправителя
        login, domain = extract_login_domain(norm_sender)
        email_data['masked_sender'] = mask_sender_email(login, domain)

        # Делаем короткий текст
        email_data = add_short_body(email_data)
        email_data['clean_body'] = email_data['short_body']

        # Создаем итоговый текст
        temp_for_text = {
            'to': email_data['recipient'],
            'from': email_data['masked_sender'],
            'subject': email_data['subject'],
            'date': email_data['date'],
            'clean_body': email_data['clean_body']
        }
        email_data['sent_text'] = build_sent_text(temp_for_text)

        all_emails.append(email_data)

    return all_emails


# Проверка
emails = sender_email(
    recipient_list=["admin@company.ru", "manager@study.com", "default@study.com"],
    subject="Hello!",
    message="Привет, коллега!",
    sender="default@study.com",
)

for e in emails:
    print(e["sent_text"])
    print("---")



