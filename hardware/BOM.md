# Ön BOM — 72 V Hall six-step / FOC geçişi

Revizyon A, 10 Ekim 2026. Bir sürücü için planlama listesi. Kesin sipariş listesi değildir. Ana mimari: BAT− referanslı kontrol, üç izole çift kanal gate driver, üç bağımsız high-side besleme ve izole araç I/O. Bootstrap alternatifi aynı anda monte edilmez ve pin uyumlu değildir.

Miktarlar ön yerleşim içindir. DNP = alan ayrılır, ilk montajda takılmaz. TBD = değer/MPN henüz seçilmedi. Aday ürünlerin resmî bağlantıları verilmiştir; stok, güncel fiyat, vergi, teslimat ve paket varyantı araştırılmadığından fiyatlar **TBD** bırakılmıştır. Sıfır fiyat, bedelsiz anlamı oluşturacak şekilde kullanılmamıştır. Birim fiyat × miktar ile toplam fiyat ancak teklif alındığında hesaplanır. Bu liste pasiflerin bütün şema referanslarını içermez; tam BOM, şema tamamlandıktan sonra dışa aktarılır.

## A. Kontrol ve sürüş entegreleri

| ID | Ürün tipi | Part number / aday | Ürün linki | Miktar | Birim fiyat | Toplam fiyat | Açıklama / seçim kapısı |
|---|---|---|---|---:|---|---|---|
| B01 | MCU | STM32G474RET6 adayı | [ST](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html) | 1 | TBD | TBD | Six-step/FOC; paket pin planı ve otomotiv niteliği doğrulanmalı |
| B02 | İzole dual gate driver | UCC21520-Q1 ailesi | [TI](https://www.ti.com/product/UCC21520-Q1) | 3 | TBD | TBD | Ana aday; tam ordering code/UVLO/paket seçilecek |
| B03 | High-side izole DC/DC | TBD, 12→12 V | — | 3 | TBD | TBD | Faz source referanslı 3 yüzer ray; izolasyon, CMTI, kapasitans ve güç bütçesi seçilecek |
| B04 | Low-side CSA | INA240A1-Q1, gain 20 | [TI](https://www.ti.com/product/INA240-Q1) | 3 | TBD | TBD | 0,5 mΩ örneğiyle ±100 A aday aralık; yalnız low-side |
| B05 | Hızlı karşılaştırıcı | TLV3201-Q1 | [TI](https://www.ti.com/product/TLV3201-Q1) | 6 | TBD | TBD | Faz başına pozitif/negatif eşik; fault yolu gecikme hesabı bekleniyor |
| B06 | Fault latch ve gate mantığı | TBD, fail-safe logic | — | 1 set | TBD | TBD | OCP/OV/enable/watchdog birleşimi; reset güvenli kapalı |
| B07 | Harici watchdog/supervisor | TPS3850-Q1 | [TI](https://www.ti.com/product/TPS3850-Q1) | 1 | TBD | TBD | MCU reset yanında gate kapatma bağımsız yolu |
| B08 | CAN transceiver | ISO1042-Q1 | [TI](https://www.ti.com/product/ISO1042-Q1) | 1 | TBD | TBD | İki izolasyon alanının beslemeleri ayrı; termination/TVS ayrıca |
| B09 | İzin/fault dijital izolasyonu | ISO7721-Q1 ailesi | [TI](https://www.ti.com/product/ISO7721-Q1) | TBD | TBD | TBD | Kanal yönü/power-off varsayılanı; safety enable/fault ihtiyacına göre |
| B10 | İzole RS485, opsiyon | ISO1410 | [TI](https://www.ti.com/product/ISO1410) | 0–1 | TBD | TBD | DNP; katalog adayı, otomotiv niteliği doğrulanmadı |
| B11 | Hall Schmitt/level shift | TBD, 3 kanal | — | 1 set | TBD | TBD | 5 V Hall türüne göre 3,3 V lojik; fail state ve ESD |
| B12 | Pedal LV ön uç / izole veri | TBD, çift kanal | — | 1 set | TBD | TBD | VCU okuyorsa inverter üzerinde DNP; iki kanal plausibility |
| B13 | 1,65 V referans/buffer | TBD | — | 1 set | TBD | TBD | CSA REF ve ADC bütçesi; tolerans/gürültü hesabı |

## B. Güç ve pasifler

| ID | Ürün tipi | Part number / aday | Ürün linki | Miktar | Birim fiyat | Toplam fiyat | Açıklama / seçim kapısı |
|---|---|---|---|---:|---|---|---|
| B14 | Güç MOSFET | IPB057N15NM6 | [Infineon](https://www.infineon.com/part/IPB057N15NM6) | 12 aday | TBD | TBD | 150 V; 2 paralel/anahtar ön alanı. AEC-Q101 doğrulanmadı, araç sürümü alternatifi seçilecek |
| B15 | Gate on/off direnç | TBD | — | 12–24 | TBD | TBD | Her MOSFET ayrı; Rg-off diyot yolu opsiyon |
| B16 | Gate-source pull-down | TBD | — | 12 | TBD | TBD | Açılış/driver enerjisizken kapalı durum |
| B17 | Gate clamp | TBD, MOSFET VGS'ye uygun | — | 12 aday | TBD | TBD | Parazitik yük ve clamp toleransı doğrulanmalı |
| B18 | Kelvin low-side shunt | TBD, 0,5 mΩ aday | — | 3 | TBD | TBD | Düşük TCR, yeterli RMS/pulse güç; 100 A sürekli örneğinde 5 W |
| B19 | DC giriş akım sensörü | TBD, çift yönlü / izole Hall | — | 1 | TBD | TBD | Batarya akımı/log/regen; faz ölçümünün yerine geçmez |
| B20 | Elektrolitik DC-link bank | TBD, 160 V sınıfı | — | TBD | TBD | TBD | Toplam kapasite, RMS ripple, ESR, ömür ve yerleşim hesaplanacak |
| B21 | Yerel film DC-link cap | TBD, uygun 160–250 V sınıfı | — | 3 aday | TBD | TBD | Half-bridge komütasyon halkasına yakın; akım/dvdt sınıfı |
| B22 | HV seramik decoupling | TBD, 200 V sınıfı aday | — | TBD | TBD | TBD | DC-bias/ESL/çatlak riski; C0G/X7R seçimi uygulamaya göre |
| B23 | RC snubber | TBD R + C | — | 3–6 alan | TBD | TBD | DNP başlangıç, ringing ölçümü sonrası |
| B24 | Bara TVS/clamp | TBD | — | TBD | TBD | TBD | Vstandoff > Vpack_max; Vclamp < en düşük parça limiti; fren enerjisi için değil |
| B25 | Giriş DM filtre | TBD L/C + sönüm | — | 1 set | TBD | TBD | Akım/satürasyon ve kaynak-inverter stabilitesi |
| B26 | Giriş CM choke | TBD | — | 0–1 | TBD | TBD | Ölçüm sonrası, kaçak endüktans/DC ve kablo EMC'si |
| B27 | Şasi kapasitörleri | TBD, uygun güvenlik sınıfı | — | 0–2 | TBD | TBD | DNP başlangıç; IMD/kaçak kapasitesi ve izolasyon hesabı |
| B28 | Gate/sense decoupling RC/C | TBD | — | 1 set | TBD | TBD | Datasheet yerleşim kuralları; tam adet şemadan çıkacak |

## C. Yardımcı besleme

| ID | Ürün tipi | Part number / aday | Ürün linki | Miktar | Birim fiyat | Toplam fiyat | Açıklama / seçim kapısı |
|---|---|---|---|---:|---|---|---|
| B29 | HV→12 V buck controller | LTC3895 | [ADI](https://www.analog.com/en/products/ltc3895.html) | 1 | TBD | TBD | 140 V çalışma; harici FET/L/C gerektirir, otomotiv niteliği doğrulanmadı |
| B30 | Buck harici MOSFET/L/C/sense | TBD | — | 1 set | TBD | TBD | Giriş zarfı, 12 V güç bütçesi, ripple ve termal hesap |
| B31 | 12→5 V buck | TPS62130A-Q1 | [TI](https://www.ti.com/product/TPS62130A-Q1) | 1 | TBD | TBD | Harici L/C dahil; gerçek 12 V zarfı ve akım gereksinimi |
| B32 | 5→3,3 V regülatör | TBD, automotive LDO/buck | — | 1 | TBD | TBD | MCU/ADC rayı, dropout ve termal bütçe |
| B33 | Araç LV arayüz besleme | Araç LV veya TBD izole DC/DC | — | 1 alan | TBD | TBD | İzolasyon bariyerini güç yolu üzerinden bypass etmemeli |
| B34 | Analog filtre/reference C/R | TBD | — | 1 set | TBD | TBD | ADC/CSA temiz ray ve referans kararlılığı |

## D. Araç, bağlantı ve mekanik

| ID | Ürün tipi | Part number / aday | Ürün linki | Miktar | Birim fiyat | Toplam fiyat | Açıklama / seçim kapısı |
|---|---|---|---|---:|---|---|---|
| B35 | DC sigorta ve yuva | TBD | — | 1 | TBD | TBD | DC kesme kapasitesi, paket kısa devre akımı, I²t ve kablo koordinasyonu |
| B36 | DC kontaktör | TBD | — | Araç mimarisine göre | TBD | TBD | BMS/VCU sahipliği; welded-contact feedback ve DC kesme sınırı |
| B37 | Precharge relay/anahtar | TBD | — | 1 | TBD | TBD | DC yük, fault ve ana kontaktör bypass kolu |
| B38 | Precharge direnç | TBD pulse-rated | — | 1 | TBD | TBD | 100 Ω yalnız örnek; enerji/timeout/tekrar süresiyle seçilir |
| B39 | Deşarj direnç/aktif anahtar | TBD | — | 1 set | TBD | TBD | Bus safe-voltage süresi ve fail durumları |
| B40 | Fren kıyıcı + direnç | TBD | — | 0–1 set | TBD | TBD | Alan ayrılır; enerji kabul etmeyen paket/overspeed analizinden sonra |
| B41 | Sıcaklık sensörleri | TBD NTC/PT1000 vb. | — | 5 aday | TBD | TBD | Görseldeki 4 güç/soğutucu + 1 motor; konum ve motor sensörü türü doğrulanacak |
| B42 | Hall/NTC ESD ve filtre | TBD | — | 1 set | TBD | TBD | Kablo girişi TVS, bias, RC ve seviye uyumu |
| B43 | CAN terminasyon/TVS/CMC | TBD | — | 1 set | TBD | TBD | Uç konumuna göre 120 Ω; fault gerilim zarfı |
| B44 | HV güç ve motor konektörü | TBD | — | 1 batarya + 1 üç faz set | TBD | TBD | Gerilim, akım, sıcaklık, IP, kilitleme ve touch protection |
| B45 | LV/Hall/pedal konektörleri | TBD | — | TBD | TBD | TBD | Domain ayrımı, yanlış takma koruması, pin dizilimi |
| B46 | Busbar/kablo/krimp | TBD | — | 1 set | TBD | TBD | Faz tepe/RMS ve batarya akımı ayrı; izolasyon ve strain relief |
| B47 | PCB | TBD stack-up/bakır | — | 1 | TBD | TBD | Akım/termal/creepage; busbar gerekiyorsa sırf kalın bakıra güvenme |
| B48 | Soğutucu/TIM/yalıtkan vida | TBD | — | 1 set | TBD | TBD | Drain tab→şasi izolasyonu, termal R, nem/vibration |
| B49 | Muhafaza/rakor/ekran bağlantısı | TBD | — | 1 set | TBD | TBD | IP/EMC ve servis erişimi |
| B50 | SWD/test konektörü | TBD | — | 1 | TBD | TBD | HV referanslı debug için izolasyon; araçta açık erişim yok |

## E. Alternatifler — ana BOM'a eklenmez

| Aday | Kullanım | Seçim koşulu |
|---|---|---|
| [UCC27301A-Q1](https://www.ti.com/product/UCC27301A-Q1), 3 adet | Bootstrap half-bridge driver | HB ≈ Vbus + 12 V ve overshoot; DRC enable durumu, duty/yenileme doğrulanmalı |
| [UCC27211A-Q1](https://www.ti.com/product/UCC27211A-Q1), 3 adet | Alternatif half-bridge driver | Bağımsız donanım gate-off/HI-LI mantığı ve aynı HB marjı gerekir |
| [DRV8353](https://www.ti.com/product/DRV8353), 1 adet | Entegre üç faz driver + CSA | 100 V sınıfı; ölçülmüş tüm pin gerilim zarfı uygun olursa. Otomotiv niteliği ayrıca |
| [LM5164-Q1](https://www.ti.com/product/LM5164-Q1) | Düşük güçlü 100 V auxiliary buck | 1 A çıkış ve 100 V giriş marjı/güç bütçesi uygun olursa |
| [LM5146-Q1](https://www.ti.com/product/LM5146-Q1) | Harici MOSFET'li 100 V buck | Giriş zarfı sıkı sınırlıysa; 140 V adayın pin uyumlu alternatifi değil |
| Encoder A/B/Z | FOC açı geri beslemesi | Hall interpolasyonunun performansı yetersizse; pin/connector/izolasyon alanı P0'da ayrılacak |

## Satın alma için dondurma kontrolü

Tam ordering code → üretici datasheet/revizyon → voltage/current/thermal derating → paket/footprint → automotive qualification → stok/fiyat/teslimat → alternatifin pin/işlev uyumu kontrol edilir. Aynı “150 V” etiketi veya aynı gate sürücü fonksiyonu drop-in uyumluluk sağlamaz. Nihai pasif değerleri ve birim fiyatlar açık kalırken toplam bütçe verilmez.
