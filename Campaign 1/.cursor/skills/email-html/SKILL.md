---
name: email-html
description: >
  Build production-ready HTML email templates with full responsiveness, cross-client compatibility, and
  marketing strategy baked in. Use this skill whenever the user asks to create, design, build, or generate
  an HTML email, newsletter, promotional email, transactional email, drip campaign email, or any email
  template — even if they just say "make me an email for X" or "design an email blast" or "write a
  marketing email". Also trigger when the user wants to convert a screenshot/image/brief into a working
  HTML email file. This skill covers the complete pipeline: marketing analysis → content hierarchy →
  responsive table layout → inline CSS → inline SVG asset generation → cross-client testing checklist.
---

# Email HTML Skill

Build responsive, standards-compliant HTML email templates with strong marketing strategy embedded in
the design decisions. Every email produced by this skill should be immediately deployable in any ESP
(Mailchimp, Klaviyo, HubSpot, Sendinblue, etc.) or raw SMTP send.

---

## Phase 1 — Marketing Strategy Analysis

Before writing a single line of HTML, read `references/marketing-strategy.md` for the section
that matches the email goal (funnel stage, B2B/B2C, offer type, and email-type blueprint). Then
analyse the email's purpose. Extract or infer:

### Audience & Goal Matrix
| Signal | What to extract |
|---|---|
| **Who** | B2B (decision-makers, procurement) vs B2C (end consumer) |
| **Stage** | Awareness / Consideration / Decision / Retention / Re-engagement |
| **Desired action** | One primary CTA — every design decision should serve this CTA |
| **Tone register** | Formal/corporate ↔ Friendly/playful ↔ Urgent/FOMO |
| **Trust signals needed** | Logos, testimonials, guarantees, certifications, social proof |

### Hierarchy of Persuasion (apply in this order)
1. **Attention** — Hero headline stops the scan. One idea, maximum impact.
2. **Interest** — Subhead or benefit line. "What's in it for me?" answered immediately.
3. **Desire** — Visual proof, offer specifics, social proof. Make the outcome vivid.
4. **Action** — One unmissable CTA. Repeated 2–3× if long email.
5. **Reassurance** — Reduce friction below the CTA: guarantees, deadlines, secondary info.

### Strategic Decisions to Document (comment in HTML)
- Primary CTA text and target URL
- Offer validity / scarcity signal (if any)
- Above-the-fold promise (must fit ~300px preview height on mobile)
- Preview text / preheader (50–90 chars, extends subject line)

---

## Phase 2 — Layout Architecture

### The Golden Rule: Tables for Structure, Inline CSS for Style
Email clients strip `<style>` blocks, `<link>` tags, and most CSS classes. Use:
- `<table>` / `<tr>` / `<td>` for ALL layout (never CSS grid/flexbox for structure)
- `style=""` inline attributes on every element that needs styling
- `role="presentation"` on all layout tables
- `cellpadding="0" cellspacing="0" border="0"` on every table

### Wrapper Pattern (always use this shell)
```html
<table width="100%" bgcolor="#BACKGROUND" cellpadding="0" cellspacing="0" role="presentation">
  <tr><td align="center" style="padding:20px 0;">

    <!-- MAIN WRAPPER: fixed width desktop, fluid mobile -->
    <table width="620" class="wrapper" cellpadding="0" cellspacing="0" role="presentation"
           style="width:620px; max-width:620px; background:#ffffff; border-radius:0 0 16px 16px; overflow:hidden;">
      <!-- sections go here -->
    </table>

  </td></tr>
</table>
```

**Standard widths:** 600–640px desktop wrapper. Never exceed 640px.

### Section Anatomy
Each logical block of the email is a `<tr>` inside the wrapper. Common sections:
1. **Header** — Logo + brand colour bar
2. **Hero** — Headline + subhead (above the fold)
3. **Offer / Value Block** — Coupon, product, benefit grid
4. **CTA** — Primary button (standalone row, centred)
5. **Social Proof** — Testimonials, logos, stats
6. **How It Works** — 2–4 step process cards
7. **Info Bar** — Terms, deadlines, conditions
8. **Brand / Partner Rail** — Compatible logos
9. **Footer** — Trust icons + contact + legal

---

## Phase 3 — Responsiveness Rules

### Required `<head>` Block
```html
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Preheader (hidden preview text) -->
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all;">
  PREHEADER TEXT HERE — 50–90 chars extending the subject line &#8203;&nbsp;
</div>
```

