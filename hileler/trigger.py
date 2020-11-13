import keyboard
import pymem
import pymem.process
import time
import ctypes
import sys
sys.path.append('./')
import config
from Offsets import *



def main():
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
        return
    
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:
        player = pm.read_int(client + dwLocalPlayer)
        entity_id = pm.read_int(player + m_iCrosshairId)
        entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

        entity_team = pm.read_int(entity + m_iTeamNum)
        player_team = pm.read_int(player + m_iTeamNum)

        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
            time.sleep(config.responseSpeed)
            pm.write_int(client + dwForceAttack, 6)

        time.sleep(config.fireLoop)

if __name__ == '__main__':
    main()