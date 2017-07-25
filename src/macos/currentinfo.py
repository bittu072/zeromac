import os

def show_current_wifi(base_command):
    enter_command = base_command + " --getinfo"
    # result = os.system(enter_command)
    temp_result = os.popen(enter_command)
    result = temp_result.read()
    temp_result.close()
    result = result.replace(" ", "").splitlines( )

    wifi_result = {}
    for i in result:
        if ("SSID" or "BSSID") in i:
            wifi_result[i.split(":")[0]] = i.split(":",1)[-1]
        elif "lRSSI" in i:
            wifi_result["signal_strength"] = i.split(":")[-1]

    print (wifi_result)

# example output
#       agrCtlRSSI: -72
#      agrExtRSSI: 0
#     agrCtlNoise: -95
#     agrExtNoise: 0
#           state: running
#         op mode: station
#      lastTxRate: 176
#         maxRate: 1300
# lastAssocStatus: 0
#     802.11 auth: open
#       link auth: wpa2-psk
#           BSSID: 10:86:8c:8b:8e:38
#            SSID: 8B8E38
#             MCS: 2
#         channel: 36,80
