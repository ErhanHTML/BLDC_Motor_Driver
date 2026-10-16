# Sistem blok diyagramları

Oklar işlevsel akışı gösterir; bunlar PCB routing'i ya da tamamlanmış elektrik şeması değildir.

## Güç akışı

```mermaid
flowchart LR
  IN[DC giriş] --> PROT[Giriş koruma / ayırma / ön şarj]
  PROT --> LINK[DC-link ve gerilim algılama]
  LINK --> A[Yarım köprü U]
  LINK --> B[Yarım köprü V]
  LINK --> C[Yarım köprü W]
  A --> M[Üç faz motor]
  B --> M
  C --> M
  LINK --> AUX[Yardımcı beslemeler]
```

## Kontrol, ölçüm ve fault

```mermaid
flowchart TD
  MCU[Kontrol MCU: PWM / ADC / zamanlayıcı] --> GA[Gate Driver U]
  MCU --> GB[Gate Driver V]
  MCU --> GC[Gate Driver W]
  GA --> A[Half-Bridge U]
  GB --> B[Half-Bridge V]
  GC --> C[Half-Bridge W]
  H[Hall / opsiyonel encoder] --> MCU
  IA[Faz akımı / DC-link ölçümü] --> MCU
  TEMP[Sıcaklık / bus gerilimi] --> MCU
  CMP[Bağımsız fault algılama] --> LATCH[Donanımsal kapatma / latch]
  LATCH --> GA
  LATCH --> GB
  LATCH --> GC
  LATCH --> MCU
```

Yüksek taraf sürücü beslemesi faz düğümüne referanslı olabilir; tüm sürücüleri tek ortak toprak sembolüne indirgemeyin. Güvenli kapatma mantığı firmware'in zamanında tepki vermesine bağımlı olmamalıdır.
