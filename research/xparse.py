import json,sys
for f in sys.argv[1:]:
  s=open(f).read(); i=s.find('{'); d=json.loads(s[i:s.rfind('}')+1])
  users={u['id']:u['username'] for u in d.get('includes',{}).get('users',[])}
  print('META',d.get('meta'))
  for p in d.get('data',[]):
    m=p['public_metrics']; print(p['id'],users.get(p.get('author_id'),''),p['created_at'][:16],m['like_count'],m['retweet_count'],m.get('impression_count'),p['text'][:160].replace('\n',' '))
