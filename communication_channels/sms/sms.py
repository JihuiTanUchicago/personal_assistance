from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='',
  body='Hello from Twilio',
  to=''
)

print(message.sid)