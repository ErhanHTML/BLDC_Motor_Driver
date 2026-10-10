# Hall, encoder, akım ölçümü ve prototip geçişi

10 Ekim 2026. [Kontrol anlatımındaki](06-control-methods.md) işaret/ölçek konvansiyonları kullanılır. Bu dosya donanım gereksinimlerini ve doğrulama kapılarını tanımlar; bitmiş firmware veya doğrulanmış araç güvenlik tasarımı değildir.

## 1. Üç dijital Hall ile FOC

Üç Hall tipik olarak bir elektriksel turda altı sektör bildirir. Sektör içinde tek başına kesin açı vermez. Geçiş açıları kalibre edilirse Hall kenarı konum referansı olur; ardışık kenar sürelerinden hız tahmin edilir:

`ωe_hat = Δθsector / Δt`; `θe_hat(t) = wrap(θedge + ωe_hat × (t−tedge))`.

Nominal Δθsector=π/3 olsa da gerçek sensör yerleşimi sektörleri eşit yapmayabilir. Her kenar açısının ve iki dönüş yönündeki offset'in ölçülmesi gerekir. Örnek: 60° geçiş 2 ms sürerse elektriksel hız 523,599 rad/s, elektriksel frekans 83,333 Hz olur. p=4 varsayımıyla mekanik hız 1250 rpm; bu motorun p değeri değildir.

Yeni kenarda süre/hız güncellenir. Açı hatası kontrollü düzeltilir; büyük ani sıçrama Park dönüşümünde yapay d/q değişimi oluşturur. PLL veya gözlemci kullanılabilir; PLL adını taşımak ivmenin doğrudan ölçüldüğü veya hatanın sıfır olduğu anlamına gelmez. ST UM1052 §8.3.2, Hall açısının kontrol çevrimleri arasında güncellenmesini anlatır; kullanılan güncel SDK ve sensör modülünün davranışı ayrıca incelenir [C03/C04].

Motor dururken mevcut Hall kodu yine **sektör bilgisi** verir. Kenar geçmişi olmadan tam konum/hız tahmini yoktur. Kalibre edilmiş sektör merkezi, sınırlandırılmış kalkış akımı ve uygun başlangıç stratejisi mümkündür; her Hall-FOC'nin mecburen belirli süre six-step çalışması veya mutlaka hırıltı yapması gerekmez. İlk kalkış torku, yanlış yön hareketi ve düşük hızdaki açı belirsizliği ölçülür. ±30° belirsizlik ideal eşit sektörün orta noktası içindir; yerleşim hatası eklenebilir.

Hall teşhisleri: kalibre edilmiş geçerli kodlar, komşu sektör sırası, zaman aşımı, fiziksel hız/ivme sınırı, dönüş yönü ve sensör besleme durumu. 000/111 yalnız yaygın 120° düzen için genellikle geçersizdir; 60° düzenin tablosuna aynı kural körlemesine uygulanmaz. Geri dönüş/durma halinde eski hızla açıyı sınırsız yürütmek hatalıdır.

## 2. Açı hatası torku nasıl etkiler?

Tahmini açı θhat=θtrue+δ olsun. Tahmini eksende Id_hat=0, Iq_hat=I komutu uygulanırsa ideal gerçek eksen bileşenleri:

`Id_true = −I sinδ`; `Iq_true = I cosδ`.

Bu sonuç yalnız tanımlanan işaret konvansiyonu ve ideal akım takibi için geçerlidir. Yüzey mıknatıslı temel modelde tork oranı cosδ:

| Elektriksel açı hatası | I=10 A için Id_true | Iq_true | İdeal tork oranı |
|---|---:|---:|---:|
| 2° | −0,349 A | 9,994 A | %99,939 |
| 10° | −1,736 A | 9,848 A | %98,481 |
| 30° | −5 A | 8,660 A | %86,603 |

Bu tablo sistem verimi tablosu değildir. Sabit toplam akımda ideal bakır kaybı, akım vektörü döndü diye otomatik artmaz; aynı torku korumak için daha çok akım gerekirse kayıp artar. Zamanla değişen δ tork dalgalanması, istenmeyen Id, gürültü ve limit sorunları yaratabilir. Gemini'deki “%99 enerji torka, %1 ısıya” oranı bu denklemden çıkarılamaz.

Mekanik encoder hatası ve gecikmesi elektriksel açıya büyütülür: `δe≈p δm + ωe tdelay`. Çok kutuplu motorda çözünürlük kadar gerçek doğruluk, offset ve zaman damgası önemlidir.

## 3. Analog Hall ne sağlar?

Uygun yerleştirilmiş analog Hall kanalları alanın bileşenlerini ölçebilir. Offset ve gain kalibrasyonundan sonra birbirine dik sin/cos bileşenler varsa `θ=atan2(y,x)` kullanılabilir. 120° yerleşmiş üç analog kanal doğrudan sin/cos çifti sayılmaz; önce uygun dönüşüm ve kalibrasyon gerekir.

