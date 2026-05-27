## Learned User Preferences

- Use `/caveman` (full) for terse responses on routine ops (e.g. restarting preview servers) until the user says "stop caveman" or "normal mode".
- Apply Karpathy-style discipline on email work: surgical edits only, match existing patterns, no speculative features beyond the request.
- Before building or auditing email HTML, read `.cursor/skills/email-html/references/marketing-strategy.md` for funnel stage, B2B/B2C, offer type, and email-type blueprint.
- After a strategy audit, give a concrete add/remove list; implement in the template when the user says to apply changes (e.g. "do the changes").
- Use DOM-path or element-targeted edits for precise visual tweaks in templates (header bgcolor, borders, padding).
- When comparing templates locally, serve both on fixed ports: template1 on 8080, template2 on 8081; kill duplicate listeners on those ports before restarting.
- Persist browser-preview CSS change payloads to `template1.html` inline styles, matching existing table patterns.
- For email icons and small graphics, prefer PNG from Canva (transparent background, ~2× display size) over SVG or WebP.

## Learned Workspace Facts

- Workspace folder `Campaign 1` is a Bhakti Enterprises B2B email campaign; primary template is `template1.html` (promotional coupon, code `BE1000SHIP`, $1000 shipping credit).
- Reference/compare template lives at `template2/pixel-perfect-templates/public/email-template.html` — there is no `template2.html` at repo root.
- Email authoring skill: `.cursor/skills/email-html/` with `references/marketing-strategy.md` and `references/sections.md`.
- Local preview: `python -m http.server 8080` from `Campaign 1` root (`template1.html` + `assets/`); port 8081 from `template2/pixel-perfect-templates/public/` (`email-template.html`).
- Template2 references `./email-assets/` for images; that folder is often missing, so images break until assets are added.
- Campaign icons and step graphics live under `assets/icons/`; resize PNGs to match `<img>` display size (~64–128px) before production — avoid 1500×1500 sources; host on CDN/ESP.
- `template1.html` follows B2B decision-stage promotional/coupon blueprint: dual CTAs, coupon value in headline and badge, urgency under CTAs, footer `{{COMPANY_ADDRESS}}` and `{{UNSUBSCRIBE_URL}}`.
- Settled header styling in `template1.html`: white background `#ffffff`, bottom border `1px solid #e2e6ee` (not solid brand-blue or grey `#f3f5f9` header).
- `template1.html` typography uses Segoe UI / Helvetica Neue with hierarchy classes (`type-h1`, `type-lead`, `type-cta`, etc.).
- Brand rail in `template1.html`: white rounded card, centered `#003fa5` tab (bottom corners only), six placeholder logo cells for user-supplied brand images.
