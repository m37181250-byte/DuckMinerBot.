[app]
title = Duck AI Miner
package.name = duckminerbot
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# کتابخانه‌های مورد نیاز (دقیقاً بدون کامای اضافی در انتها)
requirements = python3,kivy,requests

# تنظیمات دسترسی برای پنجره شناور (حل مشکل کلیک در اندروید)
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE
android.api = 33
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2

