<div align="center">

  <img
    src="docs/assets/softbreak-logo.png"
    alt="Softbreak"
    width="170"
  />

  <h1>STAR AI Engineering Workflow</h1>

  <p>
    <strong>AI ile kod yazarken mühendislik kontrolünü kaybetme.</strong>
  </p>

  <p>
    Cursor, Claude Code, GitHub Copilot, Codex ve benzeri AI araçlarını; doğrudan kod üretmek yerine
    problemi açıklamaya, kritik kararları görünür hâle getirmeye, alternatifleri
    karşılaştırmaya, kırılma noktalarını göstermeye ve mühendislik kararlarını
    kaydetmeye yönlendiren hazır proje kuralları.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Workflow-STAR-F97316" alt="STAR Workflow" />
    <img src="https://img.shields.io/badge/Cursor-Supported-111827" alt="Cursor Supported" />
    <img src="https://img.shields.io/badge/Claude_Code-Supported-D97757" alt="Claude Code Supported" />
    <img src="https://img.shields.io/badge/GitHub_Copilot-Supported-24292F" alt="GitHub Copilot Supported" />
    <img src="https://img.shields.io/badge/Codex-Supported-10A37F" alt="Codex Supported" />
    <img src="https://img.shields.io/badge/Language-TR%20%7C%20EN-2563EB" alt="Turkish and English" />
  </p>

  <p>
    <a href="README.md"><strong>Türkçe</strong></a>
    ·
    <a href="README.en.md">English</a>
  </p>

  <p>
    <a href="https://softbreak.net"><strong>🌐 Web Sitesi</strong></a>
    ·
    <a href="https://www.youtube.com/@softbreak"><strong>▶ YouTube Kanalı</strong></a>
  </p>

  <p>
    <a href="#-hızlı-başlangıç">🚀 Hızlı Başlangıç</a>
    ·
    <a href="#-nasıl-çalışır">⚙️ Nasıl Çalışır?</a>
    ·
    <a href="#-örnek-mühendislik-teslim-kaydı">📄 Örnek Çıktı</a>
    ·
    <a href="#-dört-mühendislik-sorusu">🧭 Dört Soru</a>
  </p>

</div>

---

<details>
<summary><strong>STAR AI Engineering Workflow ne yapar?</strong></summary>

<br />

Bu çalışma sistemi, AI destekli geliştirme sırasında şu davranışları teşvik eder:

- Kullanıcının isteğini kod görevine çevirmeden önce problemi yeniden tanımlar.
- Eksik kabul kriterlerini ve görünmeyen varsayımları ortaya çıkarır.
- Kullanıcıya ait ürün ve mimari kararlarını sessizce uydurmaz.
- Uygulanabilir alternatifleri ve bunların bedellerini karşılaştırır.
- Kırılma senaryolarını ve test planını koddan önce görünür hâle getirir.
- Değişiklikleri küçük ve açıklanabilir adımlarla üretir.
- Çalışma sonunda kararları `STAR-HANDOFF.md` dosyasına kaydeder.

</details>

## Neden Bu Repo Var?

AI araçlarına çoğu zaman şöyle bir istek veriyoruz:

```text
Bu projeye şifre sıfırlama özelliği ekle.
```

AI birkaç saniye içinde çalışan bir çözüm üretebilir. Ancak bu sırada farkında olmadan birçok karar vermiş olabilir:

- Token nasıl üretilecek?
- Nerede ve hangi biçimde saklanacak?
- Ne kadar süre geçerli olacak?
- Tekrar kullanılabilecek mi?
- Kullanıcı sistemde yoksa nasıl cevap verilecek?
- Aynı anda birden fazla istek gelirse ne olacak?
- Hangi testler yazılacak?
- Hangi güvenlik ve operasyon maliyetleri kabul edilecek?

Kodun çalışması, bu kararların sahibi olduğun anlamına gelmez.

Bu repo, AI’ın senin yerine görünmez mühendislik kararları vermesini azaltmak ve seni karar sürecinin içinde tutmak için oluşturuldu.

