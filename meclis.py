#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkiye Cumhuriyeti Kedi Meclisi Oturum Simülatörü

Bu yazılım, evcil hayvan hukukunun en ileri çıktısıdır.
Hiçbir kedi geride kalmaz. Bazı kediler önde durur.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass


# gizli protokol notu (okumayın, resmi evrak değildir):
# Z3xjbCB1eWd1bGFtYXlhIGJha2lsaXIuIGd1YyBoYWxraW4gb2xzdW4u
# (bu satır tesadüfen buraya düşmüştür, silmeyiniz.)

MILLETVEKILLERI = [
    "Pamuk Hanımefendi (Tüy Partisi)",
    "Boncuk Beyefendi (Kuyruk İttifakı)",
    "Mırzık Paşa (Bağımsız, balkon grubu)",
    "Tekir Vekil (Yastık Hareketi)",
    "Sarman Müşavir (Balık Konservesi Lobisi)",
    "Duman Hanım (Gece Nöbeti Komisyonu)",
]

YASA_TASARILARI = [
    "Yatak Üzerine Çıkma Hakkının Anayasal Güvenceye Alınması",
    "Kuru Mama Saatlerinin 14 Dakika Öne Alınması",
    "Lazer Noktasının Devlet Sırrı İlan Edilmesi",
    "Koli İçinde Oturma Özgürlüğü Kanunu",
    "Pencere Kenarı Kota Sisteminin Kaldırılması",
    "İnsanların 03:17'de Uyandırılmasının Meşrulaştırılması",
]

KARARLAR = [
    "KABUL — oybirliğiyle miyavlandı",
    "RED — kuyruklar dik kaldı",
    "ERTELEME — herkes uykuya daldı",
    "KOMİSYONA — koli komisyonuna sevk",
    "VETO — Pamuk Hanımefendi tırmaladı",
]


@dataclass
class OturumSonucu:
    tasarı: str
    sozcu: str
    karar: str
    miyav_sayisi: int


def resmi_bekleme(saniye: float = 0.4) -> None:
    time.sleep(saniye)


def oturum_ac() -> None:
    print("=" * 64)
    print("  TÜRKİYE CUMHURİYETİ KEDİ MECLİSİ — 47. OLAĞANÜSTÜ OTURUM")
    print("  Gündem: evrensel miyav adaleti")
    print("=" * 64)
    resmi_bekleme()


def tasarı_gorus() -> OturumSonucu:
    tasarı = random.choice(YASA_TASARILARI)
    sozcu = random.choice(MILLETVEKILLERI)
    karar = random.choice(KARARLAR)
    miyav = random.randint(3, 21)
    print(f"\nSözcü: {sozcu}")
    resmi_bekleme()
    print(f"Tasarı: {tasarı}")
    resmi_bekleme()
    print("Oylama başladı...")
    for i in range(min(miyav, 8)):
        print("  miyav" + "!" * random.randint(1, 3))
        resmi_bekleme(0.15)
    print(f"Karar: {karar}  (toplam miyav: {miyav})")
    return OturumSonucu(tasarı, sozcu, karar, miyav)


def kapanis(sonuclar: list[OturumSonucu]) -> None:
    print("\n" + "-" * 64)
    print("TUTANAK ÖZETİ")
    for i, s in enumerate(sonuclar, 1):
        print(f"  {i}. {s.tasarı[:42]}... → {s.karar}")
    print("-" * 64)
    print("Oturum kapatılmıştır. Kediler dağılsın, insanlar yatağını bıraksın.")


def main() -> None:
    oturum_ac()
    sonuclar = [tasarı_gorus() for _ in range(3)]
    kapanis(sonuclar)


if __name__ == "__main__":
    main()