### Responsive `<style>` Block (place in `<head>`)
```css
/* Resets */
body, table, td, a { -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }
table, td          { mso-table-lspace:0pt; mso-table-rspace:0pt; }
img                { -ms-interpolation-mode:bicubic; border:0; display:block; outline:none; }
body               { margin:0; padding:0; }

/* Mobile breakpoint — 620px is the wrapper width */
@media only screen and (max-width:640px) {
  .wrapper      { width:100% !important; }
  .mob-pad      { padding-left:16px !important; padding-right:16px !important; }
  .mob-stack    { display:block !important; width:100% !important; padding:12px 0 !important; }
  .mob-hide     { display:none !important; }
  .mob-full     { width:100% !important; max-width:100% !important; }
  .mob-center   { text-align:center !important; }
  .mob-h1       { font-size:28px !important; line-height:36px !important; }
  .mob-h2       { font-size:22px !important; line-height:30px !important; }
  .mob-body     { font-size:16px !important; line-height:26px !important; }
  .mob-cta a    { font-size:18px !important; padding:14px 24px !important; }
  .mob-coupon   { font-size:40px !important; letter-spacing:1px !important; }
}
```

### Mobile Stacking Pattern
Multi-column layouts (2-col, 3-col) use `display:block` override:
```html
<td class="mob-stack" style="width:33%; vertical-align:top; padding:0 6px;">
  <!-- card content -->
</td>
```
On mobile, `.mob-stack` makes each card full-width and stacks vertically.

---

## Phase 4 — Typography & Colour Standards

### Font Stack (web-safe only — no Google Fonts in email)
```
Headlines:  font-family: 'Arial Black', Arial, sans-serif; font-weight:900;
Body:       font-family: Arial, Helvetica, sans-serif; font-weight:400;
Mono/code:  font-family: 'Courier New', Courier, monospace;
```

### Type Scale
| Role | Desktop | Mobile class |
|---|---|---|
| H1 Hero | 34–40px | `mob-h1` → 28px |
| H2 Section | 20–26px | `mob-h2` → 22px |
| Body | 14–16px | `mob-body` → 16px |
| Caption/legal | 11–12px | unchanged |
| CTA button | 18–22px | `mob-cta` → 18px |
| Coupon code | 52–60px | `mob-coupon` → 40px |

### Colour Usage Rules
- **Brand primary**: use for header bg, CTA button bg, numbered badges, section headers
- **Brand accent**: use for highlights, prices, urgency text
- **Success green** (`#18b81e` or similar): CTA buttons, confirmation checks, positive badges
- **Warning/urgency red** (`#cc0000` / `#e00000`): prices, deadlines, scarcity signals
- **White** (`#ffffff`): card backgrounds, text on dark bg
- **Light bg** (`#e8edf5` or similar): email canvas background
- All `color` and `background` values MUST be set inline, not just in `<style>`

---

## Phase 5 — CTA Button Standards

Buttons must work even when images are blocked. **Never use image-based buttons.**

```html
<!-- Bulletproof button pattern -->
<table cellpadding="0" cellspacing="0" role="presentation">
<tr>
  <td align="center" bgcolor="#18b81e"
      style="border-radius:10px; box-shadow:0 4px 16px rgba(24,184,30,0.35);">
    <a href="{{CTA_URL}}"
       style="display:inline-block; padding:18px 44px;
              font-size:20px; font-weight:700; color:#ffffff;
              text-decoration:none; font-family:Arial Black,Arial,sans-serif;
              letter-spacing:0.3px;">
      Button Label Here
    </a>
  </td>
</tr>
</table>
```

**CTA Copywriting Rules:**
- Lead with a verb: "Claim", "Get", "Start", "Unlock", "Download"
- Include the value in the button when possible: "Claim Your $1000 Coupon"
- Never say "Click Here" or "Submit"
- Add urgency below the button (not inside it): "Offer expires 31st May, 2026"

---

## Phase 6 — Inline SVG Asset Generation

Use inline SVGs instead of external image files for all icons, illustrations, and decorative elements
(except the hero image, logo, and brand partner logos which may be external).

### SVG Asset Categories to Generate

**Icons** (32–44px viewBox): use `fill="none"` + `stroke` for line-style icons. Always include:
- A subtle fill layer (`fill="rgba(...,0.12)"` or `fill="#e8f0ff"`) for body
- Primary stroke (`stroke="#BRANDCOLOR" stroke-width="2–2.5"`)
- Decorative badge overlays (green check, number circles) where appropriate

**Step/Process Illustrations** (64–72px): richer than icons. Include:
- Shadow/depth layer (duplicate rect/path, offset 1–2px, low opacity)
- Filled body with brand-light color (`#e8f0ff`, `#dce8ff`)
- Detail lines, text labels where useful
- Completion badge (circle + checkmark) for "done" states

**Decorative Patterns** (header, section accents): circuit boards, geometric grids, dot matrices:
```svg
<!-- Circuit board pattern example -->
<svg width="180" height="60" viewBox="0 0 180 60" fill="none">
  <line x1="10" y1="20" x2="80" y2="20" stroke="rgba(100,170,255,0.3)" stroke-width="1.2"/>
  <circle cx="10" cy="20" r="3" fill="rgba(100,180,255,0.5)"/>
  <circle cx="80" cy="20" r="3.5" fill="rgba(100,180,255,0.6)"/>
  <rect x="76" y="16" width="8" height="8" rx="1.5" fill="none" stroke="rgba(100,180,255,0.4)" stroke-width="1.2"/>
  <!-- add more traces, nodes, pads... -->
</svg>
```

