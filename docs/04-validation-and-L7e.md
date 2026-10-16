# Donanım doğrulama kontrol listesi

Bu dosya proje gözden geçirmesine yöneliktir; araç tip onayı veya tamamlanmış güvenlik beyanı değildir.

## Şema incelemesi
- [ ] Giriş ters bağlantı, sigorta/ayırma ve DC-link ön şarj gereksinimleri belirlendi.
- [ ] Gate-driver high-side/low-side referansları, UVLO ve giriş durumları kontrol edildi.
- [ ] Tüm açılış/kapanış/reset durumlarında kapılar güvenli duruma geçiyor.
- [ ] MCU'dan bağımsız aşırı akım ve ortak shutdown yolu bulunuyor.
- [ ] Faz akımı örnekleme ve PWM/ADC tetikleme planı tamam.
- [ ] Hall ve haberleşme I/O için ESD/EMI ve besleme sınırları incelendi.

## PCB / mekanik incelemesi
- [ ] Yüksek di/dt güç döngüsü ve gate döngüsü minimize edildi.
- [ ] Kelvin ölçüm bağlantıları ve analog dönüş yolları tanımlandı.
- [ ] Güç ve kontrol alanları ile izolasyon gereksinimleri incelendi.
- [ ] Termal yol, konnektörler, sabitleme ve muhafaza koşulları kontrol edildi.

## Doğrulama planı
- [ ] Enerjisiz ERC, süreklilik ve fault mantığı kontrolleri
- [ ] Kontrollü düşük enerji koşullarında sinyal ve ölçüm doğrulaması
- [ ] Hall dizilimi, akım polaritesi, ADC offset/gain kalibrasyonu
- [ ] Six-Step ve FOC için aynı koruma sisteminin geçerliliği
- [ ] Termal/EMC ve arıza durumlarının yetkin laboratuvarda değerlendirilmesi

Uygulanabilir araç ve EMC mevzuatı, gerçek araç sınıfı ve pazar belirlenince uzman incelemesiyle kesinleştirilir.
