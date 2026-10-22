#!/usr/bin/env bash
# Build, check, commit and publish the site to GitHub Pages.
#   scripts/deploy.sh "Short description of the change"
# Local `main` keeps the full history. The public repo gets a separate, small `publish` history:
# each deploy adds ONE commit whose tree equals main's tree (files in .gitignore, such as raw art
# and raw API dumps, are never included). `publish` is pushed to origin/main, and that push
# triggers .github/workflows/pages.yml, which re-checks site/ and deploys it.
set -euo pipefail
cd "$(dirname "$0")/.."
MSG="${1:-Site update $(date +%F)}"
G=(git -c user.name="CEO agent" -c user.email="ceo-agent@localhost")
python3 scripts/validate.py
python3 scripts/build.py
python3 scripts/check_links.py
[ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] || { echo "Run from branch main"; exit 1; }
git add -A
"${G[@]}" commit -q -m "$MSG" || echo "main: nothing new to commit"
# refuse to publish anything that should stay private
if git ls-tree -r --name-only main | grep -E '^art/incoming/|\.env$|\.pem$|\.key$|^research/.*\.json\.txt$|^research/x_posts_full\.json$|\.log$'; then
  echo "Private files are tracked on main (listed above). Remove them before deploying."; exit 1; fi
TREE=$(git rev-parse 'main^{tree}')
PARENT=$(git rev-parse -q --verify refs/heads/publish || true)
if [ -n "$PARENT" ] && [ "$(git rev-parse 'publish^{tree}')" = "$TREE" ]; then
  echo "publish: already up to date"
else
  C=$("${G[@]}" commit-tree "$TREE" ${PARENT:+-p "$PARENT"} -m "$MSG")
  git update-ref refs/heads/publish "$C"
fi
git push origin publish:main
echo "Pushed. Live in ~1-2 min: $(python3 -c 'import json;print(json.load(open("config.json"))["base_url"])')"
echo "Watch: gh run watch \$(gh run list -R nik-schultz/agents-on-radar -L1 --json databaseId -q '.[0].databaseId') -R nik-schultz/agents-on-radar"
