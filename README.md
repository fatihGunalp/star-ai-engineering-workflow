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
    Claude Code, Codex, Cursor, GitHub Copilot ve Gemini CLI için bir Agent Skill.
    AI'ın kod yazmadan önce kritik kararları sana sormasını, kırılma noktalarını
    göstermesini ve gerçekten neyin doğrulandığını dürüstçe raporlamasını sağlar.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Agent_Skill-star--engineering-F97316" alt="Agent Skill: star-engineering" />
    <img src="https://img.shields.io/badge/Claude_Code-Supported-D97757" alt="Claude Code Supported" />
    <img src="https://img.shields.io/badge/Codex-Supported-10A37F" alt="Codex Supported" />
    <img src="https://img.shields.io/badge/Cursor-Supported-111827" alt="Cursor Supported" />
    <img src="https://img.shields.io/badge/GitHub_Copilot-Supported-24292F" alt="GitHub Copilot Supported" />
    <img src="https://img.shields.io/badge/License-MIT-16A34A" alt="MIT License" />
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

</div>

---

## İçindekiler

- [Bu nedir?](#bu-nedir)
- [Hızlı başlangıç](#-hızlı-başlangıç)
- [Kullanım](#-kullanım)
- [Hangi kurulum yolunu seçmeliyim?](#-hangi-kurulum-yolunu-seçmeliyim)
- [Nasıl çalışır?](#️-nasıl-çalışır)
- [Örnekler](#-örnekler)
- [Ne zaman kullanılmalı?](#ne-zaman-kullanılmalı)
- [Bu repo ne değildir?](#bu-repo-ne-değildir)
- [Repository yapısı](#repository-yapısı)
- [Katkıda bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Bu nedir?

AI'a "şifre sıfırlama özelliği ekle" dediğinde birkaç saniyede çalışan kod alırsın. Ama AI bu sırada senin yerine birçok karar vermiş olur: Token ne kadar geçerli? Tekrar kullanılabilir mi? Kullanıcı yoksa ne cevap dönülür? Aynı anda iki istek gelirse ne olur?

**Kodun çalışması, bu kararların sahibi olduğun anlamına gelmez.**

STAR, AI'ın bu görünmez kararları kod yazmadan önce masaya koymasını sağlayan bir çalışma akışıdır:

| STAR olmadan | STAR ile |
|---|---|
| İstek doğrudan koda çevrilir. | İstek önce problem ve kabul kriteri olarak tanımlanır. |
| Eksik gereksinimleri AI sessizce tamamlar. | Sana ait kararlar açıkça sorulur. |
| İlk çalışan çözüm kabul edilir. | Gerçek alternatifler ve bedelleri karşılaştırılır. |
| Kırılma noktaları üretimde fark edilir. | Kırılma senaryoları ve testler koddan önce belirlenir. |
| "Testler geçti" denir, çalıştırılıp çalıştırılmadığı belirsizdir. | Gerçekten çalıştırılan ile planlanan kontroller ayrı raporlanır. |
| Kararlar sohbet geçmişinde kaybolur. | Kararlar kalıcı bir teslim kaydına (`STAR-HANDOFF.md`) yazılır. |

> **Amaç AI'ı yavaşlatmak değil; hızlı üretim sırasında mühendislik sorumluluğunu kaybetmemek.**

## 🚀 Hızlı başlangıç

**Gereksinim:** [Node.js](https://nodejs.org/) 22.20+ ve desteklenen bir coding agent.

Kendi projenin kök dizininde çalıştır:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering
```

Kurucu hangi agent'lara kurmak istediğini sorar. Bu kadar.

Tek bir agent'a, tüm projelerinde geçerli olacak şekilde kurmak istersen:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering -g -a claude-code -y
```

> `npx skills` üçüncü taraf, açık kaynak bir kurucudur ([Skills CLI](https://github.com/vercel-labs/skills)); Anthropic veya OpenAI'ın resmî komutu değildir. Node.js kullanmıyorsan [Python ile kurulum](docs/skills-quickstart.md#5-python-ile-manuel--bağımlılıksız-alternatif) yapabilirsin.

## 💬 Kullanım

Kurulumdan sonra agent'ını yeniden başlat ve görevi normal şekilde yaz. Anlamlı bir değişiklikse (yeni özellik, API, veri modeli, ödeme, kimlik doğrulama...) agent Skill'i kendisi seçebilir. Açıkça çağırmak için:

| Agent | Komut |
|---|---|
| Claude Code | `/star-engineering Şifre sıfırlama özelliği ekle.` |
| Codex | `$star-engineering Şifre sıfırlama özelliği ekle.` |

Agent doğrudan kod yazmak yerine önce şuna benzer bir yanıt verir:

```text
Problem: Parolasını unutan kullanıcı destek ekibine yazmadan hesabına dönemiyor.

Senin karar vermen gerekenler:
1. Token ne kadar süre geçerli olsun?
2. Yeni talep, eski aktif token'ları geçersiz kılsın mı?
3. Sıfırlamadan sonra tüm oturumlar kapatılsın mı?

Önerim: Veritabanında hash olarak saklanan tek kullanımlık token.
Alternatif: İmzalı stateless token — depolama gerektirmez ama iptal edilemez.

Kırılma testleri: aynı token'ın paralel kullanımı, e-posta servisi hatası, süre dolması.
```

Kararları sen verirsin, kod ondan sonra küçük adımlarla yazılır. İş bitince agent neyin **gerçekten** doğrulandığını raporlar ve `docs/features/<özellik>/STAR-HANDOFF.md` dosyasına bir teslim kaydı yazar.

Yazım hatası düzeltme gibi küçük işlerde STAR araya girmez; agent doğrudan değişikliği yapar.

> Otomatik seçim agent'ın kararıdır ve garanti değildir. Emin olmak istediğinde Skill'i açıkça çağır.

## 🧭 Hangi kurulum yolunu seçmeliyim?

STAR'ın **tek bir kaynağı** var: [`skills/star-engineering/SKILL.md`](skills/star-engineering/SKILL.md). Diğer bütün dosyalar bundan üretilir; içerik her yolda aynıdır. Fark yalnızca **ne zaman yüklendiğidir**.

| Yol | Ne zaman yüklenir? | Kimin için? |
|---|---|---|
| **Agent Skill** (önerilen) | Yalnızca görev gerektirdiğinde | Claude Code, Codex, Cursor, Copilot, Gemini CLI |
| **Sürekli kural dosyası** | Her mesajda, her zaman | Skill desteklemeyen araçlar veya STAR'ı her işte zorunlu kılmak isteyen ekipler |
| **Universal metin** | Elle yapıştırdığında | ChatGPT gibi sohbet uygulamaları, proje talimatı alanları |

<details>
<summary><strong>Sürekli kural dosyası kurulumu</strong></summary>

<br />

Kullandığın aracın dosyasını projene kopyala:

| Araç | Kaynak dosya | Projendeki hedef konum |
|---|---|---|
| Claude Code | `rules/claude-code/CLAUDE.md` | `CLAUDE.md` |
| Codex | `rules/codex/AGENTS.md` | `AGENTS.md` |
| Cursor | `rules/cursor/star-engineering.mdc` | `.cursor/rules/star-engineering.mdc` |
| GitHub Copilot | `rules/github-copilot/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Diğer araçlar | `rules/universal/STAR-WORKFLOW.md` | Proje talimatları veya kalıcı bağlam alanı |

Teslim kaydı şablonunu da eklemeyi unutma; kurallar onu bu konumda arar:

```bash
mkdir -p docs/star/templates
cp templates/STAR-HANDOFF.md docs/star/templates/
```

> Projende zaten `CLAUDE.md`, `AGENTS.md` veya benzeri bir dosya varsa üzerine yazma. STAR içeriğini mevcut dosyanın sonuna ekle.

</details>

Kurulum, güncelleme, kaldırma ve doğrulama ayrıntıları için: **[Skill kurulum rehberi](docs/skills-quickstart.md)**.

## ⚙️ Nasıl çalışır?

STAR iki moddan oluşur:

- **Direct mode** — yazım hatası, biçimlendirme, açıkça tanımlı küçük düzeltmeler. Agent değişikliği yapar ve ne kontrol ettiğini söyler. Rapor, tablo veya teslim kaydı üretmez.
- **STAR mode** — davranışı, sözleşmeleri, veriyi, güvenliği, eş zamanlılığı veya operasyonu etkileyen değişiklikler. Küçük görünen bir değişiklik de bu kapsama girebilir.

STAR mode'da agent sırasıyla:

1. **İnceler** — ilgili kodu, testleri ve kuralları okur; gözlemi varsayımdan ayırır.
2. **Tanımlar** — problemi, mevcut ve istenen davranışı, kapsamı ve kabul kriterlerini yazar.
3. **Kararları görünür kılar** — sana ait kararları sorar, gerçek alternatifleri karşılaştırır.
4. **Kırılmayı öngörür** — tekrar, eş zamanlılık, kısmi hata, yetki, zaman aşımı senaryolarını testlere bağlar.
5. **Güvenli olduğunda uygular** — yalnızca engelleyici kararlar için durur, en küçük tutarlı değişikliği yapar.
6. **Dürüstçe doğrular** — çalıştırılan, geçen, başarısız olan ve çalıştırılmayan kontrolleri ayrı raporlar.
7. **Teslim kaydı bırakır** — karar, alternatif, bedel, test ve açık riskleri kaydeder.

Sonunda dört soruyu cevaplayabilmen gerekir:

1. **Neden bu şekilde?**
2. **Başka hangi çözüm vardı?**
3. **Nerede kırılabilir?**
4. **Gerçekte ne doğrulandı?**

## 📚 Örnekler

| Örnek | İçerik |
|---|---|
| [Şifre sıfırlama — istekten kararlara](examples/password-reset/request.md) | Agent'ın koddan önceki yanıtı ve geliştiricinin verdiği kararlar |
| [Şifre sıfırlama — teslim kaydı](examples/password-reset/completed-handoff.md) | Doldurulmuş, açık riskleri gizlemeyen bir `STAR-HANDOFF.md` |
| [Bir siparişin iki kez tahsil edilmesi](skills/star-engineering/references/double-payment.md) | Arayüz kilidinin neden tek başına yeterli olmadığı |

## Ne zaman kullanılmalı?

**STAR mode için:** yeni özellik veya iş kuralı, API sözleşmesi, veri modeli veya migration, kimlik doğrulama ve yetkilendirme, ödeme, harici servis entegrasyonu, eş zamanlılık ve tutarlılık, anlamlı refactoring, kalıcı mimari kararlar.

**Direct mode yeterli:** yazım hatası, değişken adı, biçimlendirme, dokümantasyon, davranış değiştirmeyen mekanik düzenlemeler, beklenen davranışı açık küçük hata düzeltmeleri.

## Bu repo ne değildir?

- Bir güvenlik tarayıcısı veya otomatik code review aracı değildir.
- Kodun doğru, güvenli veya production-ready olduğunu garanti etmez.
- Belirli bir mimariyi zorunlu tutmaz.
- Deneyimli bir mühendisin denetiminin yerini almaz.

Kurallar doğru soruları sordurabilir ve kararları görünür kılabilir. Verdiğin cevabın gerçekten doğru olup olmadığını ise her zaman güvenilir biçimde değerlendiremez.

> Bir kural dosyası sana soru sordurabilir. Mühendislik gelişimi ise verdiğin cevapların denetlenmesini gerektirir. Denetimli gelişim için: [Softbreak STAR](https://softbreak.net).

## Repository yapısı

```text
star-ai-engineering-workflow/
├── skills/star-engineering/     # Tek kaynak: Agent Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml       # Codex arayüz bilgisi
│   ├── assets/                  # Teslim kaydı şablonu
│   └── references/              # Örnek senaryo
├── rules/                       # Skill'den üretilen sürekli kural dosyaları
├── templates/                   # Teslim kaydı (üretilir) ve ek şablonlar
├── examples/                    # Tamamlanmış örnekler
├── docs/                        # Kurulum rehberi ve platform notları
├── scripts/
│   ├── build_rules.py           # rules/ dosyalarını Skill'den üretir
│   └── install_skill.py         # Node.js olmadan kurulum
└── tests/                       # Paket, kurucu ve senkron testleri
```

`templates/` altındaki `FEATURE-BRIEF.md`, `DECISION-RECORD.md` ve `PULL-REQUEST.md` isteğe bağlıdır. Daha resmî bir süreç isteyen ekipler bunları kullanabilir.

## Katkıda bulunma

Hata bildirimi, örnek senaryo veya kural iyileştirmesi için [issue](https://github.com/fatihGunalp/star-ai-engineering-workflow/issues) açabilirsin.

Kural metnini değiştirmek istiyorsan `rules/` altındaki dosyaları **doğrudan düzenleme**; hepsi Skill'den üretilir:

```bash
# 1. skills/star-engineering/SKILL.md dosyasını düzenle
# 2. Üretilen dosyaları güncelle
python3 scripts/build_rules.py
# 3. Testleri çalıştır
python3 -m unittest discover -s tests -v
```

Pull request'lerde bu testler otomatik çalışır; üretilen dosyalar Skill ile uyuşmazsa CI başarısız olur.

## Lisans

[MIT](LICENSE) © Fatih Günalp
