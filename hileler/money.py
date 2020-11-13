import pymem
import re
import time

def main() :
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        print("[HATA] CS:GO Açık Değil!")
        return

    client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', clientModule).start()

    while True :
        old = str(pm.read_uchar(address))
        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)

if __name__ == '__main__':
    main()