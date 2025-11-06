from datetime import date, datetime


# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы


def normalize_addresses(email: dict) -> dict:
    normalized_email = {}

    for key, value in email.items():
        if isinstance(value, str):
            normalized_value = value.lower().strip()
        else:
            normalized_value = value

        normalized_email[key] = normalized_value

    return normalized_email


# 2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")


def add_short_body(email: dict) -> dict:
    email["short_body"] = email["body"][:10] + "..."
    return email


# 3. Очистка текста письма - заменяет табы и переводы строк на пробелы


def clean_body_text(body: str) -> str:
    return body.replace("\t", " ").replace("\n", " ")


# 4. Формирование итогового текста письма - создает форматированный текст письма


def build_sent_text(email: dict) -> str:
    return f'Кому: {email["to"]}, от {email["from"]}, Тема: {email["subject"]}, дата {email["date"]} {email["clean_body"]}.'


# 5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля


def check_empty_fields(email: dict) -> tuple[bool, bool]:
    is_subject_empty = False
    is_body_empty = False

    match email.get("subject"):
        case "":
            is_subject_empty = True

    match email.get("body"):
        case "":
            is_body_empty = True

    return is_subject_empty, is_body_empty


# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)


def mask_sender_email(login: str, domain: str) -> str:
    login = email["from"].split("@")[0][:2]
    domain = email["from"].split("@")[-1]
    return f"{login} '***@' {domain}"


# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)


def get_correct_email(email_list: list[str]) -> list[str]:
    correct_email = []
    for email in email_list:
        clean_email = email.strip().lower()
        if "@" in clean_email and clean_email.endswith((".com", ".ru", ".net")):
            correct_email.append(clean_email)
    return correct_email


# 8. Создание словаря письма - создает базовую структуру письма


def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    email = {"sender": sender, "recipient": recipient, "subject": subject, "body": body}
    return email


# 9. Добавление даты отправки - добавляет текущую дату


def add_send_date(email: dict) -> dict:
    new_email = email.copy()
    new_email["date"] = datetime.now().strftime("%y-%m-%d")
    return new_email


# 10. Получение логина и домена - разделяет email на логин и домен


def extract_login_domain(address: str) -> tuple[str, str]:
    login = email["to"].split("@")[0]
    domain = email["to"].split("@")[1]

    return login, domain
