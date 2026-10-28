# STAR Agent Skill — hızlı kurulum ve kullanım

**Bir kez kur, farklı projelerde gerektiğinde kullan.** Bu repo, STAR mühendislik karar akışını [Agent Skills](https://agentskills.io/specification) standardında, taşınabilir bir paket olarak dağıtır.

## 1. Tek komutla kurulum (önerilen)

**Gereksinim:** Node.js 22.20+ ve desteklenen bir coding agent. Komutu STAR reposunda değil, **kendi uygulama projenizin kök dizininde** çalıştırın.

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering
```

Kurucu agent seçimi sorar ve Skill'i hedef projeye yerleştirir. Yalnızca Claude Code'a kurmak için:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering -a claude-code -y
```

Codex için:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering -a codex -y
```

**Her proje yerine kullanıcı genelinde kullanmak için** `-g` ekleyin:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering -g -a claude-code -y
```

Kullanıcı geneli kurulum, aynı makinedeki uygun yerel oturumlarda her projeye ayrı dosya eklemenizi gerektirmez. Hangi modelin/uygulamanın Skill'i keşfettiği o uygulamanın desteğine bağlıdır. Claude, Codex, Cursor, Gemini CLI ve Copilot desteği için araç seçimini standart CLI'ya bırakmak, klasörleri elle yönetmekten daha güvenilirdir.

## 2. Claude Code ve Codex: resmî kullanım

**Claude Code:** Kurulu skill'in adı `star-engineering` ise prompt'un başında `/star-engineering` yazarak açıkça çalıştırabilirsiniz. Alternatif olarak uygun mühendislik görevini normal şekilde tarif ettiğinizde Claude skill'i otomatik seçebilir. Proje kapsamı `.claude/skills/star-engineering/SKILL.md`, kullanıcı kapsamı `~/.claude/skills/star-engineering/SKILL.md`. Doğrudan çağırma ve otomatik kullanım açık kalır; `disable-model-invocation`, `user-invocable: false`, otomatik tool izni veya zorunlu alt-agent kısıtlaması eklenmemiştir.

**Codex CLI / IDE:** `/skills` mevcut skill'leri listelemek içindir; hedef skill'i isteme `$star-engineering` ile yapılır. Proje kapsamı `.agents/skills/star-engineering/SKILL.md`, kullanıcı kapsamı `~/.agents/skills/star-engineering/SKILL.md`. Codex ayrıca `skills/star-engineering/agents/openai.yaml` dosyasındaki isim, kısa açıklama ve varsayılan prompt bilgisini kullanabilir. `allow_implicit_invocation` ayarı değiştirilmedi (varsayılan `true`).

**Etkinleşme farkı:** Her iki uygulama skill'in önce adını ve açıklamasını görür, tam talimatları yalnızca seçildiğinde okur. Açıklamanın kısa, göreve özgü ve ilk kelimelerinin belirleyici olması bu nedenle önemlidir. **Otomatik seçim garanti değildir.** İki uygulamanın da gerçek görev çıktıları ayrıca test edilmelidir.

Resmî belgeler: [Anthropic — Claude Code Skills](https://code.claude.com/docs/en/skills), [OpenAI — Build Skills](https://learn.chatgpt.com/docs/build-skills), [Agent Skills formatı](https://agentskills.io/specification). Platforma göre alınan kararların ayrıntıları: [Claude / Codex uyumluluk notları](claude-codex-alignment.md).

## 3. Nasıl devreye girer?

Agent, her görevde bütün STAR talimatlarını okumak yerine önce `SKILL.md` dosyasının `name` ve `description` bilgisini görür. Yeni özellik, anlamlı hata düzeltmesi, API/veri modeli değişikliği veya riskli mühendislik kararları gibi uygun işlerde Skill'i yükleyebilir. **Otomatik seçimi model/agent belirler; garanti değildir.** Gerekirse Claude Code'da `/star-engineering`, Codex'te `$star-engineering` kullanın.

**Tam STAR modu:** İşin problemini, kritik kararları, seçenekleri, kırılma noktalarını, testleri ve doğrulamayı görünür kılar. **Direct modu:** Yazım hatası, biçimlendirme gibi küçük ve düşük riskli işlerde uzun rapor üretmez.

```text
Ödeme butonuna iki kez basılırsa aynı sipariş için iki kez tahsilat yapılmasın.
star-engineering skill'ini kullan. Koddan önce iş kuralını ve hata senaryolarını çıkar.
```

[Somut örnek: bir siparişin iki kez tahsil edilmesi](../skills/star-engineering/references/double-payment.md). Skill, kodu otomatik olarak doğru, güvenli veya production-ready yapmaz. Test ve insan denetimi gerekir.

## 4. Kurulumu doğrulama, güncelleme, kaldırma

Hedef projenizde:

```bash
npx skills list
npx skills check
npx skills update star-engineering
npx skills remove star-engineering
```

Listeleme, paket kurulumunu gösterir; agent'ın gerçekten Skill'i devreye soktuğunu **kanıtlamaz**. Gerçek agent üzerinde örnek görevi çalıştırıp STAR çıktısının somut kararları, riskleri ve testleri içerip içermediğini kontrol edin.

`npx skills` CLI isteğe bağlı anonim kurulum telemetrisi toplar; CLI belgesine göre `DISABLE_TELEMETRY=1` ile kapatılabilir. Kodu ve dağıtım kaynağını incelemeden üçüncü taraf skill yüklemeyin.

Not: `npx skills` Anthropic veya OpenAI'ın kendi kurucusu değildir; üçüncü taraf bir dağıtım CLI'ıdır. Resmî Codex alternatifi `$skill-installer` ile bir GitHub deposundan skill yüklemektir. Daha geniş ChatGPT/Codex kullanıcı dağıtımı için OpenAI'ın resmî önerisi bir **plugin** paketidir; bu PR doğrudan yüklenebilir bağımsız skill'i hedeflemektedir. CLI belgesi: [Skills CLI](https://www.skills.sh/docs/cli), [komut referansı](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## 5. Python ile manuel / bağımlılıksız alternatif

Node.js kurulu değilse, repo klonlandıktan sonra Python 3.9+ ile:

```bash
# Repo kök dizinindeyken, --project hedef projedir
python3 scripts/install_skill.py --tool claude --project /path/to/my-app
python3 scripts/install_skill.py --tool codex --project /path/to/my-app
python3 scripts/install_skill.py --tool all --project /path/to/my-app
```

Windows'ta `python3` yerine `py -3` kullanabilirsiniz. `--scope user` kullanıcı geneline kurar. Var olan farklı içeriklerin üzerine yazılmaz; CLI kadar kapsamlı bir güncelleme yönetimi sağlamaz. Bu manuel alternatifin kullandığı hedefler: Claude için `.claude/skills/star-engineering`, diğer desteklenen agent'lar için ortak `.agents/skills/star-engineering`.

## 6. Claude.ai web ve başka sohbet modelleri

Claude.ai'nin özel Skill ZIP yükleme yeteneği erişiminizdeyse `skills/star-engineering/` klasörünü `SKILL.md` dosyasıyla birlikte ZIP'leyip yükleyin. Bu yol, Claude Code kurulumu değildir. ChatGPT gibi bir sohbet uygulaması bu agent keşfini desteklemiyorsa `rules/universal/STAR-WORKFLOW.md` dosyasını proje talimatı olarak kullanabilirsiniz; bunu otomatik Skill etkinleşmesiyle karıştırmayın. Bu dosya Skill'den otomatik üretilir, içerik aynıdır.

## 7. Paket testleri

```bash
python3 -m unittest discover -s tests -v
```

Testler paket sözleşmesini ve Python kurulum davranışını kontrol eder. Gerçek Claude/Codex/Cursor/Gemini/Copilot çıktılarının davranış değerlendirmesi ayrıca yapılmalıdır.

## 8. Dağıtım ve sorumluluk sınırları

- Kullanıcının ürün ve yüksek etkili mühendislik kararlarını agent sessizce vermemelidir.
- Skill bir güvenlik tarayıcısı veya kod doğruluk garantisi değildir.
- Repository [MIT Lisansı](../LICENSE) ile dağıtılır.
