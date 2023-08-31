from twilio.rest import Client
import config
client = Client(config.account_sid, config.auth_token)
message = client.messages.create(
     from_="+18155915094",
     body="This is just testing ...",
     to="+923439856501",
)
print(message.sid)