> **Amaç AI’ı yavaşlatmak değil; hızlı üretim sırasında mühendislik sorumluluğunu kaybetmemektir.**

## Önce ve Sonra

| STAR olmadan | STAR ile |
|---|---|
| İstek doğrudan koda çevrilir. | İstek önce problem olarak yeniden tanımlanır. |
| Eksik gereksinimler AI tarafından sessizce tamamlanır. | Eksik kararlar kullanıcıya görünür biçimde sorulur. |
| İlk çalışan çözüm kabul edilir. | Alternatifler ve bedelleri karşılaştırılır. |
| Kırılma noktaları üretimden sonra fark edilir. | Kırılma senaryoları ve testler koddan önce planlanır. |
| Kararlar sohbet geçmişinde kaybolur. | Kararlar kalıcı bir mühendislik teslim kaydına yazılır. |
| Kullanıcı kodu açıklamakta zorlanır. | Kullanıcıya kodu savunması gereken sorular bırakılır. |

## 🧩 Yeni: Claude Skill ve çoklu Agent desteği

STAR artık yalnızca sürekli yüklü proje kuralları değil, görev gerektiğinde etkinleşebilen **taşınabilir bir Agent Skill** olarak da paketlendi.

- **Tek kaynak:** [`skills/star-engineering/SKILL.md`](skills/star-engineering/SKILL.md)
- **Kurulum:** Claude Code, Codex, Gemini CLI, GitHub Copilot agent ve Cursor için bağımlılıksız `scripts/install_skill.py`
- **Gerçek hayattan örnek:** [Bir yemek siparişinin iki kez tahsil edilmesi](skills/star-engineering/references/double-payment.md) — arayüz kilidinin neden tek başına yeterli olmadığını gösterir.
- **Tam rehber:** [Skill kurulumu ve doğrulama](docs/skills-quickstart.md)

```bash
# Bu repo klonlandıktan sonra, kendi uygulamanız için:
python3 scripts/install_skill.py --tool claude --project /path/to/my-app
python3 scripts/install_skill.py --tool codex --project /path/to/my-app
```

Skill, mevcut `CLAUDE.md` / `AGENTS.md` dosyalarının yerini almak zorunda değildir; farklı bir kullanım katmanıdır. **Otomatik hata yakalama veya güvenlik garantisi sağlamaz.**

## 🚀 Hızlı Başlangıç

### 1. Kullandığın Aracı Seç

| Araç | Kaynak dosya | Projendeki hedef konum |
|---|---|---|
| Cursor | `rules/cursor/star-engineering.mdc` | `.cursor/rules/star-engineering.mdc` |
| Claude Code | `rules/claude-code/CLAUDE.md` | `CLAUDE.md` |
| GitHub Copilot | `rules/github-copilot/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Codex | `rules/codex/AGENTS.md` | `AGENTS.md` |
| Diğer araçlar | `rules/universal/STAR-WORKFLOW.md` | Proje talimatları veya kalıcı bağlam alanı |

### 2. Kural Dosyasını Projene Ekle

Örnek: Cursor kullanıyorsan

```text
star-ai-engineering-workflow/
└── rules/
    └── cursor/
        └── star-engineering.mdc
```

dosyasını kendi projen içinde şu konuma kopyala:

```text
my-project/
└── .cursor/
    └── rules/
        └── star-engineering.mdc
```

> Projende hâlihazırda `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` veya benzeri bir talimat dosyası varsa mevcut içeriği silme. STAR kurallarını proje özelindeki talimatlarla kontrollü biçimde birleştir.

### 3. Normal İsteğini Yaz

```text
Bu projeye şifre sıfırlama özelliği ekle.
```

AI’ın doğrudan kod üretmek yerine önce şuna benzer bir yanıt vermesi beklenir:

```text
Çözmeye çalıştığımız problem:

Kullanıcının mevcut parolasını bilmeden, e-posta üzerinden güvenli
biçimde yeni parola belirleyebilmesi.

