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

## Output Format — MANDATORY

**Each post MUST be output inside a fenced code block** so the user can use the native copy button to paste directly into social media. One code block per language.

Format:

````
**English:**

```
<full post text here, ready to paste>
```

**French:**

```
<full post text here, ready to paste>
```
````

---

## Post Template

Each post inside the code block follows this structure:

```
<Hook sentence>

<emoji> Feature 1
<emoji> Feature 2
<emoji> Feature 3

<webcard URL>

#hashtag1 #hashtag2 #hashtag3
```

Emoji bullets: use contextual emojis (e.g. panel layout, mobile, fullscreen, AI, mindmap).

---

## Tone

- Professional but accessible
- Focus on what the user can DO, not implementation details
- Highlight interactive/visual aspects (animated preview, live rendering, themes)
- Always mention recent/new features (mobile view, fullscreen, new capabilities)
- Keep under 280 chars for Twitter/X compatibility (body text excluding link and hashtags)

---

## Checklist — New Social Post

1. [ ] Read og:title and og:description from webcard HTML
2. [ ] Read front matter keywords from .md page
3. [ ] Include recent/notable features as add-ons
4. [ ] Generate EN post inside a code block
5. [ ] Generate FR post inside a code block
6. [ ] Include shareable webcard URLs (not viewer ?doc= URLs)
7. [ ] Verify links point to existing webcard HTML pages with og:image
