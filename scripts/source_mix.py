#!/usr/bin/env python3
"""Print the source mix of data/use-cases.json as a markdown section.
  python3 scripts/source_mix.py "Before (2026-10-24)"   -> markdown to stdout
Counts the links in each entry's `sources` list (what readers see under "Sources"), grouped by platform."""
import json, os, sys, collections
from urllib.parse import urlparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ucs = json.load(open(os.path.join(ROOT, "data", "use-cases.json")))

def platform(url):
    h = urlparse(url).netloc.lower().removeprefix("www.").removeprefix("old.")
    if h in ("x.com", "twitter.com"): return "X"
    if h.endswith("reddit.com") or h == "reddit.sentinel-team.org": return "Reddit"
    if h == "news.ycombinator.com": return "Hacker News"
    if h in ("youtube.com", "youtu.be", "m.youtube.com"): return "YouTube"
    if h == "github.com": return "GitHub"
    if h == "producthunt.com": return "Product Hunt"
    if h == "google.com" or h == "trends.google.com": return "Search demand (Google)"
    return "Official docs, news and blogs"

COMM = ("X", "Reddit", "Hacker News", "YouTube", "GitHub", "Product Hunt")
def main(title):
    links = collections.Counter(); doms = collections.Counter(); entries_with = collections.Counter()
    x_only = 0; community = 0; n_links = 0
    for x in ucs:
        plats = set()
        for s in x["sources"]:
            p = platform(s["url"]); links[p] += 1; n_links += 1; plats.add(p)
            doms[urlparse(s["url"]).netloc.lower().removeprefix("www.")] += 1
        for p in plats: entries_with[p] += 1
        if plats == {"X"}: x_only += 1
        if plats & {"Reddit", "Hacker News", "YouTube", "GitHub", "Product Hunt"}: community += 1
    all_urls = json.dumps(ucs).count('https://x.com/')
    out = [f"## {title}", "",
           f"- Use cases: **{len(ucs)}**; source links: **{n_links}**",
           f"- X share of source links: **{links['X']}/{n_links} = {100*links['X']/n_links:.0f}%**",
           f"- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **{links['X']}/{sum(links[k] for k in COMM)} = {100*links['X']/max(1,sum(links[k] for k in COMM)):.0f}%**",
           f"- X-only use cases (every source is an X post): **{x_only}** ({100*x_only/len(ucs):.0f}%)",
           f"- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **{community}**",
           f"- x.com URLs anywhere in the file (sources + popularity blocks + examples): {all_urls}", "",
           "| Platform | Source links | Use cases citing it |", "|---|---:|---:|"]
    out += [f"| {p} | {c} | {entries_with[p]} |" for p, c in links.most_common()]
    out += ["", "Top domains: " + ", ".join(f"{d} ({c})" for d, c in doms.most_common(12)), ""]
    print("\n".join(out))

if __name__ == "__main__": main(sys.argv[1] if len(sys.argv) > 1 else "Source mix")
