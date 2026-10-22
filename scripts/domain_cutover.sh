#!/usr/bin/env bash
# Move the live site from https://nik-schultz.github.io/agents-on-radar/ to https://botsdothat.com/.
# Full runbook: ops/domain_cutover.md. Run ONLY after Nik owns botsdothat.com and the IONOS DNS records exist.
#   scripts/domain_cutover.sh check   # read-only: DNS + GitHub Pages status
#   scripts/domain_cutover.sh apply   # set Pages custom domain, set cname/base_url, deploy (deploy.sh)
#   scripts/domain_cutover.sh https   # turn on Enforce HTTPS once GitHub has issued the certificate
#   scripts/domain_cutover.sh rollback  # back to the github.io URL
set -euo pipefail
cd "$(dirname "$0")/.."
DOMAIN="botsdothat.com"; REPO="nik-schultz/agents-on-radar"; OLD_URL="https://nik-schultz.github.io/agents-on-radar/"
WANT_A="185.199.108.153 185.199.109.153 185.199.110.153 185.199.111.153"
doh(){ curl -s "https://dns.google/resolve?name=$1&type=$2" | python3 -c 'import sys,json;print(" ".join(sorted(a["data"].rstrip(".") for a in json.load(sys.stdin).get("Answer",[]))))'; }
setcfg(){ python3 - "$1" "$2" <<'PY'
import json,sys
p="config.json"; c=json.load(open(p)); c["cname"]=sys.argv[1]; c["base_url"]=sys.argv[2]
open(p,"w").write(json.dumps(c,indent=2,ensure_ascii=False)+"\n"); print("config.json: cname=%r base_url=%r"%(c["cname"],c["base_url"]))
PY
}
check(){
  echo "A     @   : $(doh $DOMAIN A)"; echo "AAAA  @   : $(doh $DOMAIN AAAA)"; echo "www       : $(doh www.$DOMAIN CNAME)"
  echo "TXT verify: $(doh _github-pages-challenge-nik-schultz.$DOMAIN TXT)"
  gh api "repos/$REPO/pages" --jq '"Pages: cname=\(.cname) https_enforced=\(.https_enforced) status=\(.status) protected=\(.protected_domain_state)"'
  gh api "repos/$REPO/pages/health" --jq '"Health: dns_resolves=\(.domain.dns_resolves) points_to_pages=\(.domain.is_pointed_to_github_pages_server) https_eligible=\(.domain.is_https_eligible) enforces_https=\(.domain.enforces_https)"' 2>/dev/null | grep Health || echo "Health: not available yet (needs a custom domain set)"
}
case "${1:-check}" in
  check) check ;;
  apply)
    [ "$(doh $DOMAIN A)" = "$WANT_A" ] || { echo "Apex A records are not the 4 GitHub Pages IPs yet. Fix DNS at IONOS (ops/domain_cutover.md) and wait."; check; exit 1; }
    gh api -X PUT "repos/$REPO/pages" -f cname="$DOMAIN" >/dev/null && echo "GitHub Pages custom domain set to $DOMAIN"
    setcfg "$DOMAIN" "https://$DOMAIN/"
    scripts/deploy.sh "Move site to https://$DOMAIN/"
    echo "Next: wait for the certificate (minutes to 24h), then: scripts/domain_cutover.sh https" ;;
  https)
    gh api -X PUT "repos/$REPO/pages" -F https_enforced=true >/dev/null && echo "Enforce HTTPS: on" || { echo "Not yet: certificate not issued. Retry later."; exit 1; }
    check ;;
  rollback)
    gh api -X PUT "repos/$REPO/pages" --input - <<<'{"cname":null}' >/dev/null && echo "GitHub Pages custom domain removed"
    setcfg "" "$OLD_URL"
    scripts/deploy.sh "Roll back to $OLD_URL" ;;
  *) echo "usage: $0 check|apply|https|rollback"; exit 2 ;;
esac
