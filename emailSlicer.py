import re
from validate_email import validate_email

def email_slicer(string):
    email_regex = r'\S+@\S+'
    match = re.search(email_regex, string)
    if match:
        email = match.group()
        is_valid = validate_email(email)
        if is_valid:
            return email
        else:
            print('O email não é válido.')
    else:
        print('Nenhum email foi encontrado.')
    

string = "meu e-mail é example@gmail.com, entre em contato comigo!"

print(email_slicer(string))
