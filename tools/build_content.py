"""Regenera todo el contenido en orden. Ejecutar desde la raíz: python3 tools/build_content.py"""
import json,subprocess,sys
subprocess.check_call([sys.executable,'tools/make_hojas.py'])
subprocess.check_call([sys.executable,'tools/make_ing.py'])
subprocess.check_call([sys.executable,'tools/enfoques.py'])
G={}
def S(id,l1,l2,l3): G[id]={'1':l1,'2':l2,'3':l3}
def b(t,a=None,k=None):
    d={'t':t}
    if a: d['a']=a
    if k: d['k']=k
    return d
for f in ['g1','g2','g3','g4','g5']: exec(open(f'tools/{f}.py').read().replace('G={}',''))
json.dump(G,open('content/guiones.json','w'),ensure_ascii=False,indent=1)
print('guiones',len(G))
subprocess.check_call([sys.executable,'tools/visual.py'])
subprocess.check_call([sys.executable,'tools/visual3.py'])
subprocess.check_call([sys.executable,'tools/tono.py'])
