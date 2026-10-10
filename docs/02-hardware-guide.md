# Donanım tasarım kılavuzu

Bu dokümandaki değerler ön boyutlandırma örnekleridir. Gerçek motor ve batarya verisiyle seçim kapıları kapatılmadan üretim değerleri sayılmaz. Üretici bağlantıları [kaynaklar](05-sources.md) dosyasındadır.

## 1. Elektriksel zarf

72 V nominal bataryanın kimyası ve seri sayısı bilinmiyor. Örneğin 20s Li-ion 4,2 V/hücre ile 84 V, 24s LiFePO4 3,65 V/hücre ile 87,6 V olur; bunlar kullanıcının bataryasının tanımı değildir. Geçici mühendislik senaryosu: 50–90 V çalışma incelemesi, ayrıca darbe ve regen analizi. UV/OV eşikleri bu senaryodan otomatik oluşturulmaz.

Her parça için sürekli çalışma, tekrar eden darbe, mutlak maksimum ve sıcaklık sınırları ayrı kontrol edilir. VDS ≈ Vbus + Lstray × di/dt; 50 nH ve 500 A/µs örneğinde 25 V ek darbe çıkar. Bu yüzden 90 V bara için 100 V MOSFET koşulsuz uygun değildir. 150 V sınıfı başlangıç adayıdır; 150 V da otomatik güvenli tasarım değildir. Tolerans ve derating ile bütün devrenin en zayıf sınırı belirlenir.

## 2. Üç faz köprüsü ve MOSFET seçimi

Her faz: DC+ → high-side MOSFET → faz düğümü → low-side MOSFET → low-side shunt → DC−. Gövde diyotlarının yönü, akım serbest dolaşımı ve ters akım bütün anahtarlama durumlarında doğrulanır.

Aday: IPB057N15NM6, 150 V D²PAK MOSFET. Üretici ürünü doğrulanmıştır; AEC-Q101 niteliği burada doğrulanmamıştır. Araç sürümü için uygun otomotiv dereceli 150/200 V alternatif ayrıca seçilmeli. Ön yerleşim için anahtar başına iki paralel, toplam 12 MOSFET alanı ayrılabilir. Bu, 50 A veya 100 A termal kapasite garantisi değildir.

Seçim ölçütleri: RDS(on) sıcaklık katsayısı ve gerçek VGS, Qg/Qgd, Coss/Eoss, Qrr, SOA, kısa darbe, avalanche bağımlılığı, paket/termal bağlantı, gate sürücü kapasitesi. Datasheet'teki ID değeri PCB üzerinden geçirilebilecek akım değildir.

Örnek: RDS(on) = 5,7 mΩ, sıcaklık çarpanı 2, anahtar başına 2 paralel. Six-step'te iki aktif anahtar grubu için yaklaşık iletim kaybı:

`Pcond ≈ 2 × Iphase² × RDS_hot / Nparallel`

50 A faz akımı için 28,5 W; 100 A için 114 W. Akımın şekli, diyot iletimi, PWM ve anahtarlama kayıpları ayrıca eklenir. 50 A batarya akımını bu formüle faz akımı diye koymak doğru değildir.

Her MOSFET'in ayrı gate direnci olsun. Simetrik drain/source güç dağılımı, yakın termal eşleşme ve kısa gate-source dönüşü kur. Bir ortak gate direnciyle paralellerin eşit anahtarlandığını varsayma. Paket Kelvin source içermiyorsa sürücü dönüşünü source pad yakınından ayrı iz ile al.

## 3. Gate driver seçenekleri

### A. Gerilim marjı için önerilen ön mimari

3 × UCC21520-Q1, her birinden iki MOSFET grubu sürülür. High-side için faz düğümüne referanslı 3 bağımsız izole 12 V besleme; low-side için HV kontrol alanındaki ortak 12 V kullanılabilir. Besleme izolasyon kapasitesi, CMTI, ray UVLO ve açılış sırası incelenir. Her high-side ray için yüzer 12 V regülasyonu/UVLO doğrulanır. Driver çıkışı gate'i kendi source'una göre sürer.

