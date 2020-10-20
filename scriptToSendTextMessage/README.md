## Script to send a text message

# Usage:

You can test sending a message with a test-key "Textbelt", provided by Textbelt. To send more messages you need to create an API key in here: https://textbelt.com/.

The function to send a message takes three parameters: apikey, phone_number and message. They are all given as strings. Here's an example:

send_text_message('textbelt', '+358123456789', 'hello this is a test')