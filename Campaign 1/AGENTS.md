## Learned User Preferences

- Use `/caveman` (full) for terse responses on routine ops (e.g. restarting preview servers) until the user says "stop caveman" or "normal mode".
- Apply Karpathy-style discipline on email work: surgical edits only, match existing patterns, no speculative features beyond the request.
- Before building or auditing email HTML, read `.cursor/skills/email-html/references/marketing-strategy.md` for funnel stage, B2B/B2C, offer type, and email-type blueprint.
- After a strategy audit, give a concrete add/remove list; implement in the template when the user says to apply changes (e.g. "do the changes").
- Use DOM-path or element-targeted edits for precise visual tweaks in templates (header bgcolor, borders, padding).
- When comparing templates locally, serve both on fixed ports: template1 on 8080, template2 on 8081; kill duplicate listeners on those ports before restarting.
- Persist browser-preview CSS change payloads to `template1.html` inline styles, matching existing table patterns.
- For email icons and small graphics, prefer PNG from Canva (transparent background, ~2× display size) over SVG or WebP.
- When optimizing `assets/` for size only, use lossless compression (e.g. oxipng for PNG, jpegtran for JPEG) so preview appearance stays unchanged — no resize or re-quantize unless asked.

## Learned Workspace Facts

- Workspace folder `Campaign 1` is a Bhakti Enterprises B2B email campaign; primary template is `template1.html` (promotional coupon, example code `BE1000SHIP`, $1000 shipping credit, min order $10,000; urgency copy uses "Coupon expires" not "Offer expires").
- Reference/compare template lives at `template2/pixel-perfect-templates/public/email-template.html` — there is no `template2.html` at repo root.
- Email authoring skill: `.cursor/skills/email-html/` with `references/marketing-strategy.md` and `references/sections.md`.
- Local preview: `python -m http.server 8080` from `Campaign 1` root (`template1.html` + `assets/`); port 8081 from `template2/pixel-perfect-templates/public/` (`email-template.html`).
- Template2 references `./email-assets/` for images; that folder is often missing, so images break until assets are added.
- Campaign icons and step graphics live under `assets/icons/`; resize PNGs to match `<img>` display size (~64–128px) before production — avoid 1500×1500 sources; host on CDN/ESP.
- `template1.html` merge tags: `{{COUPON_CODE}}`, `{{COUPON_EXPIRY_DATE}}`, `{{COMPANY_ADDRESS}}`, `{{UNSUBSCRIBE_URL}}`; both CTAs use WhatsApp `wa.me/919820229230` with a pre-filled message including `{{COUPON_CODE}}`.
- `template1.html` follows B2B decision-stage promotional/coupon blueprint: dual CTAs, coupon value in headline and badge, urgency under CTAs, footer trust row is four 25% columns (no fifth item); coupon headline and badge accent `#18b81e`.
- Settled header styling in `template1.html`: white background `#ffffff`, bottom border `1px solid #e2e6ee` (not solid brand-blue or grey `#f3f5f9` header).
- `template1.html` typography uses Segoe UI / Helvetica Neue with hierarchy classes (`type-h1`, `type-lead`, `type-cta`, etc.).
- Brand rail in `template1.html`: white rounded card, centered `#003fa5` tab (bottom corners only), tab copy "LEADING COPIER & PRINTER BRANDS"; four logos (HP, Canon, Epson, Kyocera) in a centered row with equal gutters; HP uses `assets/brands/hp.png`, others from `bhaktienterprises.co.in/home/we-deals-in/`; `.brand-logo` capped at 96×28px.
- Settled `template1.html` blocks: info bar `#eef5ff` background, `#103060` text, `#d0dff0` column dividers; footer contact line "Need Help? Contact Us:" + `+91 98202 29230`.
- Production campaign images (steps, arrows, footer icons) are hosted on Supabase public storage (`keytpzeojnqdtaojmqik.supabase.co/storage/v1/object/public/Campaign/`).
- Gmail wide-pane fixes in `template1.html`: 50% | 620px | 50% `.center-gutter` shim for horizontal centering; `.img-lock-*` + fixed-width icon `<td>`s to prevent image stretch.