Netleştirilmesi gereken kararlar:

- Sıfırlama token'ı ne kadar süre geçerli olacak?
- Token tek kullanımlık mı olacak?
- Kullanıcı sistemde bulunmuyorsa nasıl cevap verilecek?
- Aktif token varken yeni bir talep oluşturulabilecek mi?

Uygulanabilir yaklaşımlar:

1. Token'ı veritabanında hash olarak saklamak
2. İmzalı ve stateless token kullanmak

Bu kararları netleştirmeden kod üretmeye başlamıyorum.
```

### 4. Kararları Ver ve Üretime Geç

AI’ın ürün ihtiyacını bilmeden veremeyeceği kararları sen netleştirirsin.

Ardından kod:

- küçük adımlarla,
- açıklanabilir değişikliklerle,
- görünür varsayımlarla,
- önceden belirlenmiş test senaryolarıyla

üretilir.

### 5. Teslim Kaydını Al

Çalışma sonunda aşağıdaki gibi bir dosya oluşturulur:

```text
docs/features/password-reset/STAR-HANDOFF.md
```

Bu dosya, yalnızca ne yapıldığını değil, **neden yapıldığını** da kaydeder.

## ⚙️ Nasıl Çalışır?

STAR mühendislik akışı üç aşamadan oluşur.

### 1. Koddan Önce

AI:

1. İsteği çözülmesi gereken problem olarak yeniden tanımlar.
2. Eksik kabul kriterlerini belirler.
3. Kullanıcıya sorulmadan verilmemesi gereken kararları görünür hâle getirir.
4. Uygulanabilir alternatifleri karşılaştırır.
5. Önerdiği yaklaşımın avantajlarını ve bedellerini açıklar.
6. Muhtemel kırılma senaryolarını belirler.
7. Yazılması gereken testleri koddan önce listeler.

### 2. Kod Sırasında

AI:

- küçük ve açıklanabilir değişiklikler yapar,
- varsayımlarını gizlemez,
- kapsam dışına sessizce çıkmaz,
- kullanıcıya ait ürün kararlarını kendisi uydurmaz,
- yaptığı değişikliğin yalnızca ne olduğunu değil, nedenini de açıklar.

### 3. Koddan Sonra

AI:

1. Yapılan değişiklikleri özetler.
2. Seçilen yaklaşımı ve nedenini kaydeder.
3. Değerlendirilen alternatifleri belirtir.
4. Kırılma noktalarını ve bilinen sınırlamaları yazar.
5. Yazılan ve eksik kalan testleri listeler.
6. Açık kararları görünür bırakır.
7. Kullanıcının kodu savunabilmesi için sorular üretir.
8. `STAR-HANDOFF.md` dosyasını oluşturur.

## 📄 Örnek Mühendislik Teslim Kaydı

```markdown
# Şifre Sıfırlama — Mühendislik Teslim Kaydı

## Çözülen Problem

Kullanıcıların mevcut parolalarını bilmeden, e-posta üzerinden
güvenli biçimde yeni parola belirleyebilmesi.

## Kabul Kriterleri

- Geçerli kullanıcı sıfırlama bağlantısı talep edebilmeli.
- Kullanıcı sistemde bulunmasa bile aynı genel yanıt dönülmeli.
- Token yalnızca bir kez kullanılabilmeli.
- Süresi dolmuş token reddedilmeli.
- Başarılı işlem sonrasında eski parola geçersiz olmalı.

## Seçilen Yaklaşım

Tek kullanımlık, veritabanında hash olarak saklanan sıfırlama token'ı.

## Neden Bu Yaklaşım Seçildi?

Token'ın iptal edilebilmesi, kullanımının takip edilebilmesi ve tekrar
kullanımının engellenmesi gerektiği için.

## Değerlendirilen Alternatif

İmzalı ve stateless token.

### Avantajı

Token doğrulaması için veritabanı sorgusu gerektirmemesi.

### Neden Seçilmedi?

