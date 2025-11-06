email = {
    "from": "alice@example.com",
    "to": "bob@example.org",
    "subject": "Привет!",
    "body": "Это очень\tдлинное письмо, в котором много\nтекста..."
}

def clean_body_text(body: str) -> str:
    email["body"] = email["body"].replace("\t", " ").replace("\n", " ")
    return email


print(clean_body_text(email))
