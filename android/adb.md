# ADB: `Cheatsheet for Android Debug Bridge`
![image](https://github.com/TechnologyMediaorg/LearnSheet/assets/111997815/770fe417-3d68-4099-b9cc-40635f9fe3b0)

## ADB Server
- `adb kill-server`
- `adb start-server` 

## ADB Reboot
- `adb reboot`
- `adb reboot recovery` 
- `adb reboot-bootloader`
- `adb root` // restarts ADB with root permissions

## Shell
- `adb shell` // Open or run commands in a terminal on the host Android device.

## Devices
- `adb usb`
- `adb devices` // show devices attached
- `adb devices -l` // devices (product/model)
- `adb connect ip_address_of_device`

## Get device android version
- `adb shell getprop ro.build.version.release` 

## LogCat
- `adb logcat`
- `adb logcat -c` // clear // The parameter -c will clear the current logs on the device.
- `adb logcat -d > [path_to_file]` // Save the logcat output to a file on the local system.
- `adb bugreport > [path_to_file]` // Will dump the whole device information like dumpstate, dumpsys, and logcat output.

## Files
- `adb push [source] [destination]` // Copy files from your computer to your phone.
- `adb pull [device file location] [local file location]` // Copy files from your phone to your computer.

## App install
- `adb -e install path/to/app.apk`

-d                        - directs command to the only connected USB device...
-e                        - directs command to the only running emulator...
-s <serial number>        ...
-p <product name or path> ...
The flag you decide to use has to come before the actual `adb command:

- `adb devices | tail -n +2 | cut -sf 1 | xargs -IX - `adb -s X install -r com.myAppPackage` // Install the given app on all connected devices.

## Uninstalling app from device
- `adb uninstall com.myAppPackage`
- `adb uninstall <app .apk name>`
- `adb uninstall -k <app .apk name>` -> "Uninstall .apk without deleting data"

- `adb shell pm uninstall com.example.MyApp`
- `adb shell pm clear [package]` // Deletes all data associated with a package.

- `adb devices | tail -n +2 | cut -sf 1 | xargs -IX - `adb -s X uninstall com.myAppPackage` // Uninstall the given app from all connected devices

## Update app
- `adb install -r yourApp.apk` // -r means re-install the app and keep its data on the device.
- `adb install –k <.apk file path on computer>` 

## Home button
- `adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`

## Activity Manager
- `adb shell am start -a android.intent.action.VIEW`
- `adb shell am broadcast -a 'my_action'`

- `adb shell am start -a android.intent.action.CALL -d tel:+972527300294` // Make a call

// Open send sms screen with phone number and the message:
- `adb shell am start -a android.intent.action.SENDTO -d sms:+972527300294   --es  sms_body "Test --ez exit_on_sent false`

// Reset permissions for an app:
- `adb shell pm reset-permissions PACKAGE_NAME`

## Emulator
- `adb emu kill`
- `adb emu kill-all`
- `adb emu ping`
- `adb emu avd name`
- `adb -s emulator-5556 emu avd name`

## WiFi
- `adb shell svc wifi enable`
- `adb shell svc wifi disable`

## Battery
- `adb shell dumpsys battery set level 50` // Set battery level to 50%

## Screen Capture
- `adb shell screencap -p /sdcard/screenshot.png` // Capture screen and save to file
- `adb pull /sdcard/screenshot.png` // Copy file from device to computer

## Package Manager
- `adb shell pm list packages`
- `adb shell pm list packages -f` // include the full path to the APK.

## SQLite database
- `adb shell sqlite3 /data/data/package_name/databases/database_name.db` // Open database shell

## Monkey
- `adb shell monkey -p your.package.name -v 500` // Send 500 pseudo-random events to your app

## Backup and Restore
- `adb backup -f backup.ab -apk com.example.app` // Backup the app and its data
- `adb restore backup.ab` // Restore the app and its data from the backup file

## Miscellaneous
- `adb shell input keyevent 26` // Press the power button
- `adb shell input keyevent 82` // Press the menu button
- `adb shell input text "Hello World"` // Input text on the device

## Resources
- [ADB Cheat Sheet](https://devhints.io/adb)

## Note
- Replace `[source]`, `[destination]`, `[path_to_file]`, `[device file location]`, `[local file location]`, `[app .apk name]`, `[package]`, `[.apk file path on computer]`, `com.myAppPackage`, `yourApp.apk`, `PACKAGE_NAME`, `your.package.name`, `backup.ab`, `com.example.app` with the actual values in your specific use case.
