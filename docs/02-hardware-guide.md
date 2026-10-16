# Donanım tasarım rehberi

Bu rehber bir şema/netlist değildir. Bileşenler yalnızca gereksinim ve datasheet uygunluğu teyit edildiğinde kesinleştirilmelidir.

## Güç katı

- Üç yarım köprüyü benzer parazitik empedanslarla yerleştir; anahtarlama döngüsünü DC-link'in yerel yüksek frekanslı kapasitörleriyle küçük tut.
- MOSFET değerlendirmesinde VDS transient marjı, sıcaklıktaki RDS(on), gate charge, Qrr/Eoss, SOA ve soğutma yolunu birlikte incele. Katalog akım derecesini doğrudan PCB akım kapasitesi sayma.
- Faz düğümü yüksek dv/dt bölgesidir; Hall ve analog ölçüm hatlarını buradan uzak tut.

## Gate-driver mimarisi

- Her faza bir bağımsız high-side/low-side sürücü ayrılmalı; toplam üç entegre. DRV ailesi proje adayı olarak kullanılmayacak.
- Bağımsız high-side referansı, uygun besleme/UVLO, giriş lojik seviyeleri, negatif switch-node transient sınırı ve CMTI kontrol edilmeli.
- Gate turn-on/turn-off yolları, Miller etkisi ve gerekirse Kelvin source bağlantısı gözden geçirilmeli.
- Bootstrap veya yüzer besleme kararı, yüksek tarafın uzun süre açık kalabildiği durumlar dahil kontrol stratejisine göre verilmelidir.
- Dead-time ve tüm kapıları güvenli kapatan **MCU'dan bağımsız** fault yolu önerilir.

## Akım ve gerilim ölçümü

- FOC için geçerli faz akımı örnekleme pencereleri gerekir; üç faz ölçüm yeri/alternatif iki faz topolojisi ADC tetikleme planıyla birlikte kararlaştırılmalı.
- Akım yükseltecinin common-mode, PWM rejection, offset, kazanç, bant genişliği ve aşırı yükten toparlanma özellikleri incelenmeli.
- Güç shunt'ları için Kelvin algılama; ADC için uygun referans, filtre ve analog dönüş yolu önerilir.
- Bara gerilim bölücüsü, gerilim dayanımı ve filtre gecikmesiyle birlikte ele alınmalıdır.

## Konum ve kontrol I/O

- Hall girişlerinde ESD, mantık seviyeleri, konnektör pinlemesi ve hatalı kod/zaman aşımı algısı tasarlanmalı.
- Uzun motor kablolarında sinyal-dönüş çifti, ekran bağlantı stratejisi ve giriş filtre gecikmesi bütün hatlarda değerlendirilmelidir.
- Encoder opsiyonu için yer ve zamanlayıcı pinleri ayrılabilir; üç Hall, sektör içinde doğrudan sürekli hassas açı sağlamaz.

## Beslemeler ve PCB

- Gate sürücü akımı ve MCU/analog akımlar için ayrı güç bütçeleri oluştur; DC/DC başlangıç, brownout ve fault davranışını doğrula.
- Güç dönüşlerini analog toprakla gelişigüzel birleştirme; ortak referans/izolasyon sınırları şemada ve PCB'de tutarlı olsun.
- Sıcak komponentlerin konumunu, ölçüm devrelerini, konnektör çıkışlarını ve soğutucu mekanik bağlantısını beraber değerlendir.
- Ön şarj, sigorta, kontaktör, bus deşarjı ve rejeneratif aşırı gerilim tehlikesi sistem seviyesinde koordine edilmeli.

## Tasarım inceleme kapıları

Şema/ERC; PWM-fault durum tablosu; besleme sınırları; sürücü-MOSFET eşleşmesi; ADC zamanlaması; güç döngüsü/parazitik incelemesi; izolasyon ve çevresel gereksinimler; termal ve EMC doğrulama planı.
