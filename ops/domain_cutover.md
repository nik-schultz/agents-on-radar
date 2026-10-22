# Domain cutover: github.io → botsdothat.com

**Status (Oct 21, 2026, 11:13 PM CT):**
- botsdothat.com is not registered yet. Nik is buying it himself at IONOS. We buy nothing.
- The site stays at https://nik-schultz.github.io/agents-on-radar/ with `cname` empty and `base_url` unchanged, so nothing breaks before DNS is ready.
- The DNS values below were checked against GitHub's docs on Oct 21, 2026:
  - "Managing a custom domain for your GitHub Pages site"
  - "Verifying your custom domain for GitHub Pages"

## 1. IONOS DNS records (Domains & SSL → botsdothat.com → DNS)

First delete any default records IONOS creates for `@` and `www` (parking-page A/AAAA/CNAME records). GitHub's docs say to remove default records. Don't add a wildcard (`*`) record; GitHub warns that wildcards allow takeovers.

| Type | Host / Name | Points to / Value | TTL |
|---|---|---|---|
| A | @ | 185.199.108.153 | 1 hour (default) |
| A | @ | 185.199.109.153 | 1 hour |
| A | @ | 185.199.110.153 | 1 hour |
| A | @ | 185.199.111.153 | 1 hour |
| AAAA | @ | 2606:50c0:8000::153 | 1 hour |
| AAAA | @ | 2606:50c0:8001::153 | 1 hour |
| AAAA | @ | 2606:50c0:8002::153 | 1 hour |
| AAAA | @ | 2606:50c0:8003::153 | 1 hour |
| CNAME | www | nik-schultz.github.io | 1 hour |
| TXT | _github-pages-challenge-nik-schultz | *(code GitHub shows in step 2)* | 1 hour |

Notes:
- The `www` CNAME points to `nik-schultz.github.io` with **no repo name** and no `*.pages.github.io` value.
- Once both apex and www are set up, GitHub redirects www.botsdothat.com to botsdothat.com automatically.
- The AAAA records are optional (IPv6). GitHub recommends keeping the A records alongside them.
- DNS changes can take up to 24 hours. They're usually much faster.

## 2. Verify the domain on GitHub (takeover protection; Nik, in the browser)

1. Open github.com → profile picture → **Settings** (profile, not repo) → **Pages** → **Add a domain**.
2. Enter `botsdothat.com`.
3. GitHub shows a TXT record named `_github-pages-challenge-nik-schultz` and a code. Add it at IONOS (table row above) and keep it there permanently.
4. Click **Verify** once `scripts/domain_cutover.sh check` shows the TXT value.

## 3. Cut over (agent or Nik, on the box)

```bash
scripts/domain_cutover.sh check   # read-only: shows A/AAAA/www/TXT + GitHub Pages status
scripts/domain_cutover.sh apply   # refuses unless the 4 A records resolve. Then it:
                                  #  1) sets the Pages custom domain (gh api -X PUT repos/nik-schultz/agents-on-radar/pages -f cname=botsdothat.com)
                                  #  2) sets config.json cname=botsdothat.com, base_url=https://botsdothat.com/
                                  #  3) deploys with scripts/deploy.sh (never git push origin main)
scripts/domain_cutover.sh https   # after the cert is issued (minutes to 24h): gh api -X PUT .../pages -F https_enforced=true
scripts/domain_cutover.sh rollback  # back to the github.io URL if anything goes wrong
```

**Why this order:**
- GitHub's docs say to add the custom domain on GitHub before or right when DNS points at Pages, so nobody else can claim it.
- `apply` sets it and redeploys back to back. The old github.io build (with `/agents-on-radar/` paths) is served on the new domain for only the ~1–2 minutes the deploy takes.
- The site publishes through GitHub Actions, so GitHub ignores the `CNAME` file. The custom domain must be set through the API/Settings, which `apply` does. The build still writes `site/CNAME` from config for clarity.

## 4. What changes automatically after cutover

- **Paths:** `base_path` becomes empty, so every link, asset, canonical URL, og:url, JSON-LD URL, RSS link and llms.txt URL moves to `https://botsdothat.com/...`. I dry-ran this build on Oct 21: 0 broken internal links, canonical `https://botsdothat.com/advertise/`.
- **robots.txt and sitemap.xml:** they now live at the domain root (`https://botsdothat.com/robots.txt` → `Sitemap: https://botsdothat.com/sitemap.xml`). Crawlers now actually read them; today they sit under a subpath, which crawlers ignore.
- **Old links:** GitHub Pages redirects old `nik-schultz.github.io/agents-on-radar/...` links to the custom domain.

## 5. After cutover (checklist)

- [ ] `curl -sI https://botsdothat.com/` returns 200, and `curl -sI http://botsdothat.com/` redirects to https (after `https`).
- [ ] `curl -sI https://www.botsdothat.com/` redirects to the apex domain.
- [ ] `curl -sI https://nik-schultz.github.io/agents-on-radar/advertise/` returns a 301 to botsdothat.com.
- [ ] Search consoles: add `https://botsdothat.com/` in Google Search Console and Bing Webmaster Tools. Paste the meta values into `config.json → verification`, deploy, submit the sitemap.
- [ ] Update links in `ops/launch_drafts.md`, README and PLAN to https://botsdothat.com/.
- [ ] Optional later: rename the repo to `botsdothat`. Do this only after cutover; the custom domain keeps the URL stable. Update `REPO` in scripts/domain_cutover.sh, deploy.sh and the README.
- [ ] Optional: contact email on the domain (for example IONOS mail forwarding). It's not set up; `contact_url` stays GitHub Issues until then.