Tekil token iptali, tekrar kullanım kontrolü ve kullanım takibi daha zor.

## Kararın Bedeli

- Token üretimi ve doğrulaması için veritabanı erişimi gerekir.
- Süresi dolan token kayıtları için temizleme stratejisi gerekir.
- Paralel talepler için tutarlılık kuralları açıkça tanımlanmalıdır.

## Nerede Kırılabilir?

- Aynı token iki kez kullanılırsa
- Aynı kullanıcı paralel sıfırlama talepleri gönderirse
- E-posta servisi başarısız olursa
- Token süresi işlem sırasında dolarsa
- Veritabanı işlemi yarıda kalırsa

## Yazılan Testler

- Geçerli token ile parola değiştirilebilir
- Süresi dolmuş token reddedilir
- Kullanılmış token tekrar kullanılamaz
- Olmayan kullanıcı için kullanıcı varlığı açığa çıkarılmaz

## Eksik Kalan Testler

- Paralel token kullanım denemesi
- E-posta servisi başarısızlığı
- Aktif token varken yeni talep oluşturulması

## Bilinen Sınırlamalar

Rate limiting henüz uygulanmadı.

## Bu Kararı Savunmak İçin Bilmen Gerekenler

- Token neden düz metin olarak saklanmıyor?
- Stateless yaklaşım neden tercih edilmedi?
- Kullanıcı varlığı neden gizleniyor?
- Paralel istekler nasıl yönetiliyor?
- Bu karar hangi koşullarda değiştirilmelidir?
```

## 🧭 Dört Mühendislik Sorusu

Bu çalışma sisteminin merkezinde dört soru bulunur.

### 1. Bu kod neden böyle yazıldı?

Kullanılan yapının ve verilen kararın arkasındaki nedeni açıklayabiliyor musun?

### 2. Başka bir çözüm olabilir miydi?

En az bir uygulanabilir alternatifi ve iki yaklaşım arasındaki bedelleri biliyor musun?

### 3. Bu çözüm nerede kırılır?

Beklenmeyen girdilerde, veri büyüdüğünde, eş zamanlı işlemlerde veya bağımlılıklar başarısız olduğunda ne olacağını öngörebiliyor musun?

### 4. Bu kararı bir başkasına savunabilir misin?

Kararın yalnızca ne olduğunu değil, neden kabul edilebilir olduğunu ve hangi koşullarda değiştirilmesi gerektiğini açıklayabiliyor musun?

> Kodun çalışması, bu soruların cevaplandığı anlamına gelmez.

## Ne Zaman Kullanılmalı?

Tam STAR akışı özellikle şu tür değişikliklerde kullanılmalıdır:

- Yeni özellik geliştirme
- İş kuralı ekleme veya değiştirme
- API sözleşmesi oluşturma
- Veri modeli değişikliği
- Harici servis entegrasyonu
- Kimlik doğrulama ve yetkilendirme
- Mimari değişiklik
- Güvenlik kararı
- Birden fazla dosyayı etkileyen anlamlı refactoring
- Kalıcı teknik karar

## Ne Zaman Kullanılmamalı?

Her küçük işlem için uzun bir karar süreci gerekmez.

Aşağıdaki işler genellikle doğrudan yapılabilir:

- Yazım hatası düzeltme
- Değişken adı değiştirme
- Açıklama veya dokümantasyon güncelleme
- Basit biçimlendirme
- Davranış değiştirmeyen mekanik düzenleme
- Açıkça tanımlanmış küçük hata düzeltmesi

Ancak küçük görünen bir değişiklik güvenliği, veriyi, sistem davranışını veya dışarıya açık bir sözleşmeyi etkiliyorsa STAR akışı uygulanmalıdır.

## Şablonlar

| Şablon | Amaç |
|---|---|
| `FEATURE-BRIEF.md` | Koddan önce problemi, kapsamı, kabul kriterlerini ve açık kararları tanımlar. |
| `STAR-HANDOFF.md` | Çalışma sonunda yapılan kararları, riskleri ve sınırlamaları kaydeder. |
| `DECISION-RECORD.md` | Kalıcı veya geri döndürülmesi maliyetli teknik kararları kayıt altına alır. |
| `PULL-REQUEST.md` | Değişikliğin yalnızca ne yaptığını değil, neden yapıldığını açıklamaya yardımcı olur. |

## Repository Yapısı

```text
star-ai-engineering-workflow/
│
├── README.md
├── README.en.md
│
├── rules/
│   ├── cursor/
│   │   └── star-engineering.mdc
│   ├── claude-code/
│   │   └── CLAUDE.md
│   ├── github-copilot/
│   │   └── copilot-instructions.md
│   ├── codex/
│   │   └── AGENTS.md
│   └── universal/
│       └── STAR-WORKFLOW.md
│
├── templates/
│   ├── FEATURE-BRIEF.md
│   ├── STAR-HANDOFF.md
│   ├── DECISION-RECORD.md
│   └── PULL-REQUEST.md
│
├── examples/
│   └── password-reset/
│       ├── request.md
│       └── completed-handoff.md
│
└── docs/
    └── assets/
        └── softbreak-logo.png
