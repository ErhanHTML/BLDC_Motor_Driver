# BLDC Motor Driver

Üç fazlı BLDC/PMSM motorlar için **Hall sensörlü Six-Step ve FOC/SVPWM uygulamalarını aynı donanım üzerinde desteklemeyi hedefleyen** motor sürücü donanım ön tasarımı.

Bu depo tamamlanmış veya doğrulanmış ürün sunmaz; sistem mimarisini, tasarım önerilerini, kritik arayüzleri ve doğrulama sırasında dikkat edilecek konuları açıklar. Nihai bileşen, gerilim/akım/termal sınır ve PCB kararları ölçüm ve incelemelerden sonra kesinleştirilmelidir.

## Sistem kapsamı

- Üç faz için üç bağımsız yarım köprü; her fazda high-side ve low-side güç anahtarı.
- Her yarım köprü için **bir bağımsız çift çıkışlı gate-driver**; toplam üç sürücü.
- Kontrol biriminde tamamlayıcı PWM, donanımsal dead-time ve fault girişleri.
- Senkron faz akımı geri beslemesi, DC-link ölçümü, sıcaklık ve donanımsal aşırı akım koruması.
- Üç dijital Hall girişi; gelecekte daha hassas rotor konumu için ek sensör arayüzüne yer ayrılması.
- Yardımcı beslemeler, haberleşme, kontrol girişleri ve korumalı durum geçişleri.

## Belgeler

| Belge | Amaç |
|---|---|
| [Sistem mimarisi](docs/01-review.md) | Donanım blokları ve açıklamalar |
| [Donanım tasarım rehberi](docs/02-hardware-guide.md) | Her alt sistemde dikkat edilecek konular |
| [Blok diyagramları](docs/03-diagrams.md) | Güç, sinyal ve fault akışları |
| [Doğrulama kontrol listesi](docs/04-validation-and-L7e.md) | Şema, yerleşim ve test öncesi gözden geçirme |
| [Kaynak değerlendirme yöntemi](docs/05-sources.md) | Datasheet ve uygulama notu inceleme ölçütleri |
| [Algoritma uyumluluğu](docs/06-control-methods.md) | Ortak donanımın Six-Step ve FOC gereksinimleri |
| [Algılama ve geçiş](docs/08-sensing-and-transition.md) | Hall, akım ve konum arayüzleri |
| [Ön BOM](hardware/BOM.md) | Aday kategorileri ve seçim gerekçeleri |

**Durum:** Mimari öneri; şema, PCB routing, motor karakterizasyonu, koruma koordinasyonu ve termal doğrulama tamamlanmış değildir.
