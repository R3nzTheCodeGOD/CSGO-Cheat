import pymem
import re

def main() :
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        print("[HATA] CS:GO Açık Değil!")
        return

    client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08', clientModule).start() + 6

    pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
    pm.close_process()

if __name__ == '__main__':
    main()