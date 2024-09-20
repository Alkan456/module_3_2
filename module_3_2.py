def send_email(message, recipient, sender = "univerity.help@gmail.com"):
    if("@" and (".com"or".ru"or".net")) not in (recipient or sender) or ("@" or (".com"or"ru"or".net")) not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "univerity.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender !="university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Well done','university.help@mail.com','alkan@gmail.com')
send_email('Good job', 'univerity.help@gmail.com')
send_email('Just do it','shustrik43@gmail.com')
send_email('Who are you?','unknown@.c')