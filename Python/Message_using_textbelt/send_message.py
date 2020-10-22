import os
import requests

def send_message(phoneNumber, message):
    resp = requests.post('https://textbelt.com/text', {
    'phone':phoneNumber,
    'message':message,
    'key':'textbelt',
    })
    sent = resp.json()['success']
    if sent is True:
        print("Message successfully sent!")
    
    else:
        print("Sorry...Message cannot be sent")
        print(resp.json()['error'])

def main():
    phone_number = input("Enter your 10 digit phone number: ")
    message = input("Enter your message:")
    send_message(('+91'+str(phone_number)),message)

if __name__ == "__main__":
    main()

