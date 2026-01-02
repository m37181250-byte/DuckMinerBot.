from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import threading
import time
import random

class DuckFinalApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # بخش نمایش اطلاعات تریدر و امنیت
        self.status_label = Label(
            text="BTC: $88358.15\nSecurity: Active ✅", 
            font_size='24sp',
            halign='center'
        )
        self.layout.add_widget(self.status_label)
        
        # دکمه هوشمند استخراج
        self.btn = Button(
            text="START SMART TAP", 
            background_color=(0, 0.8, 0, 1),
            font_size='20sp'
        )
        self.btn.bind(on_press=self.toggle_engine)
        self.layout.add_widget(self.btn)
        
        self.running = False
        return self.layout

    def toggle_engine(self, instance):
        self.running = not self.running
        if self.running:
            self.btn.text = "STOPPING AI..."
            self.btn.background_color = (0.8, 0, 0, 1)
            threading.Thread(target=self.ai_tap_logic, daemon=True).start()
        else:
            self.btn.text = "START SMART TAP"
            self.btn.background_color = (0, 0.8, 0, 1)

    def ai_tap_logic(self):
        while self.running:
            # شبیه‌سازی الگوی انسانی که در تصویر ۱۱ داشتی
            delay = random.uniform(0.08, 0.15)
            
            # اینجا فرمان کلیک صادر می‌شود
            # بعد از تبدیل به APK، این بخش با Accessibility Service جایگزین می‌شود
            print(f"AI Action: Tap Sent | Delay: {delay:.3f}s")
            
            # استراحت‌های هوشمند ۵، ۸ و ۱۱ ثانیه‌ای
            if random.random() < 0.05:
                rest = random.choice([5, 8, 11])
                print(f"💤 AI Resting for {rest}s to avoid ban...")
                time.sleep(rest)
                
            time.sleep(delay)

if __name__ == '__main__':
    DuckFinalApp().run()
