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
- For image-based section swaps (flow, footer trust, header logo), default to `template2.html` only unless the user asks to update `template1.html` too.

## Learned Workspace Facts

- Workspace folder `Campaign 1` is a Bhakti Enterprises B2B email campaign; primary template is `template1.html` (promotional coupon, example code `BE1000SHIP`, $1000 shipping credit, min order $10,000; urgency copy uses "Coupon expires" not "Offer expires").
- Active templates at repo root: `template1.html` (primary; HTML step cards, 4-column footer trust, remote header logo) and `template2.html` (variant; `assets/logo.png`, `assets/sections/flow2.png`, `assets/sections/trust.png`). Legacy compare template: `template2/pixel-perfect-templates/public/email-template.html` (uses `./email-assets/`, often missing).
- Email authoring skill: `.cursor/skills/email-html/` with `references/marketing-strategy.md` and `references/sections.md`.
- Local preview: `python -m http.server 8080` from `Campaign 1` root (`template1.html`, `template2.html`, `assets/`); port 8081 from `template2/pixel-perfect-templates/public/` (`email-template.html`).
- Info bar (both templates): inner `.info-cols` with `table-layout:fixed` and `.info-cell` as `display:table-cell` at 33% so three columns stay in one row on mobile — do not stack with `display:block` on info cells.
- Campaign icons and step graphics live under `assets/icons/`; resize PNGs to match `<img>` display size (~64–128px) before production — avoid 1500×1500 sources; host on CDN/ESP.
- `template1.html` merge tags: `{{COUPON_CODE}}`, `{{COUPON_EXPIRY_DATE}}`, `{{COMPANY_ADDRESS}}`, `{{UNSUBSCRIBE_URL}}`; both CTAs use WhatsApp `wa.me/919820229230` with a pre-filled message including `{{COUPON_CODE}}`.
- `template1.html` follows B2B decision-stage promotional/coupon blueprint: dual CTAs, coupon value in headline and badge, urgency under CTAs, footer trust row is four 25% columns (no fifth item); coupon headline and badge accent `#18b81e`.
- Settled `template1.html` blocks: white header `#ffffff` + bottom border `1px solid #e2e6ee`; info bar `#eef5ff` / `#103060` / `#d0dff0` dividers; Segoe UI type classes; brand rail centered via `.brands-row` / `.brands-center` / scoped `.brand-td`; tab "LEADING COPIER & PRINTER BRANDS"; four logos, `.brand-logo` 96×28px; footer contact "Need Help? Contact Us:" + `+91 98202 29230`.
- Production campaign images (steps, arrows, footer icons) are hosted on Supabase public storage (`keytpzeojnqdtaojmqik.supabase.co/storage/v1/object/public/Campaign/`).
- Gmail wide-pane fixes in `template1.html`: 50% | 620px | 50% `.center-gutter` shim for horizontal centering; `.img-lock-*` + fixed-width icon `<td>`s to prevent image stretch.
