from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading
import time

class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self)

app = IBapi()
app.connect('127.0.0.1', 7497,0)
print(app.isConnected())
def run_loop():
    app.run()
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

'''
#Uncomment this section if unable to connect
#and to prevent errors on a reconnect
import time
time.sleep(2)
app.disconnect()
'''