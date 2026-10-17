# Ön BOM — entegre kart revizyonu

Aday gereksinim listesi; kesin sipariş BOM'u değildir. Görselin çizdiği her pasif elemanın elektriksel değeri bilinmez. **DRV serisi kullanılmaz.** Detay: [Entegre kart notu](../docs/09-integrated-board-revision.md).

| Blok | Yerleşim adayı | İnceleme ölçütü |
|---|---|---|
| DC giriş / koruma | konnektör, sigorta/ayırma, precharge ve deşarj değerlendirmesi | giriş transient, kablo, güvenlik |
| EMI | filtre ve gerekli sönüm; opsiyonel elemanlar TBD | rezonans, şasi/IMD uyumu, EMC |
| DC-link | bulk bank + köprüye yakın yerel film/seramik | gerilim, ESR/ESL, RMS ripple, ömür |
| Güç katı | üç half-bridge, altı MOSFET konumu | RDS(on) sıcaklık, SOA, Qg, mekanik/termal |
| Gate-driver | **faz başına 1 çift çıkışlı; toplam 3** | yüzer high-side, UVLO, CMTI, kapatma |
| Gate pasifleri | sürücü başına bypass / gate ağı / varsa bootstrap | üretici önerisi ve transient |
| Kart içi buck | DC girişten 12 V kontrolcü, indüktör, diyot (topolojiye göre), CIN/COUT, FB/EN, gerekli kompanzasyon | maksimum giriş + transient, 12 V yük bütçesi, termal |
| Düşük gerilim | 12→5 V ve 5→3,3 V regülasyon, bypass/filtre | MCU/Hall/sensör güç bütçesi |
| MCU | STM32 motor-control adayı | altı PWM, ADC trigger, break, Hall, debug |
| Faz akım algılama | kart üstünde üç kanal rezervi / AFE | FOC zamanlama, ofset, Kelvin, aşırı akım |
| DC-link algılama | kart üstü bus akım/gerilim | aralık, ADC, koruma |
| Fault | karşılaştırıcı/latch, gate shutdown, watchdog | MCU'dan bağımsız fail-safe |
| Hall | tek Hall konnektörü, giriş koruma/filtre | seviye, ESD, gecikme |
| Sıcaklık | kart üstü/uygun motor sensör arayüzü | kalibrasyon, fail-safe |
| Servis | SWD/programlama ve seçilecek temel kontrol arayüzleri | pin bütçesi / ESD |
| Mekanik | 160 × 120 mm referans kart alanı | konnektör, soğutma ve clearance |

**Bu revizyonda BOM'dan çıkarılacaklar:** harici AUX besleme konnektörü, CAN transceiver/konnektörü, RS485 transceiver/konnektörü, harici akım ölçüm konnektörü. Akım ölçüm devreleri çıkarılmaz.

100 nF = 0,1 µF gibi tipik bypass değerleri, yalnız uygulama şeması ve gerilim/derating kontrolünden sonra net MPN/0805 alanlarına atanmalıdır.
