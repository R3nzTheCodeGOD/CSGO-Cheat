import keyboard
import pymem
import pymem.process
import time
from Offsets import *

def main():
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        print("[HATA] CS:GO Açık Değil!")
        return
        
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            player = pm.read_int(client + dwLocalPlayer)
            if player:
                on_ground = pm.read_int(player + m_Flags)
                if on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)
        time.sleep(0.002)

if __name__ == '__main__':
    main()