# twilio : hitesh5pakhan@gmail.com
# password : Luci@7142128354249
# link : https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1&newCustomer=true
# accout name : Luci@714SMS
# link: https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1&newCustomer=true
# account sid : ACceea98b33845c6e787802ecc3f38077c
# account token : 20aa601f781471687f7a7096a54ad638

# windows powershell 
# $url = "https://api.twilio.com/2010-04-01/Accounts/ACceea98b33845c6e787802ecc3f38077c/Messages.json"
#                 $params = @{ To = "+919637754757"; From = "+17754056347"; Body = "Hello from Twilio" }
#                 $secret = "20aa601f781471687f7a7096a54ad638" | ConvertTo-SecureString -asPlainText -Force
#                 $credential = New-Object System.Management.Automation.PSCredential(ACceea98b33845c6e787802ecc3f38077c, $secret)
#                 Invoke-WebRequest $url -Method Post -Credential $credential -Body $params -UseBasicParsing | ConvertFrom-Json | Select sid, body

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACceea98b33845c6e787802ecc3f38077c"
auth_token = "20aa601f781471687f7a7096a54ad638"
client = Client(account_sid, auth_token)

message = client.messages.create(
                     from_='+17754056347',
                     body="are you get the message",
                     to='+919637754757'
                 )

print(message.sid)