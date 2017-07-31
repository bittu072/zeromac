from macos.currentinfo import show_current_wifi
from macos.installer.initscript import place_xml

base_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
result = show_current_wifi(base_command)
# print result

place_xml("/Volumes/Bittu/trial.xml")
print ("writing succedded")
