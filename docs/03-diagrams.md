# Sistem blok diyagramları

Bu revizyonun geçerli ayrıntıları: [Entegre kart tasarım notu](09-integrated-board-revision.md). Diyagramlar işlevsel akıştır; elektrik şeması ve routing değildir.

```mermaid
flowchart LR
  IN[DC giriş] --> PROT[Giriş koruma ve ayırma]
  PROT --> LINK[DC-link]
  LINK --> A[Half-Bridge U]
  LINK --> B[Half-Bridge V]
  LINK --> C[Half-Bridge W]
  A --> M[Motor]
  B --> M
  C --> M
  IN --> AUX[Kart içi buck 12 V]
  AUX --> LV[5 V / 3,3 V]
```

```mermaid
flowchart TD
  MCU[STM32 / PWM / ADC] --> GA[Gate Driver U]
  MCU --> GB[Gate Driver V]
  MCU --> GC[Gate Driver W]
  GA --> A[Half-Bridge U]
  GB --> B[Half-Bridge V]
  GC --> C[Half-Bridge W]
  H[Hall connector] --> MCU
  IA[Kart içi faz akımı / DC-link ölçüm] --> MCU
  T[Sıcaklık / bus gerilimi] --> MCU
  CMP[Bağımsız fault algılama] --> LATCH[Donanımsal shutdown]
  LATCH --> GA
  LATCH --> GB
  LATCH --> GC
  LATCH --> MCU
```

Harici AUX, CAN, RS485 veya current-sense konnektörü bu kart revizyonunda yoktur. High-side besleme ve referansları gerçek gate-driver seçiminde ayrıca doğrulanmalıdır.
