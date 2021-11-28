import string
import random
import time
import crayons
from discord_webhook import *

print("{}".format(crayons.green('This was made by FlyingndCoding!')))
print("{}".format(crayons.red('Enjoy View it on github: https://github.com/FlyingndCoding/NitroWebhooker-DiscordWebhookbot')))

def send():
    webhook = DiscordWebhook(url=webhookurl, content="https://discord.gift/" + code) # First part of the generating.
    response = webhook.execute()

# SETTINGS
webhookurl = 'YOURWEBHOOKURL' 
# Put your webhook here. ^^^^

changewh = input("\nDo you want to change the webhook URL? \n\nIf you already set the webhook URL in the files enter N.\nIf not, enter Y and generate a new webhook URL.\n(Y/N) > ")
if changewh == "y":
    webhookurl = input("You have chosen to change the web hook url, paste it here and press enter. > ")

amount = 0
amount = input("\nHow many codes would you like to be sent to your server? \n> ")

print("{}".format(crayons.blue('\n'+ amount +' code(s) will be generated and sent!')))
print("{}".format(crayons.blue('Closing session...')))

### WEBHOOK SENDER

for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # Makes strings and sends them.
    print("{}".format(crayons.magenta('\n> Generated code: ' + code + '\n- Code Number: %d' % (x))))
    time.sleep(0.5)
    print("{}".format(crayons.green('- Code sent!')))
    time.sleep(1.65) # Cooldown because of rate limited.

### CLOSING
print("{}".format(crayons.red('\nDisconnecting from server...')))
time.sleep(0.1)
print("{}".format(crayons.red('Closing session...')))
time.sleep(0.2)
print("{}".format(crayons.red('Cleaning files...')))
time.sleep(0.3)
print("{}".format(crayons.red('Stoping Generator...')))
time.sleep(0.2)
print("{}".format(crayons.red('Stoping API...')))
time.sleep(0.4)
print("{}".format(crayons.red('Clearing history...')))
time.sleep(0.2)

print('\nAll the codes have been sent! Go check them out!')
time.sleep(1)
