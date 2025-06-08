
# 🧠 Hamming SEC-DED Simülatörü

Bu proje, BLM230 Bilgisayar Mimarisi dersi projesi için geliştirilmiş bir **Hamming SEC-DED (Single Error Correction – Double Error Detection)** kodlama simülatörüdür. Proje, manuel olarak girilen veya otomatik oluşturulan 8, 16 veya 32 bitlik bir verinin hamming koda dönüştürülmesi ve sonrasında isteğe bağlı olarak 1 veya 2 hata yaparak bunların düzeltilmeye çalışılmasını sağlayan bir python kodunu içermektedir.

---


## 📌 İçindekiler

- [Genel Bakış]
- [Kurulum]
- [Kod Açıklamaları]
- [Ekran Görüntüleri]
- [Kaynak Kod ve Video]

---


## 🎯 Genel Bakış

Bu simülatör:

8, 16 ve 32 bitlik verileri Hamming koduna dönüştürür. Yapay olarak rastgele bir bite hata ekler bu biti ve sendromu hesaplayıp hatalı biti bulup düzeltebilir (SEC). Yapay olarak rastgele iki bite hata ekleyebilir. Eğer iki bite hata eklenirse bu hataları algılar fakat bu hataları düzeltemez (DED).

---


## ⚙️ Kurulum

Projede sadece Python dili kullanılmıştır. Güncel Pyhton ile projeyi çalıştırabilirsiniz. Gui için Python'ın kendi kütüphanesi oan tkinter kullanılmıştır. Bu yüzden ekstra bir kütüphane indirmenize gerek yoktur.

---

## 🧩 Kod Açıklamaları

### `hamming_module.py`
- `encode_hamming()` → SEC-DED kodu üretir
- `inject_error()` → rastgele ya da belirli bitte hata oluşturur
- `detect_and_correct()` → sendrom hesaplar, hatayı düzeltir

### `hamming_gui.py`
- Tkinter arayüz
- Kullanıcıdan veri alır, kodlar, hata oluşturur ve düzeltir

---


## 🖼️ Ekran Görüntüleri

> `ekran_goruntuleri/` klasöründe arayüzün çeşitli aşamalarını içeren ekran görüntüleri yer almaktadır:

- Veri girişi
- Kodlama sonrası çıktı
- Hata sonrası bozulmuş veri
- Düzeltme işlemi

---


## 🔗 Kaynak Kod ve Video

- 💻 GitHub: [github.com/kullaniciAdi/hamming-simulator](#)
- 🎥 Video Sunum: [youtube.com/watch?v=ornekvideo](#)

---


