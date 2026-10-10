# L7e gereksinim ve doğrulama planı

## 1. L7e kapsamı

“L7 standartlı sürücü” tek bir entegre veya PCB standardı değildir. L7e araç kategorisi ve alt kategorisi, araç güç/ağırlık/yerleşim özellikleri ve hedef pazar tip onayı yoluyla belirlenir. 3,5 kW motor bulunması tek başına L7e sınıflandırmasını kanıtlamaz. Nihai uygunluk araç, batarya, kablo, muhafaza, inverter, yazılım ve test kayıtlarının birlikte değerlendirilmesini gerektirir.

Mevzuat ön taraması 10 Ekim 2026: (EU) 168/2013 için EUR-Lex'te 02/08/2026 konsolide sürümü erişilebilir. Elektrik tahrikli L kategorisi için UN R136 ve EMC için UN R10 resmî UNECE dizinlerinde yer alır. Bunlar tasarımın kapsam araştırması kaynaklarıdır. Ülke kabulü, geçiş tarihleri, uygulanacak amendment series ve muafiyetler teknik servisle teyit edilmeden “onaylı” denmez. Türkiye'de uygulanacak güncel ulusal tip onayı hükümleri bu çalışmada ayrıca doğrulanmamıştır.

| Konu | Ön kaynak | Tasarım sonucu / kanıt |
|---|---|---|
| Kategori ve araç tip onayı | (EU) 168/2013 ve ilgili delegasyon düzenlemeleri | L7e alt kategorisi, araç kapsamı, elektriksel güvenlik sorumluluğu |
| Elektrik tahrik güvenliği | UN R136; ilgili AB işlevsel güvenlik çerçevesi | Doğrudan/dolaylı temas, izolasyon, gövde bağlantıları, HV arayüzler, araç uyarıları |
| EMC tip onayı | UN R10, uygulanacak seri/kapsam | Araç veya elektronik alt sistem test planı; kablolar/şasi ile doğrulama |
| EMC mühendislik testleri | CISPR 25, ISO 11452 ailesi vb., uygun kapsam seçimi | Laboratuvar test yöntemleri; tek başına L7e onayı değildir |
| Besleme transientleri | ISO 7637/ISO 16750 veya ISO 21498 ailesi, gerilim alanına uygun kapsam | 12 V test darbeleri 72 V traction girişine aynen kopyalanmaz |
| İşlevsel güvenlik | ISO 26262 kapsam değerlendirmesi ve hazard analysis | ASIL veya sertifika varsayılmaz; unintended torque için bağımsız kontrol yolları |
| Çevre/mekanik | Uygun otomotiv çevre/IP/titreşim yöntemleri | Nem, su, sıcaklık, vibration, konektör ve izolasyon doğrulaması |

Bu standartların ücretli tam metinlerinin tüm maddeleri bu çalışmada okunmamıştır. Dolayısıyla madde numarası, kesin pass/fail limiti veya zorunlu revizyon uydurulmamıştır. R136/R10 güncel seri ve ulusal uygulanabilirlik matrisi nihai test planı öncesi doldurulacak açık girdidir.

## 2. Donanım gereksinimleri ve doğrulama matrisi

