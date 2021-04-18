import threading, speedtest, global_var as g

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform


class SpeedTest_Screen(Screen):
    def getSpeedTest(self):
        self.loading_button.active = True
        self.req_button.opacity = 0
        self.req_button.disabled = 1
        t1 = threading.Thread(target=self.retSpeedTest).start()
        print(f"ret : {g.speed_test_src}, {g.speed_test_host}, {g.speed_test_dl}, {g.speed_test_up}")

    def retSpeedTest(self):
        g.speed_test_src, g.speed_test_host, g.speed_test_dl, g.speed_test_up = speedtest.main()
        self.ret_speedtest.text = g.speed_test_src+"\n\n"+g.speed_test_host+"\n\n"+g.speed_test_dl+"\n\n"+g.speed_test_up
        self.loading_button.active = False
        self.req_button.opacity = 1
        self.req_button.disabled = 0
    pass

class MainApp(MDApp):
    def build(self):
        # SSL certificate for HTTPS request
        import certifi
        import os
        os.environ['SSL_CERT_FILE'] = certifi.where()
        # Theming : https://kivymd.readthedocs.io/en/latest/themes/theming/index.html
        self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.theme_style = "Light"
        # print(portforwardlib.forwardPort(22,22,None,None,True,"TCP",9999, None,True))
        if platform =='android':
            print("Platform: Android")
            from android.permissions import Permission, request_permissions
            request_permissions([Permission.INTERNET, Permission.ACCESS_NETWORK_STATE, Permission.ACCESS_WIFI_STATE, Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

            def callback (permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print ("Did not get all permissions")
                    
        print("Platform: Not Android")
if __name__ == "__main__":
    MainApp().run()
