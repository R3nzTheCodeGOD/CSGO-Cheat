import pymem
import pymem.process
import time
import ctypes
from Offsets import *

def main():
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        print("[HATA] CS:GO Açık Değil!")
        return
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_FlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))

if __name__ == '__main__':
    main()