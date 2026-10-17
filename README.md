# BLDC Motor Driver

Üç fazlı BLDC/PMSM sürücü için Hall sensörlü Six-Step ve FOC/SVPWM'ye uygun **entegre kart donanım ön tasarımı**. Bu depo üretime hazır elektrik şeması/PCB sunmaz; gereksinim ve tasarım önerilerini kayıt altına alır.

## Güncel kart kapsamı

- Üç half-bridge, altı MOSFET konumu, faz başına **bir bağımsız çift çıkışlı gate-driver**.
- Harici AUX supply yok: DC girişten **kart içinde buck ile 12 V**, ardından ihtiyaç duyulan 5 V/3,3 V rayları.
- **CAN, RS485 ve harici akım ölçüm konnektörleri bulunmayacak.** FOC için kart içi faz akımı geri beslemesi korunacak.
- Hall sensör arayüzü, STM32 motor kontrol PWM/ADC, bus ve sıcaklık ölçümü, bağımsız fault kapatma.
- DRV ailesi kullanılmıyor. Bütün aday MPN ve değerler doğrulamaya tabidir.

## Belgeler

| Belge | İçerik |
|---|---|
| [Entegre kart yerleşim revizyonu](docs/09-integrated-board-revision.md) | Referans görsele göre yerleşim, kart içi buck, çıkarılan arayüzler ve açık kararlar |
| [Sistem kapsamı](docs/01-review.md) | Mimari açıklama |
| [Donanım kılavuzu](docs/02-hardware-guide.md) | Güç katı, ölçüm, Hall, gate drive ve güvenlik |
| [Blok diyagramları](docs/03-diagrams.md) | Güncel bloklar ve fault akışı |
| [Doğrulama listesi](docs/04-validation-and-L7e.md) | İnceleme kapıları |
| [Kaynak değerlendirmesi](docs/05-sources.md) | Datasheet doğrulama |
| [Algoritma uyumluluğu](docs/06-control-methods.md) | Six-Step / FOC ortak arayüz |
| [Algılama](docs/08-sensing-and-transition.md) | Hall ve dahili faz akım algılama |
| [Ön BOM](hardware/BOM.md) | Güncel komponent grupları ve çıkarılan harici konektörler |

**Durum:** Konsept; üretim için şema, hesaplar, footprint, routing, ERC/DRC ve uygun test/doğrulama gereklidir.
