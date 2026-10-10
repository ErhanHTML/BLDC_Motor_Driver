# 72 V BLDC motor sürücüsü — donanım ön tasarımı

İlk prototip: **Hall sensörlü, kapalı çevrim akım kontrollü six-step**. Sonraki prototip: aynı üç faz güç köprüsü ve akım ölçümüyle **FOC + SVPWM**.

Bu çalışma 10 Ekim 2026 tarihinde paylaşılan blok diyagramı ve motor sonuç tablosuna göre hazırlanmıştır. Depoda üretime hazır Altium şeması, PCB veya motor test verisi bulunmadığından inceleme mimari düzeydedir. Aşağıdaki adaylar satın alma onayı veya L7e tip onayı anlamına gelmez. Özellikle bataryanın tam dolu gerilimi, motor faz akımı ve termal sınırlar henüz doğrulanmamıştır.

## Dosyalar

| Dosya | İçerik |
|---|---|
| [Ön inceleme](docs/01-review.md) | Motor verileri, diyagramdaki hatalar/eksikler, açık girdiler |
| [Donanım tasarım kılavuzu](docs/02-hardware-guide.md) | Güç köprüsü, sürücüler, besleme, ölçüm, koruma, PCB ve soğutma |
| [Blok diyagramları](docs/03-diagrams.md) | Güç yolu, kontrol, donanımsal kapatma ve izolasyon alanları |
| [Ön BOM](hardware/BOM.md) | Parça adayları, miktarlar, seçim koşulları, fiyat/tedarik durumu |
| [L7e gereksinim ve test matrisi](docs/04-validation-and-L7e.md) | Araç düzeyi mevzuat kapsamı, doğrulama ve prototip geçişi |
| [Kaynaklar](docs/05-sources.md) | Üretici dokümanları ve resmî mevzuat bağlantıları |
| [Hesap örnekleri](scripts/preliminary_calculations.py) | Tekrarlanabilir boyutlandırma örnekleri; gerçek motor modeli değildir |

## Önerilen başlangıç mimarisi

- STM32G474RE sınıfı MCU; 6 PWM, senkron ADC, donanımsal timer break, Hall ve encoder bağlantı alanı.
- Üç low-side Kelvin shunt + üç çift yönlü akım yükselteci; ayrı DC giriş akımı ölçümü.
- 150 V MOSFET sınıfı aday güç köprüsü. MOSFET paralel sayısı sıcaklık ve faz akımıyla belirlenecek.
- Gerilim marjı için üç UCC21520-Q1 çift kanal izole gate driver adayı; high-side başına yüzer besleme. İzole gate driver tek başına araç izolasyonunu sağlamaz.
- Alternatif: üç UCC27301A-Q1 bootstrap driver. HB pin gerilimi bara + gate beslemesidir; 120 V etiketi 120 V bara izni değildir. Paket/enable farkına dikkat.
- Dahili kontrol alanı BAT− referanslı; araç LV/şasi alanına haberleşme ve kullanıcı I/O üzerinden galvanik köprü kurulmayacak.
- Precharge, kontaktör/BMS izinleri, DC-link deşarjı, bağımsız OCP/fault latch ve sıcaklık derating.

İlk prototipte alan zayıflatma ve rejenerasyon devre dışı tutulur. Bu, dönen motorun gövde diyotları üzerinden DC-link'i yükseltemeyeceği anlamına gelmez; bara aşırı gerilim senaryosu yine ele alınmalıdır.

## Önce kapatılacak kararlar

1. Batarya kimyası, seri hücre sayısı, maksimum şarj gerilimi, BMS akım/regen sınırları.
2. Motor üretici/modeli, faz R/L, kutup çifti sayısı, geri EMK biçimi ve Hall sırası/açısı.
3. 50 A değerinin batarya akımı mı, faz RMS akımı mı olduğu; kalkış akımı ve izin verilen süresi.
4. Araç sınıfı (L7e alt kategorisi), hedef ülke/tip onayı yolu ve uygulanacak mevzuat revizyonları.
5. Ortam sıcaklığı, soğutucu, muhafaza/IP hedefi, kablo ve konektör sınırları.

Bu bilgiler olmadan kesin MOSFET adedi, DC-link kapasitesi, sigorta değeri veya nihai BOM dondurulmaz.
