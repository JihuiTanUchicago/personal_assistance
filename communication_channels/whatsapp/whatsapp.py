from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='',
  content_sid='',
  content_variables='',
  to=''
)

print(message.sid)