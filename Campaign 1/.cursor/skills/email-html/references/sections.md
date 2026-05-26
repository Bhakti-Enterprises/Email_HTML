# Email Sections Reference

Copy-ready HTML patterns for each standard email section. Customise brand colours, fonts, and copy.
All patterns assume the wrapper is 620px wide.

---

## Table of Contents
1. [Header](#1-header)
2. [Preheader / Preview Text](#2-preheader--preview-text)
3. [Hero Text Block](#3-hero-text-block)
4. [Coupon / Offer Box](#4-coupon--offer-box)
5. [CTA Button Row](#5-cta-button-row)
6. [Hero Image Row](#6-hero-image-row)
7. [Process Steps (3-col)](#7-process-steps-3-col)
8. [Info Bar (3-col terms)](#8-info-bar-3-col-terms)
9. [Brand / Partner Rail](#9-brand--partner-rail)
10. [Benefit Icons Footer](#10-benefit-icons-footer)
11. [Contact + Copyright Footer](#11-contact--copyright-footer)
12. [Social Proof / Testimonial Block](#12-social-proof--testimonial-block)
13. [Product Grid (2-col)](#13-product-grid-2-col)
14. [Countdown Urgency Banner](#14-countdown-urgency-banner)

---

## 1. Header

Dark brand-coloured header with logo left, decorative element right.

```html
<!-- ════ HEADER ════ -->
<tr>
<td style="background:linear-gradient(135deg,#0a2d6e 0%,#0d3a8a 50%,#0a2d6e 100%);
           padding:22px 28px 22px 22px;">
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
  <tr>
    <!-- LOGO cell — replace with <img> tag or keep SVG text -->
    <td valign="middle" width="220">
      <!-- Option A: image logo -->
      <img src="{{LOGO_URL}}" width="160" alt="{{BRAND_NAME}}"
           style="width:160px; max-width:160px; display:block;">
      <!-- Option B: CSS text logo (fallback) -->
      <!--
      <span style="font-size:22px; font-weight:900; color:#ffffff;
                   font-family:Arial Black,Arial,sans-serif;">{{BRAND}}</span>
      <div style="font-size:9px; color:#a0c4ff; letter-spacing:0.5px; margin-top:3px;">
        {{TAGLINE}}
      </div>
      -->
    </td>

    <!-- Decorative right side — circuit pattern or brand visual -->
    <td align="right" valign="middle">
      <svg width="160" height="60" viewBox="0 0 160 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <line x1="10" y1="15" x2="70" y2="15" stroke="rgba(100,170,255,0.25)" stroke-width="1.2"/>
        <line x1="20" y1="30" x2="90" y2="30" stroke="rgba(100,170,255,0.3)" stroke-width="1.2"/>
        <line x1="5"  y1="45" x2="65" y2="45" stroke="rgba(100,170,255,0.2)" stroke-width="1.2"/>
        <line x1="80" y1="10" x2="155" y2="10" stroke="rgba(100,170,255,0.2)" stroke-width="1"/>
        <line x1="100" y1="50" x2="155" y2="50" stroke="rgba(100,170,255,0.25)" stroke-width="1"/>
        <line x1="70" y1="15" x2="70" y2="30" stroke="rgba(100,170,255,0.25)" stroke-width="1.2"/>
        <line x1="90" y1="30" x2="90" y2="10" stroke="rgba(100,170,255,0.2)" stroke-width="1"/>
        <line x1="120" y1="10" x2="120" y2="50" stroke="rgba(100,170,255,0.18)" stroke-width="1"/>
        <circle cx="10"  cy="15" r="3"   fill="rgba(100,180,255,0.5)"/>
        <circle cx="70"  cy="15" r="3.5" fill="rgba(100,180,255,0.6)"/>
        <circle cx="90"  cy="10" r="3"   fill="rgba(100,180,255,0.55)"/>
        <circle cx="120" cy="50" r="2.5" fill="rgba(100,180,255,0.4)"/>
        <circle cx="155" cy="10" r="3"   fill="rgba(100,180,255,0.5)"/>
        <rect x="86" y="26" width="8" height="8" rx="1.5" fill="none" stroke="rgba(100,180,255,0.45)" stroke-width="1.2"/>
      </svg>
    </td>
  </tr>
  </table>
</td>
</tr>
```

**Strategy note:** Header confirms brand identity in under 1 second. Keep it under 80px tall.
The decorative element adds premium feel without image load dependency.

---

## 2. Preheader / Preview Text

Invisible text shown in inbox preview (after subject line). Always include.

```html
<!-- PREHEADER — shows in inbox preview, invisible in email body -->
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; color:#ffffff;">
  {{PREHEADER_TEXT}} &#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;
</div>
```

**Preheader copywriting:**
- 50–90 characters (preview truncates at 90 on most clients)
- Extends or adds to subject line — never repeats it
- Include the key benefit or urgency signal
- The `&#8203;&nbsp;` invisible padding stops inbox clients pulling in body text after the preheader

**Example:**
- Subject: "Your exclusive B2B offer is ready"
- Preheader: "Use code BE1000SHIP to claim $1000 in free shipping on orders $25k+"

---

## 3. Hero Text Block

Headline + subhead. First content the reader sees. Must communicate the core offer in isolation.

```html
<!-- ════ HERO TEXT ════ -->
<tr>
<td align="center" class="mob-pad" style="padding:36px 40px 8px 40px; background:#ffffff;">

  <!-- Eyebrow / label (optional) -->
  <div style="font-size:13px; font-weight:700; color:#1a73e8; letter-spacing:1.5px;
              text-transform:uppercase; font-family:Arial,sans-serif; margin-bottom:10px;">
    {{EYEBROW_LABEL}}
  </div>

  <!-- H1 -->
  <div class="mob-h1"
       style="font-size:36px; line-height:44px; font-weight:800; color:#0d2d6e;
              font-family:Arial Black,Arial,sans-serif;">
    {{HEADLINE}}
  </div>

  <!-- Subhead -->
  <div class="mob-body"
       style="font-size:18px; line-height:28px; color:#1a3060; margin-top:12px; font-weight:600;
              font-family:Arial,sans-serif;">
    {{SUBHEADLINE}}
  </div>

  <!-- Body line with accent -->
  <div class="mob-body"
       style="font-size:24px; line-height:34px; color:#0d1f45; margin-top:14px; font-weight:600;
              font-family:Arial,sans-serif;">
    {{BODY_LINE_1}}
    <span style="color:#e00000; font-weight:800;">{{OFFER_HIGHLIGHT}}</span>
    {{BODY_LINE_2}}
  </div>

</td>
</tr>
```

**Strategy notes:**
- **Headline** = the transformation or reward ("Thank You — Your $1000 Benefit is Ready")
- **Subhead** = who this is for + why now ("Exclusive B2B offer, expires 31st May")
- **Accent colour** on the price/offer number makes it scannable at 2 seconds
- Keep headline under 8 words for mobile

---

## 4. Coupon / Offer Box

Visually distinct offer presentation with scissor hint, dashed border, and value badge.

```html
<!-- ════ COUPON BOX ════ -->
<tr>
<td align="center" class="mob-pad" style="padding:20px 40px 10px 40px; background:#ffffff;">

  <table cellpadding="0" cellspacing="0" role="presentation"
         style="width:100%; max-width:400px; border-radius:16px; overflow:hidden;
                box-shadow:0 4px 20px rgba(10,68,184,0.18); border:2px solid #c8d8f5;">

    <!-- Header bar -->
    <tr>
      <td align="center"
          style="background:linear-gradient(90deg,#0835a0,#0a44b8,#0835a0);
                 color:#ffffff; font-size:13px; font-weight:700; letter-spacing:1.5px;
                 padding:14px 10px; font-family:Arial,sans-serif;">
        ★ YOUR EXCLUSIVE COUPON CODE ★
      </td>
    </tr>

    <!-- Code area -->
    <tr>
      <td align="center"
          style="background:#f5f9ff; padding:24px 20px 20px 20px;
                 border:2.5px dashed #3a6ad4; border-top:none;">

        <!-- Scissors hint -->
        <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 10px auto;">
        <tr><td>
          <svg width="32" height="20" viewBox="0 0 32 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="5" cy="5" r="4" fill="none" stroke="#0a44b8" stroke-width="1.8"/>
            <circle cx="5" cy="15" r="4" fill="none" stroke="#0a44b8" stroke-width="1.8"/>
            <line x1="8" y1="7"  x2="30" y2="19" stroke="#0a44b8" stroke-width="1.6" stroke-linecap="round"/>
            <line x1="8" y1="13" x2="30" y2="1"  stroke="#0a44b8" stroke-width="1.6" stroke-linecap="round"/>
          </svg>
        </td></tr>
        </table>

        <!-- Code -->
        <div class="mob-coupon"
             style="font-size:54px; font-weight:900; color:#0a2d7a; letter-spacing:3px;
                    line-height:1; font-family:Arial Black,Arial,sans-serif;
                    text-shadow:2px 2px 0 rgba(10,44,122,0.1);">
          {{COUPON_CODE}}
        </div>

        <!-- Value badge -->
        <table cellpadding="0" cellspacing="0" role="presentation" style="margin:14px auto 0 auto;">
        <tr>
          <td style="background:linear-gradient(135deg,#e8f0ff,#d0e2ff); border-radius:20px;
                     padding:6px 18px; border:1px solid #aac2f0;">
            <span style="font-size:13px; color:#0835a0; font-weight:700; font-family:Arial,sans-serif;
                         letter-spacing:0.5px;">
              {{COUPON_VALUE_LABEL}}
            </span>
          </td>
        </tr>
        </table>

      </td>
    </tr>

  </table>
</td>
</tr>
```

**Strategy notes:**
- Dashed border triggers the mental model of a physical coupon — high recall
- The code should be memorable and brand-reinforcing (e.g. `BRAND50OFF`, `WELCOME20`)
- Value badge below the code adds secondary confirmation of the offer
- Box shadow makes the coupon "lift" off the page — premium perception

---

## 5. CTA Button Row

Standalone row dedicated to the primary call-to-action.

```html
<!-- ════ CTA BUTTON ════ -->
<tr>
<td align="center" style="padding:18px 40px 28px 40px; background:#ffffff;">

  <table cellpadding="0" cellspacing="0" role="presentation">
  <tr>
    <td align="center" class="mob-cta"
        style="background:linear-gradient(135deg,#15a819,#18cc1e); border-radius:12px;
               box-shadow:0 4px 18px rgba(21,168,25,0.38);">
      <a href="{{CTA_URL}}"
         style="display:inline-block; padding:18px 46px; font-size:21px; font-weight:700;
                color:#ffffff; text-decoration:none; font-family:Arial Black,Arial,sans-serif;
                letter-spacing:0.3px;">
        {{CTA_LABEL}}
      </a>
    </td>
  </tr>
  </table>

  <!-- Urgency nudge below button -->
  <div style="font-size:12px; color:#888888; margin-top:10px; font-family:Arial,sans-serif;">
    {{URGENCY_NOTE}}
    <!-- e.g. "Offer expires 31st May, 2026 · Minimum order $25,000" -->
  </div>

</td>
</tr>
```

**Button colour guide by goal:**
| Goal | Colour | Why |
|---|---|---|
| Purchase / Claim | Green (`#18b81e`) | Go signal, money, positive |
| Download / Get | Blue (`#0a44b8`) | Trust, information |
| Register / Join | Orange (`#f57c00`) | Energy, social |
| Urgent / Last chance | Red (`#cc0000`) | Alarm, scarcity |

---

## 6. Hero Image Row

Full-width image between hero text and blue section. Keep aspect ratio 16:9 or wider.

```html
<!-- ════ HERO IMAGE ════ -->
<tr>
<td align="center" style="background:#ffffff; padding:0; line-height:0; font-size:0;">
  <img src="{{HERO_IMAGE_URL}}"
       width="620" alt="{{HERO_ALT_TEXT}}"
       style="width:100%; max-width:620px; display:block;">
</td>
</tr>
```

**If no hero image is available**, generate an inline SVG illustration instead:
```html
<tr>
<td style="background:linear-gradient(135deg,#f0f5ff,#e8edf8); padding:30px 40px; text-align:center;">
  <!-- SVG illustration of the product/service concept -->
  <svg width="560" height="200" viewBox="0 0 560 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- custom illustration SVG here -->
  </svg>
</td>
</tr>
```

---

## 7. Process Steps (3-col)

"How it works" or "what happens next" section. Max 3–4 steps.

```html
<!-- ════ PROCESS STEPS ════ -->
<tr>
<td style="background:#0a44b8; padding:30px 20px 28px 20px;">

  <!-- Section title with rule lines -->
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="margin-bottom:22px;">
  <tr>
    <td valign="middle" style="border-top:2px solid rgba(255,255,255,0.3);">&nbsp;</td>
    <td align="center" style="padding:0 14px; white-space:nowrap;">
      <span style="font-size:18px; font-weight:800; color:#ffffff; letter-spacing:0.5px;
                   font-family:Arial Black,Arial,sans-serif;">
        {{STEPS_TITLE}}
      </span>
    </td>
    <td valign="middle" style="border-top:2px solid rgba(255,255,255,0.3);">&nbsp;</td>
  </tr>
  </table>

  <!-- Step cards -->
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
  <tr valign="top">

    <!-- Repeat this <td> block for each step (2–4 steps) -->
    <td class="mob-stack" style="width:33%; padding:0 6px 0 0; vertical-align:top;">
      <table width="100%" cellpadding="0" cellspacing="0" role="presentation"
             style="background:#ffffff; border-radius:14px; box-shadow:0 4px 14px rgba(0,0,0,0.15);">
      <tr>
        <td align="center" style="padding:20px 12px 22px 12px;">

          <!-- Step number badge -->
          <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 16px auto;">
          <tr>
            <td align="center" valign="middle"
                style="width:40px; height:40px;
                       background:linear-gradient(135deg,#1355cc,#0a44b8);
                       border-radius:20px; color:#ffffff; font-size:20px; font-weight:900;
                       line-height:40px; font-family:Arial Black,Arial,sans-serif;
                       box-shadow:0 3px 10px rgba(10,68,184,0.4);">
              {{STEP_NUMBER}}
            </td>
          </tr>
          </table>

          <!-- Step icon (inline SVG 64–72px) -->
          <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 14px auto;">
          <tr><td>
            <!-- SVG ICON HERE -->
            {{STEP_ICON_SVG}}
          </td></tr>
          </table>

          <!-- Optional dashed arrow connector (omit on last step) -->
          <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 14px auto;">
          <tr><td align="center">
            <svg width="54" height="14" viewBox="0 0 54 14" fill="none" xmlns="http://www.w3.org/2000/svg">
              <line x1="2" y1="7" x2="44" y2="7" stroke="#0a44b8" stroke-width="2" stroke-dasharray="5 4" stroke-linecap="round"/>
              <polygon points="44,3 52,7 44,11" fill="#0a44b8"/>
            </svg>
          </td></tr>
          </table>

          <!-- Step copy -->
          <div style="font-size:13px; line-height:21px; color:#0d2d6e; font-weight:700;
                      text-align:center; font-family:Arial,sans-serif;">
            {{STEP_DESCRIPTION}}
          </div>

        </td>
      </tr>
      </table>
    </td>
    <!-- /step -->

  </tr>
  </table>
</td>
</tr>
```

---

## 8. Info Bar (3-col terms)

Conditions, validity, and applicability. Reduces post-purchase dissonance.

```html
<!-- ════ INFO BAR ════ -->
<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="margin-top:20px;">
<tr>
  <td bgcolor="#ffffff" style="border-radius:12px; padding:20px 10px;
      box-shadow:0 4px 14px rgba(0,0,0,0.1);">
    <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
    <tr>

      <!-- Info item — repeat 3× -->
      <td class="mob-stack" align="center" style="width:33%; padding:4px 10px; vertical-align:middle;">
        <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 10px auto;">
        <tr><td>
          {{INFO_ICON_SVG}} <!-- 38–44px icon SVG -->
        </td></tr>
        </table>
        <div style="font-size:13px; font-weight:700; color:#0d2d6e; line-height:20px;
                    text-align:center; font-family:Arial,sans-serif;">
          {{INFO_LABEL}}<br>{{INFO_VALUE}}
        </div>
      </td>

      <!-- Vertical divider (hide on mobile via mob-hide if needed) -->
      <td style="width:1px; background:#d4dff5; padding:0;">&nbsp;</td>

    </tr>
    </table>
  </td>
</tr>
</table>
```

---

## 9. Brand / Partner Rail

Compatible brands, integrations, or partner logos on a light strip.

```html
<!-- ════ BRAND RAIL ════ -->
<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="margin-top:20px;">
<tr>
  <td align="center" bgcolor="#0035a0"
      style="border-radius:10px 10px 0 0; padding:12px 16px;">
    <span style="font-size:12px; font-weight:700; color:#ffffff; letter-spacing:0.4px;
                 font-family:Arial,sans-serif; text-transform:uppercase;">
      {{RAIL_LABEL}}
    </span>
  </td>
</tr>
<tr>
  <td bgcolor="#ffffff" style="padding:16px 10px; border-radius:0 0 12px 12px;">
    <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
    <tr valign="middle">
      <!-- 4–6 brand logo cells -->
      <td class="brand-cell" align="center" style="padding:4px 6px;">
        {{BRAND_LOGO_SVG_OR_IMG}}
      </td>
    </tr>
    </table>
  </td>
</tr>
</table>
```

---

## 10. Benefit Icons Footer

Trust-building icon strip just above contact info. 4–5 items max.

```html
<!-- ════ BENEFIT ICONS ════ -->
<tr>
<td style="background:#002575; padding:26px 20px 18px 20px;">
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
  <tr>

    <!-- Benefit item — repeat 4–5× -->
    <td class="mob-stack" align="center" style="width:20%; padding:6px 4px; vertical-align:top;">
      <table cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto 10px auto;">
      <tr><td align="center">
        {{BENEFIT_ICON_SVG}} <!-- 40–44px, stroke="#ffffff" -->
      </td></tr>
      </table>
      <div style="font-size:11.5px; color:#ffffff; line-height:17px;
                  text-align:center; font-family:Arial,sans-serif;">
        {{BENEFIT_LABEL_LINE1}}<br>{{BENEFIT_LABEL_LINE2}}
      </div>
    </td>

  </tr>
  </table>
```

**Standard benefit icons to generate as inline SVG:**
- Shield + checkmark → "100% Genuine"
- People network → "B2B Network"
- Truck + map pin → "Fast Delivery"
- Headset → "Dedicated Support"
- Gear/cog → "Service & Spares"

---

## 11. Contact + Copyright Footer

```html
<!-- ════ CONTACT + COPYRIGHT ════ -->
  <!-- Thin divider -->
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="margin-top:20px;">
  <tr>
    <td style="border-top:1px solid rgba(255,255,255,0.2); padding-top:18px;">
      <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
      <tr>

        <!-- Phone -->
        <td valign="middle" style="padding-right:14px; padding-bottom:6px; white-space:nowrap;">
          <table cellpadding="0" cellspacing="0" role="presentation">
          <tr>
            <td valign="middle" style="padding-right:8px;">
              <!-- green phone icon SVG -->
              <svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="13" cy="13" r="12" fill="#18b81e"/>
                <path d="M8 7 C8 6.4 8.5 6 9 6 L11 6 C11.4 6 11.7 6.3 11.8 6.7 L12.7 10
                         C12.8 10.4 12.6 10.8 12.3 11 L11 11.8 C11.9 13.8 13.2 15.1 15.2 16 L16 14.7
                         C16.2 14.4 16.6 14.2 17 14.3 L20.3 15.2 C20.7 15.3 21 15.6 21 16
                         L21 18 C21 18.6 20.5 19 20 19 C13.5 19 8 13.5 8 7Z" fill="#ffffff"/>
              </svg>
            </td>
            <td valign="middle">
              <span style="font-size:13px; color:#ffffff; font-family:Arial,sans-serif;">
                {{CONTACT_PHONE_LABEL}} <strong>{{PHONE_NUMBER}}</strong>
              </span>
            </td>
          </tr>
          </table>
        </td>

        <!-- Email -->
        <td valign="middle" style="padding-bottom:6px; white-space:nowrap;">
          <table cellpadding="0" cellspacing="0" role="presentation">
          <tr>
            <td valign="middle" style="padding-right:8px;">
              <!-- envelope SVG -->
              <svg width="28" height="22" viewBox="0 0 28 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="1" y="1" width="26" height="20" rx="3.5" fill="#1453c8" stroke="#6690e8" stroke-width="1.4"/>
                <polyline points="1,1 14,12 27,1" stroke="#aac4ff" stroke-width="1.8" fill="none"/>
                <line x1="1" y1="21" x2="10" y2="13" stroke="#7aabf8" stroke-width="1.2" opacity="0.6"/>
                <line x1="27" y1="21" x2="18" y2="13" stroke="#7aabf8" stroke-width="1.2" opacity="0.6"/>
              </svg>
            </td>
            <td valign="middle">
              <span style="font-size:13px; color:#ffffff; font-family:Arial,sans-serif;">
                {{EMAIL_ADDRESS}}
              </span>
            </td>
          </tr>
          </table>
        </td>

      </tr>
      </table>
    </td>
  </tr>
  </table>

  <!-- Copyright -->
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="margin-top:14px;">
  <tr>
    <td align="center" style="font-size:12px; color:#7a9fd4; font-family:Arial,sans-serif;">
      &copy; {{YEAR}} {{BRAND_NAME}}. All rights reserved.
      <!-- Optional: unsubscribe link -->
      &nbsp;&middot;&nbsp;
      <a href="{{UNSUBSCRIBE_URL}}" style="color:#7a9fd4; text-decoration:underline;">Unsubscribe</a>
    </td>
  </tr>
  </table>

</td>
</tr>
```

---

## 12. Social Proof / Testimonial Block

For B2C or consideration-stage emails.

```html
<!-- ════ TESTIMONIAL ════ -->
<tr>
<td style="background:#f8faff; padding:28px 30px;">
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
  <tr valign="top">

    <td class="mob-stack" style="width:50%; padding:0 12px 0 0; vertical-align:top;">
      <!-- star rating SVG -->
      <div style="font-size:0; line-height:0; margin-bottom:10px;">
        <!-- 5 stars, repeat for each -->
        <svg style="display:inline-block;" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <polygon points="9,1 11,6.5 17,6.5 12.5,10 14.5,16 9,12.5 3.5,16 5.5,10 1,6.5 7,6.5" fill="#f5a623"/>
        </svg>
        <!-- ×5 for 5 stars -->
      </div>
      <div style="font-size:15px; line-height:24px; color:#1a2f5a; font-style:italic;
                  font-family:Arial,sans-serif; margin-bottom:10px;">
        "{{TESTIMONIAL_QUOTE}}"
      </div>
      <div style="font-size:12px; color:#6680a0; font-family:Arial,sans-serif; font-weight:700;">
        — {{REVIEWER_NAME}}, {{REVIEWER_TITLE}}
      </div>
    </td>

    <td class="mob-stack" style="width:50%; padding:0 0 0 12px; vertical-align:top;">
      <!-- second testimonial -->
    </td>

  </tr>
  </table>
</td>
</tr>
```

---

## 13. Product Grid (2-col)

For product announcement or catalogue emails.

```html
<!-- ════ PRODUCT GRID ════ -->
<tr>
<td class="mob-pad" style="padding:24px 20px; background:#ffffff;">
  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
  <tr valign="top">

    <!-- Product card — repeat 2× per row -->
    <td class="mob-stack" style="width:48%; padding:0 8px 0 0; vertical-align:top;">
      <table width="100%" cellpadding="0" cellspacing="0" role="presentation"
             style="border:1.5px solid #e0e8f5; border-radius:10px; overflow:hidden;">
        <!-- Product image -->
        <tr>
          <td style="padding:0; line-height:0; font-size:0;" bgcolor="#f0f5ff">
            <img src="{{PRODUCT_IMG}}" width="280" alt="{{PRODUCT_NAME}}"
                 style="width:100%; display:block;">
          </td>
        </tr>
        <!-- Product info -->
        <tr>
          <td style="padding:14px 16px 16px 16px;">
            <div style="font-size:15px; font-weight:700; color:#0d2d6e;
                        font-family:Arial Black,Arial,sans-serif; margin-bottom:6px;">
              {{PRODUCT_NAME}}
            </div>
            <div style="font-size:13px; color:#4a6080; font-family:Arial,sans-serif;
                        line-height:20px; margin-bottom:10px;">
              {{PRODUCT_DESC}}
            </div>
            <div style="font-size:18px; font-weight:900; color:#e00000;
                        font-family:Arial Black,Arial,sans-serif;">
              {{PRODUCT_PRICE}}
            </div>
          </td>
        </tr>
      </table>
    </td>

  </tr>
  </table>
</td>
</tr>
```

---

## 14. Countdown Urgency Banner

For flash sales and limited-time offers. Use sparingly — overuse kills credibility.

```html
<!-- ════ URGENCY BANNER ════ -->
<tr>
<td align="center"
    style="background:linear-gradient(90deg,#cc0000,#e30000,#cc0000);
           padding:14px 20px;">
  <table cellpadding="0" cellspacing="0" role="presentation">
  <tr valign="middle">

    <!-- clock icon -->
    <td valign="middle" style="padding-right:10px;">
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="14" cy="14" r="12" fill="none" stroke="#ffffff" stroke-width="2"/>
        <line x1="14" y1="7"  x2="14" y2="14" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="14" y1="14" x2="19" y2="18" stroke="#ffffff" stroke-width="2"   stroke-linecap="round"/>
        <circle cx="14" cy="14" r="2" fill="#ffffff"/>
      </svg>
    </td>

    <td valign="middle">
      <span style="font-size:16px; font-weight:700; color:#ffffff;
                   font-family:Arial Black,Arial,sans-serif; letter-spacing:0.3px;">
        {{URGENCY_MESSAGE}}
        <!-- e.g. "⚡ Offer ends in 3 days — 31st May, 2026" -->
      </span>
    </td>

  </tr>
  </table>
</td>
</tr>
```

---

## Template Variables Reference

All `{{PLACEHOLDER}}` values used across sections:

| Variable | Description |
|---|---|
| `{{BRAND_NAME}}` | Company name |
| `{{LOGO_URL}}` | Absolute URL to logo image |
| `{{TAGLINE}}` | Brand tagline |
| `{{PREHEADER_TEXT}}` | 50–90 char inbox preview text |
| `{{HEADLINE}}` | H1 hero headline |
| `{{SUBHEADLINE}}` | Supporting subhead |
| `{{OFFER_HIGHLIGHT}}` | Offer value in accent colour (e.g. "$1000 Coupon") |
| `{{COUPON_CODE}}` | Coupon string (e.g. `SHIP1000`) |
| `{{COUPON_VALUE_LABEL}}` | Badge text (e.g. "VALUED AT $1,000 SHIPPING CREDIT") |
| `{{CTA_URL}}` | Primary button URL |
| `{{CTA_LABEL}}` | Button copy (verb-first) |
| `{{URGENCY_NOTE}}` | Small text under button |
| `{{HERO_IMAGE_URL}}` | Hero image absolute URL |
| `{{STEPS_TITLE}}` | "HOW IT WORKS" section heading |
| `{{STEP_NUMBER}}` | 1, 2, 3 … |
| `{{STEP_DESCRIPTION}}` | 1–2 sentence step explanation |
| `{{RAIL_LABEL}}` | "COMPATIBLE WITH …" |
| `{{CONTACT_PHONE_LABEL}}` | "Need Help?" prefix |
| `{{PHONE_NUMBER}}` | Formatted phone number |
| `{{EMAIL_ADDRESS}}` | Support email |
| `{{YEAR}}` | Copyright year |
| `{{UNSUBSCRIBE_URL}}` | Unsubscribe link |
