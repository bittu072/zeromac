from macos.currentinfo import show_current_wifi

base_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
result = show_current_wifi(base_command)
# print result