MCU bu mimaride BAT− referanslı olduğundan izole driver giriş/çıkışının bir kısmında toprak ortaklanabilir. Driverın izolasyon etiketi aracın HV–LV izolasyonunun kanıtı değildir. Araç LV arayüzleri ayrıca izole edilir. Ayrı izole high-side besleme, bootstrap'ın düşük hız/yüksek duty yenileme kısıtını azaltır; besleme arızasında iki gate de güvenli kapanmalıdır.

### B. Daha düşük BOM alternatif

3 × UCC27301A-Q1. HI/LI bağımsız PWM, input interlock, UVLO. **Enable yalnız DRC pakette var; DDA pakette yok.** DRC bulunabilirliği/ürün durumu satın almadan doğrulanmalı. DDA kullanılırsa fault, HI/LI'yi donanımdan güvenli sıfıra zorlayan mantıkla kesilir. Interlock dead-time hesabının yerine geçmez.

HB pininin BAT−'a göre gerilimi yaklaşık `Vbus + Vgate`; 120 V mutlak maksimum yalnız bara değeri değildir. HS/HB tavsiye edilen çalışma sınırları ve negatif transient süreleri datasheet §5 ile kontrol edilir. 87,6 V + 12 V = 99,6 V; buna overshoot eklenecek. Bootstrap kapasitesi `Cboot ≥ (N × Qg + IHB × ton + Qleak)/ΔVboot` ve DC-bias/soğuk toleransıyla hesaplanır. Six-step'te high-side'ı uzun süre sabit açık tutan PWM düzeni bootstrap'ı boşaltabilir. Yenileme pencereleri veya yüzer besleme gerekir.

### C. Entegre alternatifler

DRV8353 SPI/6PWM ve üç CSA açısından prototip için kolaydır; 100 V sınıfı olduğundan tam paket/regen/darbe marjı kanıtlanmadan seçilmez. Beslemeyi 12 V'a ayırmak high-side switch pinlerinin gerilim sınırını kaldırmaz. DRV8323'ün 65 V sınıfı 72 V bataryaya uygun değildir. STSPIN32G4'ün 75 V sınıfı da tipik 84–87,6 V tam dolu pakete uygun değildir. Bu parçaları FOC yetenekleri yüzünden gerilim sınırlarını görmezden gelerek kullanma.

