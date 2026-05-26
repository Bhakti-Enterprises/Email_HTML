# Email Marketing Strategy Reference

Deep-dive guidance on strategy decisions for different email types. Read the relevant section
based on the email's goal before designing.

---

## Table of Contents
1. [Funnel Stage → Design Rules](#1-funnel-stage--design-rules)
2. [B2B vs B2C Design Differences](#2-b2b-vs-b2c-design-differences)
3. [Offer Types & How to Present Them](#3-offer-types--how-to-present-them)
4. [CTA Psychology](#4-cta-psychology)
5. [Colour Psychology Quick Reference](#5-colour-psychology-quick-reference)
6. [Subject Line + Preheader Formulas](#6-subject-line--preheader-formulas)
7. [Email Type Blueprints](#7-email-type-blueprints)

---

## 1. Funnel Stage → Design Rules

### Awareness Stage
- Goal: brand recall + curiosity
- Sections: Header → Hero (brand story) → 2–3 benefit highlights → Soft CTA ("Learn More")
- Tone: educational, not salesy
- Trust signals: social proof numbers ("10,000+ businesses trust us")
- NO hard sell, NO prices, NO countdown timers

### Consideration Stage
- Goal: prove value over alternatives
- Sections: Header → Problem statement → Solution (product/service) → Social proof → CTA
- Tone: consultative, confident
- Trust signals: testimonials, case studies, logos
- Include: comparison table or benefit list

### Decision Stage (Conversion)
- Goal: close the sale / claim the offer
- Sections: Header → Hero offer → Coupon/price → CTA (above fold) → How it works → Terms → CTA repeat → Footer
- Tone: direct, urgent but not desperate
- Trust signals: guarantee, secure badge, deadline
- CRITICAL: CTA appears at least twice; urgency note below every CTA

### Retention / Loyalty
- Goal: repeat purchase, upsell, referral
- Sections: Personalised greeting → Reward/exclusive benefit → New arrivals → Referral CTA
- Tone: warm, exclusive, "you're valued"
- Trust signals: "VIP member" / "loyal customer" framing

### Re-engagement / Win-back
- Goal: bring back lapsed users
- Sections: Bold headline ("We miss you") → Best offer → Easy single-step CTA → Unsubscribe option
- Tone: humble, no guilt, clear value
- Note: One very clear CTA only — win-back emails with multiple CTAs convert 30% worse

---

## 2. B2B vs B2C Design Differences

| Dimension | B2B | B2C |
|---|---|---|
| **Header height** | Compact (60–80px) | Can be taller (80–120px) |
| **Colour palette** | Navy, slate, corporate blue | Brand-specific, more playful |
| **Hero headline** | Business outcome ("Save $1000 per shipment") | Emotional/aspirational ("You deserve this") |
| **Social proof** | Company logos, case studies, ROI numbers | Star ratings, photos, testimonial quotes |
| **CTA tone** | "Request a Quote", "Claim Your Benefit" | "Shop Now", "Get Yours Today" |
| **Decision timeline** | Longer — educational content OK | Impulse-friendly — urgency works well |
| **Number formatting** | Always use $ amounts and % metrics | Benefits in plain English too |
| **Footer** | Company registration, VAT, GDPR note | Social links, unsubscribe |
| **Mobile priority** | Desktop often more important (desk workers) | Mobile-first (60–70% open on mobile) |

---

## 3. Offer Types & How to Present Them

### Percentage Discount
- Visual emphasis: large `%` digit in accent colour
- Add: original price struck through with `<s>` tag
- Below CTA: "Save {{AMOUNT}} on your next order"

### Fixed Dollar/Value Coupon
- Use the coupon box pattern (Section 4 in sections.md)
- Make code MEMORABLE and BRAND-RELEVANT
- Show value twice: in headline AND in value badge
- Terms below CTA in small grey text

### Free Shipping
- Hero image: logistics/delivery visual
- Headline: "Ship for Free" or "Your $X Shipping Credit"
- Minimum order clearly stated in info bar
- Truck or package icon reinforces the message

### Free Trial / Freemium
- Lead with 0-risk framing: "No credit card required"
- Steps section: shows simple 3-step path to value
- CTA: "Start Free" or "Try It Free"
- Social proof: "Join X,000 teams already using [product]"

### Bundle / Package Deal
- Product grid (Section 13) showing what's included
- "Total value: $X — Yours for $Y" in hero
- CTA: "Get the Bundle"

### Loyalty / Points Reward
- Personalise: "{{FIRST_NAME}}, you've earned 500 points"
- Show progress bar or points balance (CSS-only, no JS)
- CTA: "Redeem Now" with expiry date

---

## 4. CTA Psychology

### The 3-Second Rule
A reader decides whether to click within 3 seconds of seeing the email. The CTA must be:
1. **Visible** — no scrolling required on first open
2. **Obvious** — high contrast button, large enough to tap on mobile (min 44px tall)
3. **Valuable** — the label communicates the reward, not just the action

### Button Label Formula
```
[Verb] + [Your] + [Specific Value]
```
Examples:
- ✅ "Claim Your $1000 Coupon"
- ✅ "Get Your Free Month"
- ✅ "Unlock Your VIP Discount"
- ❌ "Click Here"
- ❌ "Submit"
- ❌ "Learn More" (vague — use "See How It Works" instead)

### Placement Rules
- **First CTA**: within the top 500px of the email (above fold on most phones)
- **Second CTA**: after the proof/how-it-works section (after desire is built)
- **Third CTA** (long emails only): in the footer

### Urgency Without Panic
Genuine urgency converts; manufactured urgency erodes trust.
- ✅ Use real deadlines: "Expires 31st May, 2026"
- ✅ Scarcity with proof: "Only 50 redemptions available"
- ❌ Fake countdown: "Offer ends in 02:14:33" (refreshes on reload)

---

## 5. Colour Psychology Quick Reference

| Colour | Psychology | Email uses |
|---|---|---|
| **Navy/Dark Blue** | Trust, professionalism, authority | Corporate headers, B2B brands |
| **Bright Blue** | Technology, clarity, reliability | SaaS, fintech, healthcare |
| **Green** | Go, approval, money, nature | CTA buttons, success states, eco brands |
| **Red** | Urgency, price, emotion | Sale price, deadline, scarcity banner |
| **Orange** | Energy, creativity, warmth | Signup CTAs, startup brands |
| **Gold/Yellow** | Premium, reward, attention | Star ratings, award badges, luxury |
| **White** | Clean, space, content focus | Card backgrounds, text contrast |
| **Dark Navy (footer)** | Anchor, stability | Footer sections, closing trust |

---

## 6. Subject Line + Preheader Formulas

### High-converting subject line formulas
| Formula | Example |
|---|---|
| Benefit + Specificity | "Your $1000 shipping credit is ready" |
| Personalisation | "{{Name}}, this offer has your name on it" |
| Curiosity gap | "We saved something special for you" |
| Number-led | "3 things changing how you ship in 2026" |
| Question | "Have you claimed your B2B discount yet?" |
| Urgency | "Last 48 hours: exclusive B2B offer inside" |
| Social proof | "10,000 businesses can't be wrong — here's why" |

### Preheader formula
`[Extend subject] + [add detail] + [reinforce CTA]`

Subject: "Your $1000 shipping credit is ready"
Preheader: "Use code BE1000SHIP at checkout — minimum order $25k, expires 31 May"

---

## 7. Email Type Blueprints

### Welcome Email
1. Header
2. Hero: "Welcome to {{Brand}}" + warm subhead
3. What to expect (3-col benefit icons)
4. CTA: "Explore the Dashboard" / "Start Shopping"
5. Social links
6. Footer

### Promotional / Coupon Email
1. Header
2. Hero text: offer announcement
3. Coupon box
4. CTA (primary)
5. Hero image
6. How it works (3 steps)
7. Info bar (terms)
8. Brand rail
9. CTA (secondary, after proof)
10. Benefit icons
11. Contact + copyright

### Abandoned Cart
1. Header
2. Hero: "You left something behind"
3. Product grid (items in cart)
4. CTA: "Complete My Order"
5. Urgency: low-stock or cart-expiry note
6. Testimonial
7. Footer

### Newsletter
1. Header
2. Featured story (large image + headline + excerpt + "Read More")
3. 2–3 secondary stories (product grid style)
4. Tip/insight block
5. CTA: to latest content
6. Footer with social links

### Re-engagement
1. Header
2. Bold hero: "We've missed you, {{Name}}"
3. Best offer (coupon or upgrade)
4. Single CTA: "Come Back"
5. Unsubscribe option (reduce complaints)
6. Footer
