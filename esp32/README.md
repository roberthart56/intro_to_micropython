# intro_to_micropython

1/10/24
Installed Micropython on ESP32 xiao.


https://wiki.seeedstudio.com/XIAO_ESP32C3_MicroPython/

Clone esptool to a directory:
git clone https://github.com/espressif/esptool.git

Download the latest firmware.
https://micropython.org/download/esp32c3/

Navigate to the esptool folder in the esptool downloaded folder, put the firmware binary in that folder.

Flash the firmware:python  esptool.py --chip esp32c3 --port COM21 --baud 921600 --before default_reset --after hard_reset --no-stub  write_flash --flash_mode dio --flash_freq 80m 0x0 ESP32_GENERIC_C3-20240105-v1.22.1.bin

This erases and flashes device on COM18 with firmware in file downloaded from micropython site:




[A few more words about xiao modules and micropython](https://haystack-mtn.notion.site/Setting-up-simple-microcontroller-projects-Example-button-and-simple-LED-with-LiPo-battery-6196a7c8585649d7b8a7133133e4cf9e)

[Tutorial for installing micropython on a fresh ESP32](https://wiki.seeedstudio.com/XIAO_ESP32C3_MicroPython/)

[Random Nerd tutorial here](https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/)  looks better.