Gate beslemesi için başlangıç 10–12 V (MOSFET/driver datasheet'e göre), her gate için Rg-on/off alanı, source referanslı pull-down ve VGS clamp alanı. Rg'nin nihai değeri çift darbe/gate dalga şekli ölçümünden çıkar. Dead-time, gerçek açılma/kapanma gecikmeleri ve Miller etkisiyle belirlenir; gereksiz uzun dead-time diyot kaybını artırır.

## 4. Akım ölçümü ve koruma

Üç low-side shunt: başlangıç örneği 0,5 mΩ, Kelvin, düşük TCR, uygun pulse gücü. Üç INA240A2-Q1 (gain 50) adayı, 3,3 V besleme ve yaklaşık 1,65 V REF. ±100 A örneğinde çıkış 1,65 ± 2,5 V olur ve ADC'ye sığmaz. Dolayısıyla bu kombinasyon uygun değildir. **BOM başlangıcı INA240A1-Q1 gain 20 + 0,5 mΩ**: ±100 A için 1,65 ± 1 V, yani 0,65–2,65 V. Gerçek output swing, offset ve ADC toleransı ayrıca kontrol edilir.

INA240'ın 80 V common-mode sınırı low-side kullanımında bara ile doğrudan karşılaştırılmaz: girişleri DC− yakınındadır. Ancak bu parçayı 84–87,6 V faz içine veya DC+ shunt'a taşımak uygun değildir. Inline/high-side ölçüm için daha yüksek common-mode ve transient kapasitesi olan çift yönlü veya izole ölçüm seçilir. INA293 tek yönlü olduğundan çift yönlü faz/regen ölçümünün doğrudan alternatifi değildir.

0,5 mΩ shunt'ta 100 A sürekli örneği 5 W eder. Gerçek low-side RMS ve duty bilinmeden üç shunt'ın toplam kaybı hesaplanmaz. Kelvin izler güç bakırından ayrılır, giriş RC eşleşmesi ve CSA settling ölçülür. ADC örnekleme switching kenarlarından/blanking'den sonra, low-side iletimin geçerli penceresinde tetiklenir. Duty uçlarında faz rekonstrüksiyonu/örnekleme stratejisi gerekir.

Faz koruması: yükselteç çıkışları için +I/−I pencere karşılaştırıcıları veya bağımsız hızlı algılama; örnek başlangıç 6 TLV3201-Q1 alanı (3 faz × 2 yön). Eşik → fault latch → bütün gate driver disable ve MCU timer break. Aşırı filtreleme kısa devreyi gizlememeli. Sense amplifier gecikmesi ve doyumdan çıkışı dahil toplam kapatma süresi SOA ile doğrulanır; TLV3201 seçimi tek başına kısa devre korumasını kanıtlamaz.

Motor akımına görünmeyen bazı shoot-through yollarını yakalamak için bağımsız DC-link akım koruması da değerlendirilir. Batarya kablosu akım sensörü ile yerel kapasitörün verdiği hızlı kısa devre akımı aynı değildir. Batarya sigortası MOSFET'i her kısa devrede koruyamaz; fault kapsaması durum bazında incelenir.

## 5. DC-link, ön şarj ve aşırı gerilim

Bulk: alüminyum elektrolitik bank + yerel film kapasitörleri + küçük yüksek gerilim seramikleri. Kapasitörler faz yoluna seri bağlanmaz; DC+–DC− arasına, köprüye yakın yerleşir. Nominal 72 V için 100 V kapasitör otomatik seçilmez; 160 V elektrolitik aday sınıfı ve uygun film sınıfı marj sağlar ancak boyut/ripple/ömürle doğrulanır.

Kapasite örneği `C ≥ ΔI × Δt / ΔV`. 100 A, 100 µs, 10 V izin verilen düşüm için 1000 µF. Bu hesap PWM RMS ripple'ını vermez. Ripple ayrıca üç faz anahtarlama ve kaynak empedansından hesaplanır/simüle edilir. Paralel bankta `Pcap ≈ Irms² × ESRbank`; sıcaklık/akım paylaşımı ve ömür datasheet'ten incelenir. “7 × 100 µF yeterlidir” denemez. Bulk kapasitörde yüksek ESR hedeflenmez; gerekiyorsa filtre sönümü ayrı elemanla yönetilir.

Araç seviyesinde sigorta, servis ayırıcı, DC-rated kontaktör(ler), precharge kolu, Vpack/Vdc ölçümü ve kontaktör feedback bulunmalı. Başlangıç sırası: kontrol enerjisi → güvenlik izinleri → precharge → gerilim farkı/timeout doğrulama → ana kontaktör → precharge kolunu ayır → gate enable. Kontaktör kaynak yapması, precharge direnci açık devre ve Vdc sensörü arızası teşhis edilir.

1000 µF ve 87,6 V için enerji 3,837 J. 100 Ω precharge örneği başlangıç akımı 0,876 A ve başlangıç güç 76,74 W; %95 şarj ~0,300 s. Direnç sürekli watt etiketiyle değil pulse enerji/tekrar aralığıyla seçilir.

Deşarj direnci veya aktif yolun süresi `t = RC × ln(Vinitial/Vtarget)`. 1000 µF, 10 kΩ, 87,6 → 60 V örneği ~3,785 s; başlangıç güç 0,767 W. 60 V örnek eşiği herhangi bir mevzuatın bütün koşullarda süre şartını sağladığı iddiası değildir. Nihai servis hedefi, tolerans ve arıza durumuyla belirlenir.

Regen devre dışı olsa bile dönen motorun geri EMK'si DC-link'i yükseltebilir. BMS şarj reddi/kontaktör açılması durumunda enerji yolu tanımlanır. TVS ana fren enerjisi yutucusu değildir. Gerekirse fren kıyıcı + direnç alanı ayrılır: motor/araç enerjisi, tork ve tekrar süresiyle seçilir. Normal akımda kontaktör açma sırası ile acil kısa devre ayırma farklı senaryolardır.

## 6. Yardımcı besleme ve izolasyon alanları

Önerilen ön mimari: BAT− referanslı kapalı HV kontrol alanı. LTC3895 (140 V çalışma sınıfı) tabanlı harici MOSFET'li buck ile HV → 12 V; harici parçalar aynı zarfı sağlamalı. Bu parça prototip adayıdır; otomotiv niteliği doğrulanmamıştır. Gate rayları, high-side yüzer besleme yükleri, MCU/arayüz gücü için tam bütçe çıkarılır.

12 → 5 V için TPS62130A-Q1 adayı; 5 → 3,3 V için uygun LDO/buck ve ADC rayı filtreleme. 12 V'tan 3,3 V LDO'ya 200 mA örneğinde 1,74 W kayıp oluşur; doğrudan zincir tercih edilmez. LM5164-Q1/LM5146-Q1 gibi 100 V yardımcı beslemeler yalnız darbe zarfı kontrol altında ise alternatif. Kontrol beslemesinin kontaktör öncesi alınması gerekiyorsa ayrı sigorta/koruma ve kapalı durum tüketimi hesaplanır.

Araç LV/şasi alanına CAN (ISO1042-Q1 + iki taraf için doğru besleme), gerekiyorsa izole RS485, safety enable, pedal ve kullanıcı I/O üzerinden izolasyon sağlanır. ISO1042'nin CAN bus ±70 V fault sınıfı traction bataryasını CAN hatlarına bağlama izni değildir. İki tarafta güç izolasyonu da sağlanır; ortak GND veya USB shield izolasyonu bypass etmemeli.

Pedalı doğrudan HV adasına bağlamak yerine araç LV alanında iki kanal okuyup güvenlik kontrollü VCU/CAN komutu ve bağımsız izin yolu kullanmak bir seçenektir. VCU yoksa yerel LV pedal kartı ve izole veri/güç mimarisi tasarlanır. E-stop/enable kaybı MCU çalışmasa da gate-off oluşturmalı. Sayısal izolasyon elemanında power-off varsayılanının güvenli polarity ile uyumu kontrol edilir.

BAT− araç şasisiyle gelişigüzel ortaklanmaz. Soğutucu metal gövdeye bağlanabilir ancak MOSFET drain tabı ve HV bakırı termal pad/yalıtım ile ayrılır. Vida, rondela, nem ve kirli yüzey dahil elektriksel açıklıklar kontrol edilir. Şasi kapasitörleri IMD ve toplam kaçak kapasitesini etkiler; tek başına EMI kazanımıyla seçilmez.

## 7. MCU, Hall ve arayüzler

STM32G474RE adayı: motor PWM timerları, ADC, comparator, CORDIC/FMAC ve FDCAN. MCU otomotiv sertifikası bu çalışmada doğrulanmış değildir. Pin planında 6 gate PWM, BKIN, üç akım ADC, Vdc/Vpack, sıcaklıklar, 3 Hall, encoder A/B/Z alanı, CAN TX/RX, driver control/fault, watchdog ve SWD ayrılır. Paket bazında pin mux ve ADC tetikleme çakışmaları kontrol edilir; bütün aile özellikleri her pin/pakette eşzamanlı kullanılamaz.

Hall: ESD kablo girişinde, sensör beslemesi akım sınırlı/filtreli, doğru pull-up ve 3,3 V seviyesine uyarlama, RC + Schmitt alanı. 5 V Hall çıkışı MCU'nun bütün pinlerine doğrudan verilemez. NTC ve Hall sensörü dönüş hatları faz akımından ayrılır. 120° Hall düzeninde 000/111 genelde geçersizdir; 60° düzende tablo farklıdır. Motor test edilmeden bir hazır Hall tablo eşlemesi yazılmaz.

Filtre örneği 1 kΩ/1 nF → τ=1 µs; giriş sürücüsü ve threshold ile gerçek gecikme ölçülür. Elektriksel açı hatası `Δθe = 360 × fe × tdelay`. Kutup sayısı olmadan büyük RC seçilmez. Hall ofset/sıra/yön düşük enerjide haritalanır. FOC'de Hall sektörleri arasındaki açı interpolasyonu özellikle sıfır hızda kesin açı bilgisi değildir; encoder veya gözlemci gerektiği ölçümle belirlenir.

CAN araç haberleşmesi için aday; RS485 ancak gerçek sistem gereksinimi varsa. Terminasyon yalnız iki fiziksel uçta, TVS/CMC ve kablo referansı belirlenir. Throttle plausibility, fren önceliği, gear değişimi hız kilidi, heartbeat timeout, açılışta sıfır tork, watchdog/reset gate-off zorunlu fonksiyonlar olarak ayrılır.

## 8. EMI, snubber, layout ve mekanik

- DC-link film kondansatörünü köprü komütasyon halkasına yakın koy. Bara gidiş/dönüşünü üst üste veya yakın tut; busbar/kablo bağlantısı için akım/ısınma hesabı yap.
- Gate driver MOSFET'lere yakın; gate ve source dönüşü birlikte kısa. Faz switch-node bakırını gereksiz büyütme, analog/sensör izlerinin altında geçirme.
- Akım ADC/REF için temiz dönüş düzeni; güç dönüşünü shunt Kelvin izlerine taşıma. Genel “star ground” önerisi her frekansta çözüm değildir; gerçek akım yolları çizilir.
- Giriş filtresi kaynak kablosu, DC-link ve inverter negatif artımsal empedansı ile birlikte incelenir. DM L/C ve CM bobini akım/satürasyon/sönümle seçilir; 50 A güç filtresi küçük sinyal CMC'si değildir.
- RC snubber için üç faz/anahtar alanı ayrılır, başlangıç DNP bırakılabilir. Parazitik çınlama frekansı ve enerji ölçülmeden R/C dondurulmaz. `Psnubber ~ C × V² × f` seviyesinde kayıp kontrol edilir.
- Hall kablosunu faz kablolarından ayır; dönüşüyle bük, ekranı muhafaza girişinde tanımlı sonlandır. Kablo ekranını tek uç mu çift uç mu kararı frekans ve şasi mimarisiyle verilir.
- PCB açıklık/creepage değeri nominal 72 V'a bakılarak tek sayı verilmez: çalışma/darbe gerilimi, kirlilik, CTI, irtifa ve izolasyon sınıfıyla belirlenir.
- FET sıcaklığı NTC'den doğrudan okunmaz. `Tj = Tsink + P × Rθ(path)` ve transient termal empedans modeli kurulur. Motor sargı sıcaklığı gövde sıcaklığından farklıdır.
- IP hedefi, su tahliye/yoğuşma, kablo rakoru, konektör gerilim/akım sınıfı, vibration, termal pad izolasyonu ve vida torku belirlenir. Conformal coating açıklık hesabının otomatik alternatifi değildir.

## 9. Prototip geçişleri

P0: güçsüz I/O/fault testi → düşük voltajlı akım sınırlı kaynak → Hall haritalama ve akım ölçümü → akım kontrollü six-step → termal/darbe doğrulaması → kontrollü araç testi.

P1: aynı kartta sensörlü FOC + SVPWM. Faz R/L ve K_e, ADC offset/gain, Hall/encoder elektriksel açı kalibrasyonu ve CPU kontrol çevrimi ölçülür. Standart FOC motor modelinin trapezoidal geri EMK harmoniklerini kapsamadığı göz önüne alınır.

P2: regen ve gerekirse alan zayıflatma. BMS kabul gücü/SOC/sıcaklık, magnet demanyetizasyon limiti ve OV kontrolü doğrulanmadan aktif edilmez. İlk kartta encoder, Vdc ölçümü ve fren kıyıcı arayüzü alanı bırakmak sonradan revizyonu azaltır; her yükseltme otomatik olarak yalnız yazılım değişikliği değildir.
