import time
import pywinauto
from pywinauto.application import Application
app=Application().start(cmd_line=r"D:\Putty\putty.exe")
app=Application().connect(title="PuTTY Configuration")
window=app.PuTTYConfigBox
window.set_focus()
window[u"Host Name (or IP address):Edit"].type_keys("tty.sdf.org")
window[u"Port:Edit"].set_edit_text("22")
window["Open"].click()
putty = app.PuTTY
putty.type_keys("wsssd")
putty.type_keys("{ENTER}")

putty.type_keys("{ENTER}")


'''
app=Application().start(cmd_line=r"D:\Putty\putty.exe")
time.sleep(5)
app=Application().connect(title="PuTTY Configuration")
window=app.PuTTYConfigBox
window.set_focus()
window["Other:RadioButton"].click()
time.sleep(3)
window[u"Host Name (or IP address):Edit"].type_keys("192.168.10.1")
time.sleep(3)
window["Open"].click()
'''
