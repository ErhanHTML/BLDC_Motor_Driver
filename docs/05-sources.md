# Teknik kaynakların değerlendirilmesi

Bu depo belirli bir parça seçimini onaylamaz. Her aday için **güncel üretici datasheet'i**, uygulama notları, errata, paket çizimi ve tedarik durumu kontrol edilmelidir.

## İncelenecek kaynak türleri

- MCU: tamamlayıcı PWM, break/fault, ADC senkronizasyonu, Hall/encoder zamanlayıcı işlevleri ve işlem yükü.
- Gate driver: besleme ve switch-node sınırları, high-side yöntemi, UVLO, CMTI, çıkış akımları ve varsayılan giriş durumları.
- MOSFET: sıcaklıkla iletim direnci, anahtarlama yükleri/kayıplar, SOA, transient dayanımı ve paket termal karakterizasyonu.
- Akım ölçümü: PWM common-mode dayanımı, yerleşme süresi, doğruluk ve ADC arayüzü.
- DC-link: gerilim sınıfı, RMS ripple akımı, ESR/ESL, ömür ve mekanik paket.
- EMC/güvenlik: nihai uygulamanın ilgili test metotları ve yetkili incelemesi.

Sayısal özellik ve parça uygunluğu, ölçüm/simülasyon ve datasheet gereksinim matrisiyle doğrulanmadan BOM'da kesinleştirilmez.
