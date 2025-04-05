# 🔐 Fibonacci-Kaos Şifreleme Uygulaması

Bu proje, Flask ile geliştirilmiş bir web uygulamasıdır. Fibonacci dizisi ve Kaos teorisi (logistic map) kullanılarak metin şifreleme ve çözme işlemleri yapılır.

## 🚀 Özellikler

- Maksimum 256 bayta kadar metin şifreleme
- Fibonacci + Kaotik haritalama ile dinamik anahtar üretimi
- HEX formatında şifreleme çıktısı
- Türkçe karakter desteği

## 🛠 Kurulum

```bash
git clone https://github.com/kullanici_adi/fibonacci-kaos-sifreleme.git
cd fibonacci-kaos-sifreleme
pip install -r requirements.txt
python app.py
```

## 💡 Kullanım

- Anasayfada metni girerek şifreleyebilir, çıkan HEX kodunu çözme sekmesinde tekrar çözebilirsiniz.
- Gelişmiş karakter kontrolü ile Türkçe karakterlerde bayt sınırı uyarısı verir.

## 📁 Klasör Yapısı

- `app.py` – Ana Flask uygulaması
- `templates/` – HTML dosyaları
- `static/` – CSS dosyası
- `requirements.txt` – Gerekli paketler
- `.gitignore` – Gereksiz dosyaları dışlar

---
