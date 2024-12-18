message = 'Ты видишь это сообщение потому что ты лучший ученик'
recipient = 'sehrek@mail.ru'
sender = 'university.help@gmail.com'

def send_email ( message, recipient,*, sender ):
    if sender == recipient :

        print('нельзя отправить письмо самому себе')

        return

    if not  sender.endswith(('.com','.net','.ru')) or not recipient.endswith(('.com','.net','.ru')):

        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}!!!')

        return

    if '@' not in sender or '@' not in recipient :

        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}' )
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    else:
        print(f'{message},НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')



send_email( 'Ты видишь это сообщение потому что ты лучший ученик','univer@mail.ru', sender=sender)