| ID | Gereksinim | Yöntem / kabul ölçütünü belirleyen girdi | Durum |
|---|---|---|---|
| H01 | Paketin tüm gerilim zarfına dayanım | Tam dolu paket, tolerans, regen/overshoot; her pin çalışma/mutlak maksimum marjı | Girdi bekliyor |
| H02 | Faz ve batarya akımı sınırları ayrı | Sürekli RMS/tepe/süre; sense transfer ve güç bütçesi | Girdi bekliyor |
| H03 | MOSFET termal kapasitesi | Sıcak RDS, switching/diyot kaybı, soğutucu ve ortam | Hesap + test |
| H04 | Güvenilir akım ölçümü | Offset/gain, iki yön, sıcaklık, ADC settling ve PWM pencereleri | Test planlandı |
| H05 | Faz OCP MCU'dan bağımsız | Her polarite, tüm PWM durumları, toplam fault gecikmesi/SOA | Kritik test |
| H06 | Shoot-through fault kapsaması | Shunt görünürlüğü, yerel DC-link kaynaklı kısa devre, hard disable | Kritik test |
| H07 | Reset/UVLO/enerjisiz gate-off | Power sequencing, MCU pinleri high-Z, driver ray kaybı | Kritik test |
| H08 | Dead-time/Miller kontrolü | Gerçek VGS/VDS; sıcaklık ve paralel MOSFET dağılımı | Çift darbe testi |
| H09 | Güvenli precharge | Vpack/Vdc farkı, timeout, açık direnç/kaynak kontaktör | Hata enjeksiyonu |
| H10 | DC-link deşarjı | Mevzuat/servis süre hedefi, C/R toleransı, fail durumu | Girdi bekliyor |
| H11 | Bara OV ve mekanik enerji | BMS charge reject, dönen motor, kontaktör açılması | Enerji analizi + test |
| H12 | Sigorta/kablo koordinasyonu | Paket fault akımı, DC kesme, I²t, kablo ısısı | Girdi bekliyor |
| H13 | DC-link ripple/ömür | Gerçek RMS, ESR/ESL, hotspot ve ömür eğrileri | Hesap + test |
| H14 | Hall doğru sıra ve ofset | 60°/120° türü, yön, besleme, invalid state ve filtre gecikmesi | Motor testi |
| H15 | Hall kaybında kontrol | Kablo açık/kısa, glitch, zaman aşımı; istenmeyen tork yok | Hata enjeksiyonu |
| H16 | Pedal iki kanal plausibility | LV alanı ADC, open/short, fren önceliği, açılış pedal yüksek | Araç entegrasyonu |
| H17 | Yön değişimi güvenliği | Hız/fren koşulu, reverse talebi, haberleşme hatası | Araç entegrasyonu |
| H18 | Heartbeat/watchdog güvenliği | Paket kaybı, MCU kilitlenmesi, supervisor fault → gate-off | Hata enjeksiyonu |
| H19 | Domain izolasyonu | HV–LV güç/veri/USB/şasi yolları, creepage ve yalıtım testi | Şema sonrası |
| H20 | Kasa/soğutucu izolasyonu | Drain tab, vida, nem, termal pad yaşlanması | Mekanik test |
| H21 | Sıcaklık teşhisi ve derating | NTC açık/kısa, motor sensörü uyumu, sensör→Tj modeli | Kalibrasyon + test |
| H22 | EMC emisyon ve bağışıklık | R10 kapsamı + mühendislik yöntemleri, gerçek kablo/muhafaza | Laboratuvar planı |
| H23 | Filtre kararlılığı | Giriş kaynak empedansı, inverter yük adımı, sönüm | Simülasyon + test |
| H24 | FOC donanım hazırlığı | 3-shunt pencereler, encoder/Hall açı, timer/ADC pin planı | Şema gate |
| H25 | Sıcaklık/su/titreşim | Araç ortam zarfı, IP hedefi, bağlantı dayanımı | Girdi bekliyor |

## 3. Doğrulama sırası

1. Şema/ERC inceleme: bütün güç ve referans alanları, driver enable polarity, fault propagation, kritik toleranslar ve pin mux.
2. MCU/PWM güçsüz test: boot/reset/watchdog, fault kilidi, bütün six-step durumlarında çapraz iletim engeli. Motor Hall tablosu ölçümle çıkarılır.
3. Düşük gerilim ve akım sınırlı kaynak: sense offset/gain, Hall sıra/ofset, akım döngüsü ve Vdc ölçümü. Tam paketle ilk açılış yapılmaz.
4. Half-bridge çift darbe/gate testi: diferansiyel/izole prob ve uygun fixture ile VGS/VDS, ringing, overshoot, driver negatif transient ve paralel paylaşımı. Rastgele osiloskop GND'sini BAT−'a bağlama.
5. Artan yükte bench/dinamometre: faz/batarya akımı, input/shaft power, sıcaklık, ripple ve altı adımlı kontrol. Motor/kaynak/fixture sınırları aşılmadan.
6. Fault enjeksiyonu: sensör/kablo/besleme/watchdog/enable/Hall/OV senaryoları. Enerjili kısa devre testleri ölçüm ve korumalı laboratuvar planıyla yürütülür; 1243 A kilitli rotor değeri hedef test akımı değildir.
7. Kontrol edilen araç entegrasyonu: BMS/VCU, precharge/kontaktör, fren/pedal/yön, gövde izolasyonu ve fault kaydı.
8. FOC karşılaştırması: aynı motor, DC gerilim, hız, yük, ortam ve soğutma. Aynı duty veya aynı batarya akımı eşit mekanik çıktı demek değildir.
9. EMC/çevre ön uygunluk → güncel tip onayı kapsamı doğrulanmış laboratuvar testleri.

## 4. Six-step / FOC karşılaştırmasında kaydedilecekler

Pbat = Vbat × Ibat; Pshaft = T × ω; sistem verimi = Pshaft/Pbat. Faz RMS ve tepe akımları, motor/FET/DC-link sıcaklıkları, tork ripple, ses, düşük hız başlatma ve aynı yükte hata davranışı kaydedilir. Paylaşılan tabloda inverter kaybı sıfır olduğu için %90,4323 değeri bu karşılaştırmanın ölçülmüş sistem sonucu olarak kullanılamaz.

FOC/SVPWM kullanılması R10 veya R136 uygunluğunu kanıtlamaz. AEC-Q100/Q101 parçalar da tek başına sürücü/araç onayı değildir. İlk prototip için katalog MCU/MOSFET adayları ile araç sürümü için kalifikasyon gereksinimleri BOM'da açık tutulur.
