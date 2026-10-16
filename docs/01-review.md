# Sistem kapsamı ve mimari

Proje, farklı motor parametrelerine yazılımla uyarlanabilen üç fazlı bir sürücü donanımı oluşturmayı hedefler. Algoritma seçimi güç katını değiştirmemeli; bu nedenle PWM, ölçüm ve konum arayüzleri iki kontrol yaklaşımına göre baştan planlanmalıdır.

## Donanım blokları

1. **DC giriş ve DC-link:** giriş bağlantısı, sigorta/ayırma, ön şarj gereksinimi, uygun EMI düzeni, bulk ve yerel düşük endüktanslı kapasitörler, bara gerilimi geri beslemesi ve güvenli deşarj.
2. **Üç faz inverter:** U/V/W için birer high-side ve low-side anahtar; her faz için tek, bağımsız çift kanallı gate-driver. Sürücü toprağı ve yüzen high-side referansları şemada açık tanımlanmalı.
3. **Kontrol:** motor kontrol zamanlayıcıları, birbirini tamamlayan PWM çıkışları, ADC tetikleme, harici fault girişi, watchdog ve arıza kilitleme.
4. **Ölçüm:** üç faz akım ölçümünün öncelikli değerlendirilmesi; DC-link akımı, bus gerilimi ve güç elemanı sıcaklıklarının izlenmesi.
5. **Konum:** dijital Hall hatları, uygun seviye dönüşümü, giriş koruması ve gerektiğinde encoder için ayrı arayüz.
6. **Yardımcı besleme ve haberleşme:** kontrol/gate güç bütçeleri, besleme sıralaması, izolasyon ihtiyacı, RS485 veya seçilecek araç haberleşme arayüzleri.

## Açık tasarım kararları

- Motorun faz direnci/endüktansı, geri EMK ve kutup çifti sayısı ölçümle karakterize edilmeli.
- DC girişin çalışma ve arıza zarfı, rejeneratif enerji yolu ve geçici darbeleri ayrı tanımlanmalı.
- MOSFET, sürücü ve kapasitör seçimi tek bir nominal değere bakılarak yapılmamalı.
- Nihai PCB ölçüsü; konnektör, soğutucu, kondansatör ve kaçak açıklıkları netleşince belirlenmeli.
- Bu doküman satın alma ya da güvenlik onayı yerine geçmez.
