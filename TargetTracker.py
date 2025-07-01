import requests
import argparse
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Kontrol edilecek platformlar ve URL şablonları
platformlar = {
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitter": "https://twitter.com/{}"
}

def kullanici_kontrol(kullanici_adi):
    sonuc = {}
    print(f"\n{Style.BRIGHT}🔎 TargetTracker hedef: {kullanici_adi}\n")

    for isim, url in platformlar.items():
        tam_url = url.format(kullanici_adi)
        try:
            cevap = requests.get(tam_url, timeout=5)
            if cevap.status_code == 200:
                print(f"{Fore.GREEN}[+] {isim}: Bulundu ✅")
                sonuc[isim] = tam_url
            else:
                print(f"{Fore.RED}[-] {isim}: Bulunamadı ❌")
        except:
            print(f"{Fore.YELLOW}[!] {isim}: Hata oluştu")
    
    return sonuc

def sonuc_kaydet(kullanici_adi, sonuc):
    if not os.path.exists("sonuclar"):
        os.mkdir("sonuclar")
    dosya_yolu = os.path.join("sonuclar", f"sonuclar_{kullanici_adi}.json")
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        json.dump(sonuc, dosya, indent=4, ensure_ascii=False)
    print(f"\n{Fore.CYAN}📁 Sonuçlar {dosya_yolu} dosyasına kaydedildi.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kullanıcı adının çeşitli platformlarda varlığını kontrol eder.")
    parser.add_argument("--kullanici", required=True, help="Hedef kullanıcı adı")
    args = parser.parse_args()

    bulunanlar = kullanici_kontrol(args.kullanici)
    sonuc_kaydet(args.kullanici, bulunanlar)
