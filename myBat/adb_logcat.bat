chcp 65001

adb connect 127.0.0.1:7555
adb shell "logcat | grep "Unity""

pause
exit