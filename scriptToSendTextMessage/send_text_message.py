def send_text_message(apikey, phone_number, message):
    import requests
    resp = requests.post('https://textbelt.com/text', {
    'phone': phone_number,
    'message': message,
    'key': apikey,
    })