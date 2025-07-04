from typing import List, Tuple

def get_domains(emails:Tuple[Tuple]) -> List[str]:
    domains = list()
    for email in emails:
        i = email[1].find('@')
        domain = email[1][i + 1]
        domains.append(domain)

    return domains      




emails = (("Ali", "ali@gmail.com"),
("Vali", "vali@yandex.ru"),
("Sami", "sami@mail.ru"))
domain = get_domains(email)
print(domain)
