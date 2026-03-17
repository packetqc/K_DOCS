# Social Media Posts — Convention

> Bilingual social media post generation for sharing Knowledge webcards.

---

## When to Use

Upon user request (`/webcard`, social media post request, share request). Generate both EN and FR posts in a single response.

---

## Post Structure

| Section | Content |
|---------|---------|
| **Hook** | 1 sentence — what the page does, why it matters |
| **Features** | 2-4 bullet points — key capabilities, new features |
| **Link** | Webcard URL (shareable, has og:image preview) |
| **Hashtags** | 3-5 relevant tags |

---

## Content Sources

1. **Primary**: og:title + og:description from the webcard HTML redirect page
2. **Secondary**: Front matter keywords from the `.md` page
3. **Add-ons**: Recent features, mobile support, fullscreen mode, new capabilities — always mention what's new or notable

---

## URL Convention

Shareable webcard URLs (these render og:image for social previews):

```
English: https://packetqc.github.io/knowledge/<path>/
French:  https://packetqc.github.io/knowledge/fr/<path>/
```

Examples:
- `https://packetqc.github.io/knowledge/interfaces/main-navigator/`
- `https://packetqc.github.io/knowledge/fr/interfaces/main-navigator/`

---

## Format Template

### English

```
<Hook sentence>

<bullet> Feature 1
<bullet> Feature 2
<bullet> Feature 3

<link>

#hashtag1 #hashtag2 #hashtag3
```

### French

```
<Phrase d'accroche>

<bullet> Fonctionnalite 1
<bullet> Fonctionnalite 2
<bullet> Fonctionnalite 3

<lien>

#hashtag1 #hashtag2 #hashtag3
```

---

## Tone

- Professional but accessible
- Focus on what the user can DO, not implementation details
- Highlight interactive/visual aspects (animated preview, live rendering, themes)
- Keep under 280 chars for Twitter/X compatibility (body text excluding link)

---

## Checklist — New Social Post

1. [ ] Read og:title and og:description from webcard HTML
2. [ ] Read front matter keywords from .md page
3. [ ] Include recent/notable features as add-ons
4. [ ] Generate EN post
5. [ ] Generate FR post
6. [ ] Include shareable webcard URLs (not viewer ?doc= URLs)
7. [ ] Verify links point to existing webcard HTML pages with og:image
