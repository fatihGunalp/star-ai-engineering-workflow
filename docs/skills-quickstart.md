# STAR Agent Skill — kurulum ve kullanım

Bu repo iki kullanım biçimi sunar:

- **Kalıcı proje talimatları**: `rules/` altındaki `CLAUDE.md`, `AGENTS.md`, Cursor/Copilot kuralları; proje boyunca geçerli davranışlar.
- **İsteğe göre yüklenen Agent Skill**: `skills/star-engineering/SKILL.md`; görevle eşleştiğinde devreye girer. Aynı kuralları her sohbete uzun uzun yapıştırmak gerekmez.

Bu paket, [Agent Skills](https://agentskills.io/) biçimini izler; modellerin kendilerinden ziyade **kullandıkları uygulamanın/agent'ın** skill keşif desteğine dayanır.

## Hızlı kurulum (Python 3.9+, ek paket yok)

Repo'yu klonladıktan sonra aşağıdaki komutu çalıştırın. Proje yolunu **skill'in kullanılacağı projenin** yolu olarak verin; STAR reposunun yolu olarak değil.

```bash
git clone https://github.com/fatihGunalp/star-ai-engineering-workflow.git
cd star-ai-engineering-workflow

# Claude Code (macOS / Linux / Windows; Python kuruluysa)
python3 scripts/install_skill.py --tool claude --project /path/to/my-app

# Codex
python3 scripts/install_skill.py --tool codex --project /path/to/my-app

# Gemini CLI, GitHub Copilot agent veya Cursor
python3 scripts/install_skill.py --tool gemini --project /path/to/my-app
python3 scripts/install_skill.py --tool copilot --project /path/to/my-app
python3 scripts/install_skill.py --tool cursor --project /path/to/my-app
```

Windows'ta `python3` yerine `py -3` veya `python` komutunu kullanın. `/path/to/my-app` yerine gerçek proje yolunu yazın. Kullanıcı düzeyinde tüm projeler için `--scope user` verin; `--project` gerekmez.

**Mevcut skill dosyaları üzerine yazılmaz.** Aynı içerik zaten yüklüyse değişiklik yapılmaz; farklı dosya varsa kurulum hata verir ve mevcut içerik korunur. Yeni sürüm için önce kendi değişikliklerinizi yedekleyin.

## Hangi araç hangi klasörü kullanır?

| Araç | Proje içi hedef | Kullanıcı düzeyi |
|---|---|---|
| Claude Code | `.claude/skills/star-engineering/SKILL.md` | `~/.claude/skills/star-engineering/SKILL.md` |
| Codex | `.agents/skills/star-engineering/SKILL.md` | `~/.agents/skills/star-engineering/SKILL.md` |
| Gemini CLI | `.agents/skills/star-engineering/SKILL.md` | `~/.agents/skills/star-engineering/SKILL.md` |
| GitHub Copilot agent | `.agents/skills/star-engineering/SKILL.md` | `~/.agents/skills/star-engineering/SKILL.md` (desteklenen istemcilerde) |
| Cursor | `.agents/skills/star-engineering/SKILL.md` | `~/.agents/skills/star-engineering/SKILL.md` |

Bu dört agent ortak `.agents/skills` konumunu kullanabildiği için tek kurulumdan yararlanabilir. Claude Code için ayrıca `.claude/skills` konumuna kopyalayın. `--tool all` her iki konuma kopyalar; iki konumu birden tarayan istemciler aynı isimli skill'i iki kez gösterebilir. Kurulumdan sonra agent'ı yenileyin/yeniden başlatın.

**Kaynaklar (resmî):** [Claude Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Codex Skills](https://learn.chatgpt.com/docs/build-skills), [Gemini CLI Skills](https://geminicli.com/docs/cli/skills/), [Copilot Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Cursor Skills](https://cursor.com/docs/skills).

## Claude.ai (web) için

Claude.ai'deki özel skill yükleme işlevi ile bir ZIP paketini içeri alabilirsiniz. Klasörü `SKILL.md` ile birlikte paketleyin:

```bash
cd skills
zip -r star-engineering.zip star-engineering
```

Claude.ai tarafındaki güncel Skills ekranından yükleyin. Bu işlem Claude Code'un proje klasörü kurulumundan ayrıdır; hesap özelliklerine ve kod çalıştırma desteğine bağlıdır.

## Skill desteklemeyen sohbet araçları

Bir web sohbeti ya da uygulama Agent Skills keşfini desteklemiyorsa, aynı `SKILL.md` talimatlarını proje talimatlarına veya sohbete verin. Bu, **otomatik skill etkinleşmesiyle aynı şey değildir**. Orijinal `rules/universal/STAR-WORKFLOW.md` de evrensel alternatif olarak kullanılabilir.

## Kullanım

Kod projenizde şu tür gerçek bir görev isteyin:

```text
Ödeme butonuna iki kez basılınca aynı sipariş için ikinci tahsilat oluşmasın.
STAR ile problemi ve testleri önce ortaya çıkar.
```

İyi bir sonuç hemen kod üretmek yerine *hangi isteğin aynı ödeme sayılacağı*, *sunucu idempotency koruması*, *eş zamanlı çağrılar*, *timeout sonrası durum* ve *test kanıtlarını* görünür kılmalıdır. Açıklamalı örnek: [çift ödeme senaryosu](../skills/star-engineering/references/double-payment.md).

## Doğrulama

```bash
python3 -m unittest discover -s tests -v
```

Bu testler **kurulum betiğinin dosya yerleşimini ve üzerine yazmama davranışını** kontrol eder. Claude/Codex/Gemini/Copilot/Cursor üzerinde gerçek bir çalıştırma yapıldığını **kanıtlamaz**. Her agent'ta skill keşfi ve verilen göreve uygun çıktı ayrıca kontrol edilmelidir.

## Sınırlar

- Skill kodu otomatik olarak güvenli veya hatasız kılmaz; gerçek test, inceleme ve karar sahipliği gerekir.
- Bir `SKILL.md` dosyası Instagram yorumlarına otomatik DM göndermez. Yorum tetikleyicisi, hesap izinleri ve mesaj teslimi ayrı bir Meta uyumlu entegrasyon gerektirir.
- Skill'i dağıtmadan önce proje lisansı ve üçüncü taraf katkı politikası ayrıca netleştirilmelidir.
