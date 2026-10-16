# Six-Step ve FOC uyumlu ortak donanım

Proje iki farklı kontrol yazılımını aynı güç elektroniği altyapısında desteklemeyi hedefler. Bu belge kontrol yöntemlerinin performans karşılaştırması değil, gerekli **ortak donanım arayüzlerinin** açıklamasıdır.

## Ortak gereksinimler
- Üç bağımsız half-bridge ve faz başına bir çift kanallı gate-driver.
- Altı gate komutunu yönetebilen tamamlayıcı PWM, dead-time ve ortak donanım kapatma.
- Ölçülen faz akımları için zamanlayıcıyla senkron ADC, güvenilir bara gerilimi ölçümü.
- Hall kod/kenar girişleri, sensör beslemesi ve kalibrasyon arayüzü.
- Parametrelerin ve fault kayıtlarının firmware tarafından yönetilmesi; donanım korumasının firmware'den bağımsız kalması.

## Six-Step kullanımında
Hall sektör bilgisi ve akım geri beslemesine dayanan kontrollü komütasyon desteklenir. PWM/fault mantığı yanlış sektör veya ölçüm kaybında güvenli davranmalıdır.

## FOC/SVPWM kullanımında
Rotor elektriksel açı bilgisi veya geçerli kestirimi, faz akımı örneklemesi ve uygun zamanlayıcı-ADC eşleşmesi gerekir. Hall sektörlerinin arası kendiliğinden hassas açı ölçümü değildir; gereken performans için konum tahmini veya encoder seçeneği doğrulanmalıdır.

Algoritma geçişi yalnız yazılım değişimi olarak garanti edilmez: tüm PWM, gate driver, akım sensing, rotor konumu ve güvenlik arayüzleri ortak donanımda önceden uygun tasarlanmalıdır.
