emails = (("Ali", "ali@gmail.com"),
("Vali", "vali@yandex.ru"),
("Sami", "sami@mail.ru"))

domains = []

for item in emails:
    email = item[1] 
    domain = email.split("@")[1]   
    domains.append(domain)

print(domains)
