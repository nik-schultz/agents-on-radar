import json,sys
for f in sys.argv[1:]:
    s=open(f).read()
    i=s.find('{'); d=json.loads(s[i:s.rfind('}')+1])
    users={u['id']:u['username'] for u in d.get('includes',{}).get('users',[])}
    print("=====",f[:8], d.get('meta',{}).get('result_count'))
    for p in sorted(d.get('data',[]),key=lambda p:-p['public_metrics']['like_count']):
        m=p['public_metrics']
        print(f"[{m['like_count']}L {m['retweet_count']}R] {p['created_at'][:10]} @{users.get(p['author_id'])} {p['id']}: {p['text'][:230]!r}")
