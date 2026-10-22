#!/usr/bin/env bash
# Daily routine: validate -> append new use cases -> merge fresh popularity -> rebuild -> link check.
# Usage: scripts/daily.sh [x-metrics-file ...]
#   x-metrics-file = saved output of the X tool get_posts_by_ids for the ids from
#   `python3 scripts/refresh_popularity.py --export-ids`
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate.py
python3 scripts/add_use_cases.py
if [ "$#" -gt 0 ]; then python3 scripts/refresh_popularity.py --from-x "$@"; fi
python3 scripts/validate.py
python3 scripts/build.py
python3 scripts/check_links.py
