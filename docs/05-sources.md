# Kaynaklar ve kanıt kapsamı

İnceleme tarihi: 10 Ekim 2026. Sayfalar ürün özelliklerini ve mevzuat kapsamını araştırmak için kullanılmıştır. Kaynaklar, burada yapılan ön tasarım hesaplarını veya belirli aracın uygunluğunu onaylamaz. Satın alma öncesinde güncel datasheet, ordering code ve qualification raporu kontrol edilir.

## Kullanıcı girdileri

- `image(20261009-193224).png`: mevcut blok diyagram, başlıca besleme/köprü/STM32/Hall/RS485 yapısı.
- `image(20261009-193330).png`: motor güç/kayıp/hız/tork/locked-rotor sonuç tablosu.
- Kullanıcı talebi: 72 V batarya, yaklaşık 3,5 kW motor, yaklaşık 50 A nominal, Hall six-step ilk prototip, FOC/SVPWM sonraki sürümler, L7 araç hedefi.
- Görseller üretici datasheet'i değildir. Motor model/sensör/phase current ve batarya kimyası bilinmiyor.

## Üretici kaynakları

| Ref | Resmî kaynak | Desteklediği seçim bilgisi |
|---|---|---|
| S01 | [STM32G474RE](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html) | Motor PWM/ADC/matematik hızlandırma/FDCAN özellikleri |
| S02 | [ST motor control ecosystem](https://www.st.com/content/st_com/en/ecosystems/stm32-motor-control-ecosystem.html) | Six-step ve FOC geliştirme ekosistemi; donanım pin planı yerine geçmez |
| S03 | [UCC21520-Q1](https://www.ti.com/product/UCC21520-Q1) / [datasheet](https://www.ti.com/lit/ds/symlink/ucc21520-q1.pdf) | İzole dual gate driver, disable/dead-time, besleme özellikleri |
| S04 | [UCC27301A-Q1](https://www.ti.com/product/UCC27301A-Q1) / [datasheet](https://www.ti.com/lit/ds/symlink/ucc27301a-q1.pdf) | HB 120 V abs max, UVLO/interlock; EN sadece DRC paket (§4/§5) |
| S05 | [UCC27211A-Q1](https://www.ti.com/product/UCC27211A-Q1) | Alternatif half-bridge driver; ayrı fault/enable mantığı gerekir |
| S06 | [DRV8353](https://www.ti.com/product/DRV8353) / [datasheet](https://www.ti.com/lit/ds/symlink/drv8353.pdf) | Üç faz smart driver, CSA ve PWM seçenekleri; 100 V sınıfı marj kontrolü |
| S07 | [STSPIN32G4](https://www.st.com/en/motor-drivers/stspin32g4.html) | Entegre motor kontrol seçeneği; güç gerilimi sınırı kontrol edilir |
| S08 | [IPB057N15NM6](https://www.infineon.com/part/IPB057N15NM6) | 150 V D²PAK MOSFET adayı; otomotiv qualification iddiası yapılmadı |
| S09 | [INA240-Q1](https://www.ti.com/product/INA240-Q1) | Bidirectional/PWM rejection, -4…80 V common-mode; yalnız önerilen low-side konum |
| S10 | [INA293-Q1](https://www.ti.com/product/INA293-Q1) | -4…110 V common-mode; tek yönlü ölçüm, faz/regen doğrudan alternatifi değil |
| S11 | [TLV3201-Q1](https://www.ti.com/product/TLV3201-Q1) | Hızlı comparator adayı; tüm protection loop gecikmesi ayrıca ölçülecek |
| S12 | [LTC3895](https://www.analog.com/en/products/ltc3895.html) / [datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/3895fa.pdf) | 140 V çalışma girişli buck controller; harici güç katı gerekir |
| S13 | [LM5164-Q1](https://www.ti.com/product/LM5164-Q1) / [LM5146-Q1](https://www.ti.com/product/LM5146-Q1) | 100 V sınıfı yardımcı besleme alternatifleri, giriş marjı koşullu |
| S14 | [TPS62130A-Q1](https://www.ti.com/product/TPS62130A-Q1) | 12→5 V yardımcı buck adayı |
| S15 | [TPS3850-Q1](https://www.ti.com/product/TPS3850-Q1) | Harici supervisor/watchdog adayı |
| S16 | [ISO1042-Q1](https://www.ti.com/product/ISO1042-Q1) / [ISO7721-Q1](https://www.ti.com/product/ISO7721-Q1) | İzole CAN ve dijital arayüz seçenekleri |
| S17 | [ISO1410](https://www.ti.com/product/ISO1410) | İzole RS485 opsiyonu; automotive niteliği burada doğrulanmadı |
| S18 | [TI komütasyon yöntemleri](https://www.ti.com/document-viewer/lit/html/SSZTAP5/GUID-CC1F9308-8F55-4454-B07B-6C65016E6430) | Hall six-step ve sinüzoidal/FOC yöntemlerinin bağlamı |

## Resmî mevzuat kaynakları

| Ref | Kaynak | Bu çalışmanın doğruladığı kapsam |
|---|---|---|
| L01 | [(EU) 168/2013 güncel konsolide metin, 02/08/2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02013R0168-20260802) | L-kategorisi araç tip onayı çerçevesi; kategori/alt kategori doğrulanacak |
| L02 | [(EU) 3/2014](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32014R0003) | İşlevsel güvenlik delegasyon çerçevesi; güncel revizyon/kapsam teyidi açık |
| L03 | [UNECE R136 resmî dizin](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-121-140) | L kategorisi elektrik tahrik düzenlemesi; tam güncel amendment serisi okunmadı |
| L04 | [R136 yayımlanmış AB metni](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:42019X1120) | İlgili düzenleme bağlantısı; tam metne erişim bu oturumda engellendi, numeric gereksinim kaynağı sayılmadı |
| L05 | [UNECE R10 resmî dizin](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-0-20) | Elektromanyetik uyumluluk düzenlemesi; uygulanacak seri/kapsam teyidi açık |

ISO/CISPR ailesi örnekleri doğrulama planında mühendislik kapsamı önerisi olarak verilmiştir. Ücretli tam metinler ve Türkiye'deki ulusal uygulama bu çalışma kapsamında madde bazında doğrulanmamıştır.