```

## Bu Repo Ne Değildir?

Bu repo:

- prompt koleksiyonu değildir,
- otomatik code review aracı değildir,
- güvenlik tarayıcısı değildir,
- kod kalite garantisi vermez,
- belirli bir mimariyi zorunlu tutmaz,
- Clean Architecture şablonu değildir,
- AI’ın verdiği her cevabı doğru hâle getirmez,
- mentor veya deneyimli mühendis denetiminin yerini almaz.

Kurallar soru sordurabilir ve kararları görünür hâle getirebilir.

Fakat verdiğin cevabın gerçekten doğru olup olmadığını her zaman güvenilir biçimde değerlendiremez.

## STAR ile Sınırı

Bu repository, STAR metodolojisinin tamamı değildir.

Yalnızca AI destekli geliştirme sırasında kararları görünür hâle getiren çalışma katmanıdır.

### Ücretsiz Workflow

- AI’ın görünmez varsayımlarını azaltır.
- Doğru soruların sorulmasını teşvik eder.
- Kararların kayıt altına alınmasını sağlar.
- Kullanıcının öz değerlendirme yapmasına yardım eder.

### Denetimli Mühendislik Gelişimi

- Verilen cevabın gerçekten doğru olup olmadığını sorgular.
- Görünmeyen düşünce hatalarını yakalar.
- Üretimi gerçek code review’a açar.
- Geri bildirimden sonra yeniden üretimi zorunlu kılar.
- Gelişimi zaman içinde takip eder.
- Dış denetim ve sorumluluk oluşturur.

> Bir kural dosyası sana soru sordurabilir.  
> Mühendislik gelişimi ise verdiğin cevapların denetlenmesini gerektirir.

## Temel İlke

AI kod üretebilir.

Fakat:

- problemi doğru tanımlamak,
- eksik kararları görmek,
- alternatifleri değerlendirmek,
- hatalı çıktıyı fark etmek,
- kırılma noktalarını öngörmek,
- kodu denetime açmak,
- verilen kararın sorumluluğunu almak

hâlâ mühendislik işidir.

> **Bu repo sana yeni bir proje vermiyor. Kendi projen üzerinde AI ile daha bilinçli çalışmanı sağlayan bir mühendislik sistemi veriyor.**

## Katkıda Bulunma

Hata bildirimi, örnek senaryo, araç entegrasyonu veya kural iyileştirmesi önerileri için issue açabilirsin.

Katkı kuralları `CONTRIBUTING.md` dosyası eklendikten sonra burada ayrıca bağlantılanacaktır.

## Lisans

Lisans dosyası repository public olmadan önce eklenecektir.

---

<div align="center">

  <p>
    <strong>Softbreak STAR</strong>
  </p>

  <p>
    Eğitim değil; denetimli mühendislik gelişim sistemi.
  </p>

</div>
