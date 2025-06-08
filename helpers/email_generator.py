import random
import string


def create_login(length=15, domain="@ya.ru"):
    domain_length = len(domain)
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(length - domain_length)]) + domain
