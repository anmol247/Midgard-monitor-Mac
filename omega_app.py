from fileinput import filename
import rumps
import psutil
import os
import sys

def resource_path(filename):
        try:
            base_path = sys._MEIPASS  # PyInstaller temp dir
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, filename)

class OmegaWatcherApp(rumps.App):
    def __init__(self):
        super(OmegaWatcherApp, self).__init__("Ω", icon=resource_path("omega_normal.png"), quit_button=None)
        self.menu = ["Quit"]
        self.timer = rumps.Timer(self.check_cpu_usage, 2)  # Check every 2 seconds
        self.timer.start()
        self.notified = False  # To prevent notification spam

    
    
    def check_cpu_usage(self, _):
        cpu = psutil.cpu_percent()
        
        if cpu > 50:
            self.icon = resource_path("omega_fiery.png")
            if not self.notified:
                rumps.notification(
                    title="⚠️ High CPU Usage",
                    subtitle="RAGE MODE ON",
                    message=f"CPU usage is at {cpu}%, close apps for CLD",
                    sound=True
                )
                self.notified = True
        else:
            self.icon = resource_path("omega_normal.png")
            self.notified = False  # Reset if CPU drops
        
        self.title = ""
        self.tooltip = f"CPU Usage: {cpu}%"

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()

if __name__ == "__main__":
    OmegaWatcherApp().run()
