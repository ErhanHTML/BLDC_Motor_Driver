# Ön BOM — donanım öneri listesi

Bu belge kesin sipariş listesi değildir. **DRV serisi kullanılmayacaktır.** Parça numaraları, ölçülmüş gereksinimler ve güncel datasheet ile doğrulandıktan sonra belirlenecektir.

| Alt sistem | Öneri / miktar | Seçim kontrolü |
|---|---|---|
| Güç köprüsü | Üç half-bridge; toplam altı anahtar konumu | Elektriksel/termal zarf, paket, SOA, parazitikler |
| Gate-driver | **Üç ayrı çift kanallı entegre; her faza bir adet** | High-side yöntemi, UVLO, CMTI, PWM arayüzü, güvenli kapatma |
| Gate ağı | Her anahtar için sürüş ve deşarj bileşenleri | Gate charge, açma-kapama ve Miller davranışı |
| DC-link | Bulk + yerel film/seramik bank | RMS ripple, ESR/ESL, gerilim marjı, yerleşim |
| MCU | Motor kontrol zamanlayıcılı STM32 adayı | Tamamlayıcı PWM, break, ADC tetikleme, Hall/encoder |
| Faz akım ölçümü | Üç kanal için yer ayrılması önerilir | Örnekleme, bant genişliği, ofset, koruma |
| DC-link / bus ölçümü | Akım ve gerilim geri beslemesi | İzleme/koruma için aralık ve doğruluk |
| Donanım fault | Comparator/latch/shutdown bloğu | MCU'dan bağımsız kapatma |
| Sıcaklık | Güç katı ve motor sensör girişleri | Aralık, kalibrasyon, fail-safe |
| Hall | Üç dijital giriş + koruma | Kablo paraziti, ESD, lojik seviye |
| Haberleşme | Uygun transceiver ve konnektör | Gürültü/izolasyon ve araç arayüzü |
| AUX güç | Kontrol ve gate besleme blokları | Başlatma, UVLO, izolasyon, güç bütçesi |
| Mekanik/PCB | Konnektör, montaj ve soğutma alanları | Creepage/clearance, termal yol, servis |

Parça sayısı ve kesin MPN şema/ERC, termal çalışma, fault mantığı ve PCB gözden geçirmesinden sonra yayımlanır.
