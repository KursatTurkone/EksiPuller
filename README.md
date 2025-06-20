# Ekşi Entry Scraper

Bu Python scripti, [eksisozluk.com](https://eksisozluk.com) üzerinden belirli bir başlıktaki entry'leri gezerek her sayfadaki entry'leri bir Excel dosyasına kaydeder.

---

## ✨ Özellikler

- Belirli bir başlık slug'ı ve sayfa numarasından başlayarak entry'leri toplar
- Tüm sayfalar otomatik gezilir ("sonraki sayfa" tıklamaları dahil)
- Entry yazarı, tarih ve içeriği Excel dosyasına kaydedilir
- Çıktı dosyası masaüstüne `entryler.xlsx` olarak kaydedilir

---

## 📅 Gereksinimler

1. **Python 3.10+** yüklenmiş olmalı\
   → [Python indir](https://www.python.org/downloads/)

2. Gerekli Python kütüphanelerini yükleyin:

   ```bash
   py -m pip install selenium openpyxl
   ```

3. **ChromeDriver** indirip masaüstüne atın\
   → [ChromeDriver indir](https://googlechromelabs.github.io/chrome-for-testing/)

4. `chrome.exe` binary dosyası masaüstünde `chrome-win64` klasörü altında olmalı:

   ```
   C:\Users\KullaniciAdi\Desktop\chrome-win64\chrome.exe
   ```

---

## 🔄 Kullanım Adımları

1. Aşağıdaki dosya yapısını oluşturun:

```
Masaüstü/
├── chrome-win64/
│   └── chrome.exe
├── chromedriver.exe
├── eksi_scraper_manual_next.py
```

2. CMD (komut istemi) açın ve aşağıyı yazın:

```bash
cd %USERPROFILE%\Desktop
py eksi_scraper_manual_next.py
```

3. Script otomatik olarak `https://eksisozluk.com/umut-ozkirimli--411351?p=8` sayfasından başlar ve son sayfaya kadar ilerler.

4. Entry'ler masaüstünüzde `entryler.xlsx` adlı dosyaya kaydedilir.

---

## 🔢 Excel Formatı

| Sıra | Yazar             | Tarih            | İçerik           |
| ---- | ----------------- | ---------------- | ---------------- |
| 1    | eksici\_kullanici | 01.01.2023 12:45 | entry içeriği... |

---

## ⚠️ Notlar

- ChromeDriver ve chrome.exe **sürüm uyumlu** olmalıdır.
- Tarayıcınızın sürümünü kontrol edin ve aynı sürüme sahip ChromeDriver ındırın.
- Sayfada bot koruması varsa bazen ilk açılışta hata olabilir, tekrar deneyin.

---

## 🚀 Proje Ayarlarını Değiştirme

Script başlık slug'ını ve sayfa numarasını otomatik başlatacak şekilde ayarlıdır. Değiştirmek için şu satırları güncelleyebilirsiniz:

```python
slug = "umut-ozkirimli--411351"
start_page = 8
```

---

Herhangi bir sorun durumunda lütfen geri bildirimde bulunun. Keyifli scrapingler! ✨

