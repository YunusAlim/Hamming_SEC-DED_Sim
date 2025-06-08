
# 🧠 Hamming SEC-DED Simülatörü

Bu proje, BLM230 Bilgisayar Mimarisi dersi projesi için geliştirilmiş bir **Hamming SEC-DED (Single Error Correction – Double Error Detection)** kodlama simülatörüdür. Proje, manuel olarak girilen veya otomatik oluşturulan 8, 16 veya 32 bitlik bir verinin hamming koda dönüştürülmesi ve sonrasında isteğe bağlı olarak 1 veya 2 hata yaparak bunların düzeltilmeye çalışılmasını sağlayan bir python kodunu içermektedir.

---


## 📌 İçindekiler

- [Genel Bakış]
- [Kurulum]
- [Kod Açıklamaları]
- [Ekran Görüntüleri]
- [Tanıtım Videosu]

---


## 🎯 Genel Bakış

Bu simülatör:

8, 16 ve 32 bitlik verileri Hamming koduna dönüştürür. Yapay olarak rastgele bir bite hata ekler bu biti ve sendromu hesaplayıp hatalı biti bulup düzeltebilir (SEC). Yapay olarak rastgele iki bite hata ekleyebilir. Eğer iki bite hata eklenirse bu hataları algılar fakat bu hataları düzeltemez (DED).

---


## ⚙️ Kurulum

Projede sadece Python dili kullanılmıştır. Güncel Pyhton ile projeyi çalıştırabilirsiniz. Gui için Python'ın kendi kütüphanesi oan tkinter kullanılmıştır. Bu yüzden ekstra bir kütüphane indirmenize gerek yoktur.

---


## 🧩 Kod Açıklamaları

Kodun açıklamaları, Python dosyaları içinde yorum satırlarında açıkca belirtilmiştir bunun yanında seçilen sınıfların ve fonksiyonların isimleri kodu basit olarak tanıtacak şekilde seçilmiştir.

---


## 🖼️ Ekran Görüntüleri

Bu kısımda GUI daha iyi tanıtabilmek için ekran görüntüleri ile açıklamalar yapılmıştır.

![image](https://github.com/user-attachments/assets/86f71610-6e92-466a-9e39-5bb259fc546a)
- Kodu çalıştırınca gelen ana ekran her işlem bu ekran üzerinden kolayca gerçekleştirilir.


![image](https://github.com/user-attachments/assets/ca523930-e6a7-488f-a905-c553727ad800)
- Gireceğiniz veya otomatik olarak oluştacağınız verinin boyutunu seçtiğiniz ekran.


![image](https://github.com/user-attachments/assets/5bc5b408-f6e7-4da7-8c1a-105db1b0ca30)
- Verinin girildiği (veya generate tuşu ile rastgele oluşturulduğu) ardından hamming koda dönüştürülmesi ve kaydedilmesi için tuşların bulunduğu ekran.

![image](https://github.com/user-attachments/assets/2c8d094a-54e9-4cbb-8cd6-86c069730c5f)
- Kaydedilen kodun; soldan sağa olacak şekilde tek bitlik hata oluşturma, iki bitlik hata oluşturma, hata tespiti ve düzeltme için kullanılan butonların yer aldığı ekran.

![image](https://github.com/user-attachments/assets/66056a45-9f4b-4964-a8c4-ac3e370e94ad)
- İlk açıldığında boş olarak gelen her adımda değişen yapılan değişikliklerin kaydedildiği ve kullanıcıya bildirildiği ekran bu ekranın bir kaç değişiklikten sonra nasıl gözüktüğü altta belirtilmiştir.

![image](https://github.com/user-attachments/assets/f447af51-2e93-4b65-8ae5-638e18f1358b)
- 8 bitlik verinin seçildiği ve girildiği durumda ekran.

![image](https://github.com/user-attachments/assets/f73372a2-aa43-4fcf-b322-5caa419fa258)
- Aynı verinin girildikten sonra bir bitlik hata ile bozulduğu durumda ekran.

![image](https://github.com/user-attachments/assets/50b70953-f83a-427a-b072-42d8678c9e73)
- Bozulan kodun düzeltilmesi için tıklanıldığında gelen doğrulama ekranı.

![image](https://github.com/user-attachments/assets/25a3d999-00bc-4b97-ad78-65b2a8342846)
- Bozulan kodun düzeltilmesine verilen onay sonrasında kodun düzeltilmesi ve veriyi eski haline çevirme işlemi.

![image](https://github.com/user-attachments/assets/067e5d61-00b9-4890-b8da-71069f9c67b5)
- 32 bitlik başka bir verinin iki bitinin rastgele bozulması sonucu oluşan ekran.

![image](https://github.com/user-attachments/assets/9616f639-b04d-41e3-ac96-6312a31a5475)
- Üstte iki bitinin rastgele olarak bozulduğu 32 bitlik verinin düzeltilmesi için verilen komut sonrası oluşan ekran.






---


## 🔗 Tanıtım Videosu

- 🎥 Video Sunum: https://www.youtube.com/watch?v=-gV-d8igrlE&ab_channel=YunusAlimAvsar

---


