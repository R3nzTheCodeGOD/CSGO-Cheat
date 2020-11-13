import keyboard
import time
import threading
import multiprocessing
from multiprocessing import *
import sys
import winsound
import platform

sys.path.insert(1, 'hileler/')
from bhop import main as bhop
from noflash import main as noflash
from wallhack import main as wallhack
from radar import main as radar
from spray import main as spray
from money import main as money
from trigger import main as trigger
from config import *

_msg = f"""
    [R3NZTHECODEGOD] Hile Yazılımı v0.31
    
    # [Sitem Bilgileri]
    İşletim Sistemi = {platform.system()}
    Python Sürümü = {sys.version}
    
    # [Hile Ayarları] 
    [{bunnyKey}] = Bunny Açar ve kapatır
    [{wallHackKey}] = Wallhack Açar ve kapatır
    [{radarKey}] = Radar Açar ve kapatır
    [{sprayKey}] = Spray Açar ve kapatır
    [{noFlashKey}] = Kör Olmama Açar ve kapatır
    [{moneyKey}] = Rakip paraları göstermeyi açar ve kapatır
    [{triggerKey}] = Trigger açar ve kapatır
    
    # [Trigger ayarları]
    Trigger Tepki Süresi = [{responseSpeed}]
    Trigger Ateş Döngü Süresi = [{fireLoop}]

    # Oyunda ayarın açıkmı kapalımı olduğunu anlamak için bip seslerini dinleyin [ince] bip sesi ayarın açıldığını [kalın] bip sesi ayarın kapandığını belirtir.

    [Coded By Erdem © Tüm Hakları Saklıdır]
"""

class CSGO:
    def __init__(self) -> None:
        self.c_bhop = False
        self.c_noflash = False
        self.c_wallhack = False
        self.c_radar = False
        self.c_spray = False
        self.c_money = False
        self.c_trigger = False
        if startSound is True:
            winsound.PlaySound("sesler/ph.wav", winsound.SND_FILENAME)
            winsound.PlaySound("sesler/31.wav", winsound.SND_FILENAME)
        print(_msg)

    def f_bhop(self) -> None:
        if self.c_bhop is False:
            freeze_support()
            self.t_bhop = Process(target=bhop)
            self.t_bhop.start()
            self.c_bhop = True
            return
        if self.c_bhop is True:
            try:
                self.c_bhop = False
                self.t_bhop.terminate()
            except:
                pass

    def f_noflash(self) -> None:
        if self.c_noflash is False:
            freeze_support()
            self.t_noflash = Process(target=noflash)
            self.t_noflash.start()
            self.c_noflash = True
            return
        if self.c_noflash is True:
            try:
                self.c_noflash = False
                self.t_noflash.terminate()
            except:
                pass

    def f_wallhack(self) -> None:
        if self.c_wallhack is False:
            freeze_support()
            self.t_wallhack = Process(target=wallhack)
            self.t_wallhack.start()
            self.c_wallhack = True
            return
        if self.c_wallhack is True:
            try:
                self.c_wallhack = False
                self.t_wallhack.terminate()
            except:
                pass

    def f_radar(self) -> None:
        if self.c_radar is False:
            freeze_support()
            self.t_radar = Process(target=radar)
            self.t_radar.start()
            self.c_radar = True
            return
        if self.c_radar is True:
            try:
                self.c_radar = False
                self.t_radar.terminate()
            except:
                pass

    def f_spray(self) -> None:
        if self.c_spray is False:
            freeze_support()
            self.t_spray = Process(target=spray)
            self.t_spray.start()
            self.c_spray = True
            return
        if self.c_spray is True:
            try:
                self.c_spray = False
                self.t_spray.terminate()
            except:
                pass

    def f_money(self) -> None:
        if self.c_money is False:
            freeze_support()
            self.t_money = Process(target=money)
            self.t_money.start()
            self.c_money = True
            return
        if self.c_money is True:
            try:
                self.c_money = False
                self.t_money.terminate()
            except:
                pass

    def f_trigger(self) -> None:
        if self.c_trigger is False:
            freeze_support()
            self.t_trigger = Process(target=trigger)
            self.t_trigger.start()
            self.c_trigger = True
            return
        if self.c_trigger is True:
            try:
                self.c_trigger = False
                self.t_trigger.terminate()
            except:
                pass

    def main(self) -> None:
        while True:
            if keyboard.is_pressed(bunnyKey): 
                self.f_bhop()
                print(f"[BUNNY] {'Açıldı!' if self.c_bhop else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_bhop else 100, 600)
                time.sleep(0.6)

            if keyboard.is_pressed(noFlashKey):
                self.f_noflash()
                print(f"[ANTIFLASH] {'Açıldı!' if self.c_noflash else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_noflash else 100, 600)
                time.sleep(0.6)

            if keyboard.is_pressed(wallHackKey):
                self.f_wallhack()
                print(f"[WALLHACK] {'Açıldı!' if self.c_wallhack else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_wallhack else 100, 600)
                time.sleep(0.6)

            if keyboard.is_pressed(radarKey):
                self.f_radar()
                print(f"[RADAR] {'Açıldı!' if self.c_radar else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_radar else 100, 600)
                time.sleep(0.6)

            if keyboard.is_pressed(sprayKey):
                self.f_spray()
                print(f"[SPRAY] {'Açıldı!' if self.c_spray else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_spray else 100, 600)
                time.sleep(0.6)
            
            if keyboard.is_pressed(moneyKey):
                self.f_money()
                print(f"[MONEY] {'Açıldı!' if self.c_money else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_money else 100, 600)
                time.sleep(0.6)
            
            if keyboard.is_pressed(triggerKey):
                self.f_trigger()
                print(f"[TRIGGER] {'Açıldı!' if self.c_trigger else 'Kapatıldı!'}")
                winsound.Beep(500 if self.c_trigger else 100, 600)
                time.sleep(0.6)

            time.sleep(0.001)

if __name__ == "__main__":
    freeze_support()
    client = CSGO()
    client.main()

