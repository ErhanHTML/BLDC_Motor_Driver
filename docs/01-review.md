# Motor verileri ve mevcut diyagram incelemesi

## 1. Kaynak ve sınırlar

Kullanıcı girdisi: 72 V batarya, yaklaşık 3,5 kW motor, nominal yaklaşık 50 A ve ilk prototipte Hall sensörlü six-step. İncelenen görseller: `image(20261009-193224).png` (blok diyagram), `image(20261009-193330).png` (motor sonuçları). Sonuç tablosunun üretici ölçümü mü yoksa simülasyon mu olduğu bilinmiyor. Satırlar doğrulanmış motor datasheet'i olarak kabul edilmemiştir.

| Parametre | Görseldeki değer | Tasarım yorumu |
|---|---:|---|
| Demir kaybı | 93,504 W | Sürücü kaybı değildir |
| Sargı bakır kaybı | 223,94 W | Termal motor doğrulamasında kullanılacak ön veri |
| Transistör/diyot kaybı | 0 | İnverter kayıpları hesaba katılmamış görünüyor |
| Toplam kayıp | 317,44 W | 93,504 + 223,94 ile yuvarlama düzeyinde tutarlı |
| Çıkış gücü | 3000,4 W | Kullanıcının yaklaşık 3,5 kW ifadesinden farklı çalışma noktası |
| Giriş gücü | 3317,8 W | Motor girişinin tanımı doğrulanmalı |
| Verim | %90,4323 | 3000,4 / 3317,8 ile tutarlı; bataryadan mile sistem verimi olduğu kanıtlanmış değil |
| Anma hızı | 528,597 rpm | Motor mili/teker veya redüksiyon sonrası olup olmadığı bilinmiyor |
| Anma torku | 54,203 Nm | P = T × 2πn/60 ≈ 3000,4 W ile tutarlı |
| Kilitli rotor torku | 740,403 Nm | Sürücüde izin verilen kalkış torku değildir |
| Kilitli rotor akımı | 1243,8 A | Gerçek uygulanabilir sınır değil; sürücü akımı aktif sınırlamalı |
| Maksimum çıkış gücü | 4979 W | Süresi/soğutması/beslemesi bilinmiyor; sürekli güç kabul edilmez |

3317,8 / 72 ≈ 46,08 A yalnızca bu gücün 72 V DC girişten alındığı varsayımıyla hesaplanabilir. 72 × 50 = 3600 W elektriksel giriş. %90,4323 verimle yaklaşık 3255,6 W çıkış, inverter kaybı hariç. 3500 W mil gücü aynı motor veriminde yaklaşık 3870 W motor girişi ister; sürücü kaybı da eklenir. Faz akımını bu bölme işlemlerinden çıkarmak doğru değildir.

## 2. Diyagramdaki hatalar ve eksikler

Buradaki “hata” elektrik bağlantısı kanıtlanmış yanlışlık ile çizimde gösterilmeyen fonksiyonu ayırır. Bir blok diyagramdan pin bağlantısı, MOSFET yönü veya layout hatası kesinleştirilemez.

