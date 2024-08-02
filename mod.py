import subprocess

ADB_PATH = "/Users/phuhoa/Downloads/platform-tools/adb"  

def get_connected_devices():
    result = subprocess.check_output([ADB_PATH, 'devices'])
    devices = []
    for line in result.decode('utf-8').splitlines()[1:]:  # decode bytes to string for Python 3 compatibility
        if '\tdevice' in line:
            devices.append(line.split('\t')[0])
    return devices

def set_battery_level(device, level):
    subprocess.call([ADB_PATH, '-s', device, 'shell', 'dumpsys', 'battery', 'set', 'level', str(level)])

def uninstall_apps(device, apps):
    for app in apps:
        subprocess.call([ADB_PATH, '-s', device, 'shell', 'pm', 'uninstall', '--user', '0', app]) 

def disable_sleep_wifi(device):  
    subprocess.call([ADB_PATH, '-s', device, 'shell', 'settings', 'put', 'global', 'wifi_sleep_policy', '2'])

def disable_auto_update(device):
    subprocess.call([ADB_PATH, '-s', device, 'shell', 'settings', 'put', 'global', 'auto_update_apps', '0'])


def main():
    apps_to_uninstall = [
        "com.dsi.ant.server", "com.google.android.marvin.talkback", "com.vinsmart.calculator",
        "com.vinsmart.calendar", "com.android.callogbackup",
        "com.vinsmart.camera", "com.vinsmart.contacts", "com.vsmart.dualapps",
        "com.google.android.apps.tachyon", "com.caf.fmradio",
        "com.google.android.videos",
        "com.google.android.keep", "com.qualcomm.qti.logkit.lite", "com.qualcomm.qti.modemtestmode",
        "com.google.android.apps.messaging", "com.vinsmart.messaging", "com.android.musicfx",
        "com.example.connmgr", "com.google.android.apps.youtube.music",
        "com.qualcomm.wfd.service", "com.vsmart.android.vsmartwarranty", "com.vinsmart.vboard",
        "com.vingroup.vinid", "org.codeaurora.snapcam", "com.qualcomm.qct.dlt",
        "com.qualcomm.qti.sensors.qsensortest", "com.qualcomm.qti.qmmi", "com.qualcomm.qti.presenceappSub2",
        "com.qualcomm.qti.presenceapp", "com.vsmart.soundrecorder", "com.google.android.apps.translate",
        "com.vinsmart.android.dialer",
        "com.google.android.youtube", "com.google.android.apps.maps", "com.google.android.apps.photos",
        "com.google.android.apps.docs", "com.google.android.googlequicksearchbox", "com.google.android.gm","com.android.vending"
    ]

    devices = get_connected_devices()
    for device in devices:
        
        set_battery_level(device, 100)

        
        uninstall_apps(device, apps_to_uninstall)

        
        disable_sleep_wifi(device)

        
        disable_auto_update(device)


if __name__ == "__main__":
    main()
