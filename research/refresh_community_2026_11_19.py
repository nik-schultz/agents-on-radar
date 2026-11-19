# Refresh measured stats on HN (Algolia items API) and GitHub (gh api) sources. Real numbers only; label numbers updated in place.
import json,re,subprocess,urllib.request
P='data/use-cases.json'; H='data/popularity-history.jsonl'; M='2026-11-19'
u=json.load(open(P)); hist=open(H,'a'); n_hn=n_gh=0; changed=[]
def fmt(n): return f"{n:,}"
for x in u:
    for s in x['sources']:
        if 'stats' not in s: continue
        try:
            if s['kind']=='hn':
                i=re.search(r'id=(\d+)',s['url']).group(1)
                d=json.load(urllib.request.urlopen(f'https://hn.algolia.com/api/v1/items/{i}',timeout=20))
                pts=d.get('points'); 
                if pts is None: continue
                com=sum(1 for _ in iter_c(d)) if False else None
                # Algolia items API has no direct count; use search API for num_comments
                q=json.load(urllib.request.urlopen(f'https://hn.algolia.com/api/v1/search?tags=story_{i}',timeout=20))
                if not q['hits']: continue
                pts=q['hits'][0]['points']; com=q['hits'][0]['num_comments']
                old=dict(s['stats']); new={'points':pts,'comments':com}
                if 'points' not in old: continue
                s['label']=re.sub(r'\(?\b[\d,]+ points? / [\d,]+ comments(, measured \d{4}-\d\d-\d\d)?',(lambda m: ("(" if m.group(0).startswith("(") else "")+f"{fmt(pts)} points / {fmt(com)} comments, measured {M}"),s['label'])
                s['stats']=new; s['measured_at']=M; n_hn+=1
            elif s['kind']=='github':
                repo=re.search(r'github\.com/([^/]+/[^/#?]+)',s['url']).group(1)
                st=int(subprocess.check_output(['gh','api','repos/'+repo,'--jq','.stargazers_count']).decode().strip())
                old=dict(s['stats']); new={**old,'stars':st}
                s['label']=re.sub(r'[\d,]+ stars(, (measured|checked) \d{4}-\d\d-\d\d)?',f"{fmt(st)} stars, measured {M}",s['label'])
                s['label']=re.sub(r'measured \d{4}-\d\d-\d\d\)',f'measured {M})',s['label']) if 'stars' not in s['label'] else s['label']
                s['stats']=new; s['measured_at']=M; n_gh+=1
            else: continue
            if old!=s['stats']: changed.append((x['slug'],s['url'],old,s['stats']))
            hist.write(json.dumps({"slug":x['slug'],"platform":s['kind'],"url":s['url'],**s['stats'],"measured_at":M})+"\n")
        except Exception as e:
            print('skip',s['url'],e)
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('hn',n_hn,'github',n_gh)
for c in changed: print(c)