Sıfır hızda sürekli açı bilgisi avantaj olabilir; fakat tek lineer Hall gerilimi bir tam turu her zaman benzersiz tanımlamaz. Harmonik alan şekli, mıknatıs konumu, sıcaklık, doyum, dış alan, ADC gürültüsü ve kablo etkileri ölçülür. Analog Hall “kusursuz mutlak encoder” veya garantili maksimum kalkış torku değildir.

## 4. Encoder bağlantısı ve kalibrasyonu

Manyetik encoder örneğinde şaft üzerindeki uygun diametrik mıknatıs döner, karşısındaki sabit sensör PCB'si alan yönünü ölçer. Mekanik merkezleme, eğiklik, air gap, alan aralığı ve mıknatısın güvenilir sabitlenmesi datasheet'e göre tasarlanır. Her motor için 1–2 mm boşluk veya yalnız yapıştırıcı yeterli kabul edilmez.

| Arayüz | Kablolar / işlem | Başlangıç bilgisi | Kontrol notu |
|---|---|---|---|
| Mutlak SPI | SCK, MOSI, MISO, CS + besleme/dönüş | Mekanik açı doğrudan okunabilir | Elektriksel sıfır ve p yine kalibre edilir; gecikme/protokol doğrulanır |
| Artımsal A/B/Z | A/B quadrature timer, Z index + besleme/dönüş | Reset sonrası başlangıç referansı gerekir | Z tek yöntem değildir; uygun alignment veya başka mutlak referans kullanılabilir |
| Resolver | Excitation ve sin/cos + RDC/ADC | Uygun dönüşümle mutlak açı | Analog frontend, uyarma ve izolasyon ayrı tasarımdır |

AS5047P, Gemini'de geçen bir araştırma adayıdır [C05]. 14 bit, 360/16384≈0,02197° **mekanik sayım adımıdır**; gerçek doğruluk değildir. Parça/sistem otomotiv veya L7e uygunluğu burada onaylanmamıştır. MT6835 için üretici datasheet/qualification incelenmediğinden BOM'a doğrulanmış alternatif olarak eklenmedi.

SPI uygulaması parçanın CPOL/CPHA, clock sınırı, CS süreleri, pipelined response ve seçilen açı register'ına uyar. AS5047P'de parity/error flag değerlendirilir; yalnız `0xFFFF` kontrolü bütün arızaları yakalamaz. Yeni veri, stale data, zaman aşımı, manyetik teşhisler ve fiziksel açı/hız tutarlılığı birlikte ele alınır. 20 kHz çevrimde beş ardışık hatalı örnek beş örnek periyodu olarak **250 µs** bütçedir; tam arıza tespit süresi frame zamanlaması ve eşik tanımına bağlıdır, otomatik 1 ms değildir.

## 5. Kart üzerinde Hall ve encoder birlikte

- Hall konektörü: sensör supply, referans dönüş, H1/H2/H3; kablo girişinde ESD/koruma, gerektiğinde seviye uyarlama, RC/Schmitt alanı ve timer input capture.
- Encoder konektörü: doğrulanmış SPI beslemesi/seviyeleri, SCK/MOSI/MISO/CS; opsiyonel A/B/Z. Kablo uzunluğu SPI'ın güvenilirliğine uygunsa kullanılır; uzun kabloda uygun diferansiyel arayüz değerlendirilir.
- MCU pin planı: motor timerının altı PWM çıkışı ve BKIN, Hall timerı, encoder timer/SPI/DMA ve senkron ADC aynı pakette çakışmadan atanır. TIM2/SPI1 isimleri doğrulanmış pin planı değildir.
- Hall open-collector/open-drain ise uygun pull-up seçilir; push-pull ise çıkış seviyesine uyum kontrol edilir. Her pin 5 V tolerant değildir. Sensör supply/ground arızası iki açı kaynağını birlikte bozabilir.
- Referans dönüş yolları güç akımı taşımaz. Encoder/Hall alanının HV kontrol alanı mı araç LV alanı mı olduğu [izolasyon planına](02-hardware-guide.md) göre belirlenir; iki konektör eklemek izolasyonu kendiliğinden sağlamaz.

Hall RC örneği 1 kΩ×10 nF için τ=10 µs'dir; gerçek kenar gecikmesi pull-up, çıkış tipi ve Schmitt eşiğine de bağlıdır. Gecikmenin açı karşılığı `δθe=ωe×tdelay`. Örneğin 1 kHz elektriksel frekansta 10 µs, 3,6° eder. Dolayısıyla bu değer evrensel öneri değildir. RC, timer dijital filtresi ve yazılım debounce toplam gecikmesiyle tasarlanır.

