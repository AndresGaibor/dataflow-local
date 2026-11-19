import json,glob,sys,collections
types=collections.defaultdict(lambda:[0,set(),None])
top=collections.Counter(); links=collections.Counter(); ctx=set()
for f in glob.glob(sys.argv[1]+'/*.dfw'):
    d=json.load(open(f,encoding='utf-8'))
    top.update(d.keys()); df=d['dataflow']; ctx.add(json.dumps(df['context'].get('usage')))
    top.update('dataflow.'+k for k in df)
    g=df['graph']; links.update('graph.'+k for k in g)
    for n in g['nodes']:
        c=n['component']; t=(n['type'],c['type'])
        e=types[t]; e[0]+=1
        p=c.get('properties',{}); e[1].update(p.keys())
        cfg=p.get('configuration',{})
        if isinstance(cfg,dict): e[1].update('cfg.'+k for k in cfg)
        if e[2] is None and cfg: e[2]=(f.split('/')[-1],json.dumps(cfg)[:600])
print(dict(top)); print(dict(links)); print(ctx)
for t,e in sorted(types.items()): print(t,e[0],sorted(e[1]))
print('---EX')
for t,e in sorted(types.items()): print(t,e[2])
