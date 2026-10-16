# Algılama ve kontrol arayüzü planı

## Hall arayüzü
Üç Hall sinyali rotor sektör bilgisini kontrolcüye taşır. Konnektör, uygun sensör beslemesi, giriş gerilim sınırları, ESD ve hata teşhisi düşünülmelidir. Filtre, kablo paraziti ve gecikme hedefi ölçülerek belirlenir. Hall sırası ve yön haritası varsayılmaz; kalibre edilir.

## Faz akımı
Ölçüm topolojisi; kontrol algoritmalarının geçerli örnekleme pencerelerine göre seçilmelidir. Shunt konumu, yükselteç common-mode dayanımı, Kelvin bağlantısı ve ADC tetikleme birlikte gözden geçirilir. Akım bilgisi kaybı, koruma mevcutmuş gibi başka moda geçilerek maskelenmemelidir.

## Konum genişletme
Konutlandırma ve MCU pin bütçesinde encoder arayüzüne yer bırakılması önerilir. Hall ile FOC hedefleniyorsa açı interpolasyonu/gözlemcisi ayrıca karakterize edilmelidir.

## Entegrasyon
Ölçüm zincirleri, besleme sırası, watchdog ve bağımsız fault kapatma önce doğrulanır. Kontrol modu değiştiğinde kalibrasyon ve limitler yeniden geçerlilik kontrolünden geçirilir.
