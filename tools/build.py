"""data/*.json + src/template.html -> index.html"""
import json,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
b=json.loads((R/'data/past.json').read_text())
b['q']+=json.loads((R/'data/variants.json').read_text())
d=json.dumps(b,ensure_ascii=False).replace('</','<\\/')
(R/'index.html').write_text((R/'src/template.html').read_text().replace('__GEN__',(R/'src/gen.js').read_text()).replace('__DATA__',d))
print(len(b['q']),'questions')
