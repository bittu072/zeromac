import os
import datetime

def show_current_wifi(base_command):
    """information of current wifi"""
    time_now = datetime.datetime.now()
    enter_command = base_command + " --getinfo"
    # result = os.system(enter_command)
    temp_result = os.popen(enter_command)
    result = temp_result.read()
    temp_result.close()
    result = result.replace(" ", "").splitlines( )

    wifi_result = {}
    wifi_result["time"] = str(time_now)
    for i in result:
        if ("SSID" or "BSSID") in i:
            wifi_result[i.split(":")[0]] = i.split(":",1)[-1]
        elif "lRSSI" in i:
            wifi_result["signal_strength"] = i.split(":")[-1]
    return wifi_result