| ID | Bulgu | Yapılacak değişiklik | Öncelik |
|---|---|---|---|
| R01 | “Power MOS drain for each phase” belirsiz | Yalnız high-side drain DC+ olur; HS source/LS drain faz düğümüdür; LS source shunt üzerinden DC−'a gider | Kritik |
| R02 | Faz akımı geri beslemesi çizilmemiş | Üç low-side shunt, Kelvin hatları, çift yönlü yükselteçler ve senkron ADC ekle | Kritik |
| R03 | Yazılımdan bağımsız OCP yok | Hızlı karşılaştırıcı/pencere, fault latch, gate disable ve timer break yolu ekle | Kritik |
| R04 | Sigorta/precharge/kontaktör/deşarj yok | Araç BMS/VCU sahipliğini belirle; inverter DC-link ön şarjını ve ölçümünü göster | Kritik |
| R05 | 72 V yalnız nominal değer | Maksimum paket gerilimi, regen ve parazitik darbe zarfını belirle | Kritik |
| R06 | 12/5/3,3 V besleme çizimi gate beslemesini belirtmiyor | Gate driver için 10–12 V aday ray; high-side yüzer besleme veya bootstrap göster | Yüksek |
| R07 | STM32–şasi–BAT− ilişkisi yok | HV kontrol alanı ile araç LV alanının izolasyon sınırını çiz | Kritik |
| R08 | Throttle/gear tek hat | Pedal iki kanal plausibility, fren önceliği, yön değiştirme kilidi, açık/kısa kablo teşhisi ekle | Kritik |
| R09 | Hall filtre gecikmesi tanımsız | ESD + pull-up/level shift + küçük RC + Schmitt; gecikmeyi elektriksel hıza göre sınırla | Yüksek |
| R10 | RS485 tek başına araç arayüzü | CAN bağlantısı adayı ekle; RS485 gerekiyorsa ayrı fiziksel port/izolasyon | Orta |
| R11 | RC snubber her faz üzerinde seri blok gibi | Snubber seri güç elemanı değildir; uygun düğümlere paralel RC yerleştir ve çınlamadan boyutlandır | Yüksek |
| R12 | 5 sıcaklık sensörü var ama yer/limit yok | FET bankası/soğutucu/motor konumlarını, sensör türünü, derating ve fault eşiğini tanımla | Yüksek |
| R13 | EMI filtresi yalnız not olarak var | Giriş DM/CM yolu, sönüm, DC-link ve şasi kapasitansı/IMD etkileşimini birlikte tasarla | Yüksek |
| R14 | Fault/ready/watchdog çizilmemiş | Gate-off varsayılanı, harici watchdog, VCU heartbeat ve BMS enable ekle | Kritik |
| R15 | SWG yazısı belirsiz | SWD kastediliyorsa SWDIO/SWCLK/NRST/GND; HV referanslı debug bağlantısı için izolasyon tanımla | Orta |
| R16 | Gate direnci/pull-down/dead-time yok | Her MOSFET için ayrı gate direnci, kaynak dönüşü, VGS koruması ve dead-time ekle | Kritik |
| R17 | DC-link akım/ripple ölçütü yok | Kapasite yanında RMS ripple, ESR/ESL, sıcaklık ve ömür hesabı yap | Yüksek |
| R18 | Motor kablosu/ekran/şasi ilişkisi yok | Faz/Hall güzergâhı ayrımı, ekran sonlandırma ve gövde bağlantısını tanımla | Yüksek |

## 3. Şema başlamadan istenecek motor bilgileri

- Tam model, üretici datasheet'i, bağlantı yıldız/üçgen ve faz uçları.
- Faz-faz DC direnç (ölçüm sıcaklığıyla), faz-faz endüktans ve ölçüm frekansı. Yıldız için faz-faz R/2 dönüşümü kullanılabilir; üçgen için aynı dönüşüm uygulanmaz.
- Kutup çifti sayısı p: f_e = p × rpm / 60. 528,6 rpm tek başına PWM/filtre tasarımına yetmez.
- Geri EMK dalga şekli ve K_e tanımı (faz/faz-faz, RMS/tepe, hız birimi).
- K_t ve akım tanımı; termal limitler, motor sensörü, demanyetizasyon ve hız sınırları.
- Hall besleme, open-collector/push-pull, 60°/120° yerleşim ve elektriksel ofset.
- Sürekli faz RMS, faz tepe ve süreye bağlı kalkış akımı. Kilitli rotor tablosundan limit türetilmez.

## 4. Six-step ile FOC kararının kapsamı

İlk sürüm Hall ile komütasyon + ölçülen akımla PWM kontrolüdür. Yalnız duty ayarlayıp batarya akımına bakmak, faz akımını her koşulda korumaz. Sonraki FOC sürümünde Clarke/Park, rotor açı kestirimi, d/q PI ve SVPWM eklenir. Güç köprüsü prensipte korunur; akım örnekleme pencereleri, Hall açı kalibrasyonu ve işlem süresi ölçülür. Trapezoidal geri EMK'de standart sinüzoidal FOC'nin otomatik verim/tork üstünlüğü kabul edilmez; aynı çalışma noktalarında ölçülür.