**Brand Logos as SVG Text** (for copier/printer brands, software logos where brand fonts are well-known):
```svg
<svg width="72" height="28" viewBox="0 0 72 28" fill="none">
  <text x="4" y="22" font-family="Arial Black,Arial,sans-serif" font-size="22"
        font-weight="900" fill="#cc0000">Canon</text>
</svg>
```

### SVG-in-Email Rules
- Always include `xmlns="http://www.w3.org/2000/svg"` on the `<svg>` tag
- Wrap SVGs in a `<table cellpadding="0" cellspacing="0" role="presentation">` cell
- Set explicit `width` and `height` attributes on the `<svg>` tag
- Use `fill` and `stroke` with hex or rgba — no CSS variables in email SVGs
- Do not use `<use>`, `<symbol>`, CSS filters, or `currentColor` in email SVGs
- Avoid SVGs wider than 580px inline; for full-width graphics, use a background-color section instead

---

## Phase 7 — Cross-Client Compatibility Checklist

Apply these before finalising every email:

### Outlook (MSO) Fixes
```html
<!-- Outlook-safe image sizing -->
<img width="620" style="width:100%; max-width:620px;" ...>

<!-- Outlook button fallback (VML) — add inside <td> for critical CTAs -->
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{{URL}}"
  style="height:54px; v-text-anchor:middle; width:200px;" arcsize="18%"
  stroke="f" fillcolor="#18b81e">
  <w:anchorlock/>
  <center style="color:#ffffff; font-family:Arial,sans-serif; font-size:20px; font-weight:700;">
    Button Label
  </center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-- -->
  <!-- regular HTML button here -->
<!--<![endif]-->
```

### Gmail Clipping
Gmail clips emails over ~102KB. If the email is large:
- Minify inline CSS (remove extra spaces)
- Compress SVG paths
- Remove HTML comments (except MSO conditionals) before final output

### Dark Mode Considerations
```css
/* In <style> block */
@media (prefers-color-scheme: dark) {
  .dm-invert { filter: invert(1); }
  .dm-bg     { background-color: #1a1a2e !important; }
}
```
Use sparingly — test before deploying.

### Image Blocking
Every `<img>` needs:
- `alt=""` attribute (blank for decorative, descriptive for content)
- Inline `width` and `height`
- The surrounding `<td>` should have a `bgcolor` fallback so the layout doesn't collapse

---

## Phase 8 — Content Sections Reference

Read `references/sections.md` for copy templates, HTML patterns, and design notes for each standard
email section type (header, hero, coupon, steps, info bar, brand rail, footer). Use those patterns
as starting points and customise to the brand.

---

## Phase 9 — Final Output Format

### File output
Always save as a `.html` file to `/mnt/user-data/outputs/`. Name it descriptively:
`{brand}_{type}_email.html` e.g. `acme_promo_email.html`.

### HTML structure order
```
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- meta tags -->
  <!-- preheader div -->
  <!-- <style> with resets + @media -->
</head>
<body>
  <!-- canvas table (full width, bg color) -->
    <!-- wrapper table (620px) -->
      <!-- header row -->
      <!-- hero text row -->
      <!-- offer/coupon row -->
      <!-- CTA row -->
      <!-- hero image row (if applicable) -->
      <!-- blue/dark info section row -->
        <!-- steps cards -->
        <!-- info bar -->
        <!-- brand rail -->
      <!-- footer row -->
    <!-- /wrapper -->
  <!-- /canvas -->
</body>
</html>
```

### Inline comments
Comment each major section clearly:
```html
<!-- ════ HEADER ════ -->
<!-- ════ HERO TEXT ════ -->
<!-- ════ COUPON BOX ════ -->
```

### Marketing summary comment block
Add at the top of `<body>`:
```html
<!--
  MARKETING ANALYSIS
  Goal:         [primary conversion goal]
  Audience:     [B2B/B2C, segment]
  Stage:        [funnel stage]
  Primary CTA:  [button text → URL]
  Preheader:    [preheader text]
  Offer:        [offer details + expiry]
  Trust signals:[list]
-->
```

---

## Quick Reference — Common Mistakes to Avoid

| ❌ Wrong | ✅ Right |
|---|---|
| CSS `display:flex` for layout | `<table>` for all layout |
| `<link>` to Google Fonts | web-safe font stacks only |
| `class=` for colours/spacing | `style=""` inline on every element |
| `<button>` element for CTA | `<a>` inside `<td bgcolor>` |
| External SVG files | Inline `<svg>` in the HTML |
| `border-radius` on `<table>` without `overflow:hidden` on parent | always pair them |
| Fixed `px` widths on `<img>` without `max-width:100%` | always set both |
| Single CTA deep in the email | CTA above fold + repeat after key offer block |
| Vague CTA copy ("Learn More") | Value-explicit copy ("Claim Your $1000 Coupon") |
| Images without `alt` text | always add `alt=""` minimum |
