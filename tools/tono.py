"""Aplica al final: narración reescrita (content/tono.json) y hojas extra (content/extra_hojas_*.json)."""
import json,glob,os
G=json.load(open('content/guiones.json'));H=json.load(open('content/hojas.json'))
if os.path.exists('content/tono.json'):
    T=json.load(open('content/tono.json'))
    for q,lv in T.items():
        for l,bs in lv.items():
            old=G[q][l]
            if len(old)==len(bs):
                for o,n in zip(old,bs): o['t']=n['t']
for q in G:
    if q.startswith('ing-'):
        for bs in G[q].values():
            for o in bs:
                o['t']=o['t'].replace('he, she e it','{{he}}, {{she}} e {{it}}').replace('I, you, we y they','{{I}}, {{you}}, {{we}} y {{they}}')
for f in sorted(glob.glob('content/extra_hojas_*.json')):
    for q,hj in json.load(open(f)).items(): H[q]=hj
import os
if os.path.exists('content/pasos_extra.json'):
    for q,lst in json.load(open('content/pasos_extra.json')).items():
        for it in sorted(lst,key=lambda x:-x['despues']): H[q]['pasos'].insert(it['despues']+1,it['paso'])
if os.path.exists('content/extra_guiones.json'):
    for q,lv in json.load(open('content/extra_guiones.json')).items(): G[q]=lv
if os.path.exists('content/extra_enfoques.json'):
    E=json.load(open('content/enfoques.json'))
    for q,e in json.load(open('content/extra_enfoques.json')).items(): E[q]=e
    json.dump(E,open('content/enfoques.json','w'),ensure_ascii=False,indent=1)
json.dump(H,open('content/hojas.json','w'),ensure_ascii=False,indent=1);json.dump(G,open('content/guiones.json','w'),ensure_ascii=False,indent=1)
print('tono ok')