SPI'da büyük RC alçak geçiren filtre kenarları bozabilir. Buna rağmen “asla kondansatör/filtre olmaz” mutlak kural değildir: seri sonlandırma, ESD kapasitansı ve kontrollü küçük filtre ancak timing/sinyal bütünlüğü analiziyle seçilir. Dönüş düzlemi kesilmez, switching düğümlerinden uzak tutulur.

## 6. Akım örnekleme: FOC'ye geçişin kritik donanım şartı

Low-side shunt her anda faz akımını göstermez. Ölçüm, ilgili alt anahtar iletim yolunda akım varken ve CSA/ADC yerleşmişken geçerlidir. 000 ideal olarak üç alt anahtarı açtığından uygun pencere olabilir; **111 aynı low-side ölçüm penceresi değildir**. “Her sıfır vektöründe PWM ortasında örnekle” kuralı yeterli değildir.

Dead-time, ringing blanking, amplifikatör settling, ADC acquisition ve minimum darbe süresi birlikte hesaplanır. Duty uçlarında pencere kaybolursa başka iki faz seçimi, PWM düzenleme veya akım rekonstrüksiyonu gerekir. KCL ancak aynı zamana ait geçerli kablo akımlarıyla uygulanır. Delta motorda kablo akımı ile sargı kolu akımı ayrılır.

Standart FOC'de iki bağımsız faz akımı yeterli olabilir; bu, mutlaka iki fiziksel shunt gerektiği anlamına gelmez. Single DC-link shunt ile uygun aktif vektör pencerelerinde rekonstrüksiyon da mümkündür, fakat daha zor zamanlama/ölçüm koşulları vardır. Bu proje üç low-side shunt mimarisini korur. Akım feedback'i kaybolursa six-step'e geçip koruma varmış gibi sürmek kabul edilmez.

## 7. Aynı kartta yöntem değiştirmek

Güç köprüsü topolojisi ortak olabilir; “yalnız firmware değişir” ifadesi bütün kart için koşulsuz değildir. Başlangıçta altı bağımsız gate komutu, komplementer PWM/dead-time, senkron faz akımı ADC'si, geçerli açı ve fault yolları sağlanmalıdır. Yalnız six-step için yapılmış dar sensör/driver arayüzü FOC'de revizyon isteyebilir.

| Prototip | İzin verilen işlev | Geçiş öncesi kanıt |
|---|---|---|
| P0 | Hall + PWM akım kontrollü six-step | Faz/Hall tablosu, akım polaritesi, OCP, dead-time, termal ve bus testleri |
| P1 | Hall-FOC + SVPWM; Id_ref=0 | p, açı offset'i, Hall kenar haritası, Rs/L/ψ tahmini, ADC penceresi, PI kararlılığı |
| P2 | Encoder-FOC ve opsiyonel Hall yedeği | Encoder elektriksel sıfırı, latency, Hall/encoder farkı, arıza enjeksiyonu |
| Daha sonra | Sınırlandırılmış field weakening / regen | Demag sınırı, hız/termal zarf, BMS enerji kabulü ve DC-link OV yönetimi |

İlk prototipte mod seçimi yalnız PWM kapalı ve kontrollü durumda yapılır. Çalışırken `switch(mode)` ile tabloyu değiştirmek güvenli geçiş sayılmaz; faz akımları aniden kaybolmaz. Timer shadow update, komütasyon sırası, integratör reset/tracking ve yeni modun ölçüm pencereleri ayrıca yönetilir.

## 8. Arızada geçiş ayrı bir kontrol fonksiyonudur

Encoder kaybında motorun mutlaka kilitleneceği veya Hall'a geçince pilotun hiçbir şey hissetmeyeceği söylenemez. Önerilen **henüz doğrulanmamış** P2 akışı:

1. Encoder/Hall sağlıklarını ve kalibre edilmiş açı farklarını sürüş boyunca izle.
2. Arızada mevcut akım geri beslemesi, Hall tahmininin güncelliği ve ortak besleme arızası olasılığını değerlendir.
3. Yedek geçiş ancak sağlıklı Hall, kabul edilebilir açı farkı, test edilmiş hız/akım zarfı ve tanımlanmış tork rampasıyla denenir; integratörlerin yeni açıyla tutarlılığı sağlanır.
4. Koşullar sağlanmıyorsa tasarlanmış fault/gate-off durumuna geç. Gate-off ile elektriksel fren, serbest dönüş ve DC-link enerji davranışını birbirine karıştırma.
5. Kablo kopması, stuck Hall, parity/stale SPI, akım ADC arızası, supply çökmesi ve yön değiştirme senaryolarında akım/tork/bus dalgalarını kaydet.

İki sensör bulunması kendiliğinden bağımsız yedeklilik veya işlevsel güvenlik kanıtı değildir. Ortak MCU, supply, kablo ve güç katı arızaları ortaktır. L7e uygunluğu için mevcut [araç doğrulama planı](04-validation-and-L7e.md) ayrıca uygulanır; bu kontrol dokümanı yeni mevzuat uygunluğu iddiası eklemez.
