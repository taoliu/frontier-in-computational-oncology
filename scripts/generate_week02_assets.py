#!/usr/bin/env python3
"""Generate original SVG teaching schematics for Week 02 Functional Genomics."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "07-assets" / "images" / "week-02-functional-genomics" / "svg"
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
<style>
  svg { font-family: Arial, Helvetica, sans-serif; background: #ffffff; }
  .title { font-size: 26px; font-weight: 700; fill: #14213d; }
  .subtitle { font-size: 15px; fill: #334155; }
  .label { font-size: 16px; font-weight: 700; fill: #0f172a; }
  .small { font-size: 13px; fill: #334155; }
  .tiny { font-size: 11px; fill: #475569; }
  .box { fill: #f8fafc; stroke: #334155; stroke-width: 1.5; rx: 14; }
  .input { fill: #e0f2fe; stroke: #0284c7; }
  .process { fill: #ecfdf5; stroke: #059669; }
  .warn { fill: #fff7ed; stroke: #ea580c; }
  .risk { fill: #fef2f2; stroke: #dc2626; }
  .purple { fill: #f3e8ff; stroke: #7e22ce; }
  .gray { fill: #f1f5f9; stroke: #64748b; }
  .dna { stroke: #334155; stroke-width: 3; fill: none; }
  .read { stroke: #2563eb; stroke-width: 5; stroke-linecap: round; }
  .peak { fill: #60a5fa; opacity: 0.75; }
  .accent { stroke: #f97316; stroke-width: 3; fill: none; }
  .arrow { stroke: #475569; stroke-width: 2.2; fill: none; marker-end: url(#arrow); }
  .dash { stroke-dasharray: 6 5; }
</style>
"""

DEFS = """
<defs>
  <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L0,6 L9,3 z" fill="#475569" />
  </marker>
</defs>
"""

def wrap(title, subtitle, body, w=1280, h=720):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
{DEFS}
{CSS}
<text x="48" y="54" class="title">{escape(title)}</text>
<text x="48" y="82" class="subtitle">{escape(subtitle)}</text>
{body}
</svg>'''

def text(x,y,s,cls='small'):
    return f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>'

def rect(x,y,w,h,cls='box'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}" />'

def line(x1,y1,x2,y2,cls='arrow'):
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="{cls}" />'

def write(name, title, subtitle, body):
    p=OUT/name
    p.write_text(wrap(title, subtitle, body))
    print(p)

# W02-A001 Assay comparison
cols=[('ChIP-seq','Antibody enrichment','Peaks / domains','TFs, histone marks','input'),('ATAC-seq','Tn5 insertion','Accessible fragments','Open chromatin + nucleosomes','process'),('CUT&RUN / CUT&Tag','Tethered cleavage/tagging','Low-background peaks','TFs or chromatin marks','warn'),('Hi-C / HiChIP','Proximity ligation','Contact matrix','Enhancer-promoter linkage','purple')]
body=''
for i,(name,chem,out,use,cls) in enumerate(cols):
    x=70+i*300
    body+=rect(x,130,250,420,cls)
    body+=text(x+24,170,name,'label')
    body+=text(x+24,205,chem)
    body+=line(x+125,225,x+125,270)
    # cartoon
    body+=f'<path d="M{x+38},310 C{x+85},280 {x+140},340 {x+210},305" class="dna" />'
    if i==0:
        body+=f'<circle cx="{x+122}" cy="296" r="28" fill="#fde68a" stroke="#d97706"/><text x="{x+102}" y="301" class="tiny">Ab</text>'
        body+=f'<path d="M{x+70},390 C{x+100},330 {x+140},330 {x+185},390" class="peak"/>'
    elif i==1:
        for j,l in enumerate([28,55,90,135]): body+=f'<line x1="{x+55+j*40}" y1="{390}" x2="{x+55+j*40+l/2}" y2="{390}" class="read"/>'
    elif i==2:
        body+=f'<circle cx="{x+122}" cy="300" r="24" fill="#fed7aa" stroke="#ea580c"/><path d="M{x+122},324 L{x+122},385" class="accent"/><path d="M{x+75},390 C{x+110},350 {x+150},350 {x+185},390" class="peak"/>'
    else:
        for r in range(4):
            for c in range(4):
                op=0.2+0.15*(r==c)+0.1*((r+c)%3==0)
                body+=f'<rect x="{x+65+c*30}" y="{350+r*30}" width="26" height="26" fill="#7e22ce" opacity="{op}"/>'
    body+=text(x+24,460,'Output: '+out)
    body+=text(x+24,492,'Use: '+use)
body+=text(70,615,'Teaching point: assay chemistry determines the statistical object before software enters the story.','label')
write('W02-A001_assay_comparison.svg','Assay families produce different computational objects','ChIP-seq, ATAC-seq, CUT assays, and contact assays require different models.',body)

# W02-A002 MACS
body=rect(70,125,1140,470,'input')
body+=text(95,165,'Observed ChIP-seq pileup','label')
body+=f'<line x1="120" y1="470" x2="1130" y2="470" stroke="#334155" stroke-width="3"/>'
for x,w,h in [(180,60,50),(260,55,70),(345,50,90),(520,45,220),(570,45,260),(620,45,210),(820,65,65),(910,55,45)]:
    body+=f'<rect x="{x}" y="{470-h}" width="{w}" height="{h}" class="peak"/>'
body+=f'<path d="M480,470 C510,280 640,260 690,470" fill="#2563eb" opacity="0.30" stroke="#2563eb" stroke-width="2"/>'
body+=f'<line x1="500" y1="520" x2="700" y2="520" stroke="#f97316" stroke-width="4"/><text x="535" y="550" class="small">candidate enriched region</text>'
body+=f'<line x1="130" y1="595" x2="1150" y2="595" stroke="#64748b" stroke-width="2" stroke-dasharray="8 7"/>'
body+=text(135,625,'Local background model: estimate expected read density around the candidate peak, not from a flat genome-wide constant.','label')
body+=line(600,400,600,330)
body+=text(630,340,'Summit / peak evidence','small')
body+=line(320,405,450,520)
body+=text(155,365,'Regional background','small')
body+=text(95,210,'MACS teaching idea: model enrichment over a dynamic local background, after estimating fragment shift from strand geometry.','small')
write('W02-A002_MACS_local_background.svg','MACS-style peak calling: enrichment over local background','A narrow peak is a statistical claim against a structured background, not just a tall pileup.',body)

# W02-A003 HMMRATAC
body=''
for i,(name,y,color,lengths) in enumerate([
 ('Nucleosome-free fragments',160,'#38bdf8',[45,55,35,50]),
 ('Mono-nucleosome fragments',260,'#34d399',[110,130,100]),
 ('Di-nucleosome fragments',360,'#a78bfa',[210,240])]):
    body+=text(80,y-25,name,'label')
    body+=f'<line x1="360" y1="{y}" x2="1160" y2="{y}" stroke="#cbd5e1" stroke-width="3"/>'
    x=410
    for l in lengths:
        body+=f'<line x1="{x}" y1="{y}" x2="{x+l}" y2="{y}" stroke="{color}" stroke-width="8" stroke-linecap="round"/>'
        x+=l+70
body+=rect(80,455,260,120,'process')+text(110,495,'Fragment classes','label')+text(110,525,'separate signal tracks')
body+=line(340,515,470,515)
body+=rect(470,455,260,120,'purple')+text(500,495,'Three-state HMM','label')+text(500,525,'open / nucleosomal / background')
body+=line(730,515,860,515)
body+=rect(860,455,300,120,'input')+text(890,495,'ATAC peak calls','label')+text(890,525,'assay-specific chromatin states')
body+=text(80,635,'Teaching point: ATAC-seq paired-end fragment lengths carry biological structure that a generic pileup model may ignore.','label')
write('W02-A003_HMMRATAC_states.svg','HMMRATAC: fragment classes become hidden chromatin states','ATAC-specific modeling uses fragment-size information to distinguish open chromatin and nucleosome context.',body)

# W02-A005 Enhancer hijacking
body=''
body+=text(95,145,'Normal regulatory neighborhood','label')
body+=rect(80,170,500,180,'gray')
body+=f'<path d="M120,260 C210,210 310,300 420,245 C480,215 525,235 555,255" class="dna"/>'
body+=f'<rect x="155" y="220" width="70" height="24" fill="#fbbf24" stroke="#d97706"/><text x="145" y="210" class="tiny">enhancer</text>'
body+=f'<rect x="440" y="240" width="80" height="28" fill="#93c5fd" stroke="#2563eb"/><text x="438" y="285" class="tiny">gene A</text>'
body+=text(115,330,'Oncogene is outside this enhancer domain','small')
body+=text(720,145,'After structural rearrangement','label')
body+=rect(700,170,500,180,'warn')
body+=f'<path d="M740,260 C830,210 930,300 1040,245 C1100,215 1145,235 1175,255" class="dna"/>'
body+=f'<rect x="775" y="220" width="70" height="24" fill="#fbbf24" stroke="#d97706"/><text x="765" y="210" class="tiny">active enhancer</text>'
body+=f'<rect x="1020" y="240" width="105" height="28" fill="#fecaca" stroke="#dc2626"/><text x="1018" y="285" class="tiny">oncogene</text>'
body+=f'<path d="M820,230 C880,165 1010,165 1065,240" stroke="#ef4444" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'
body+=text(735,330,'Enhancer now activates a cancer gene','small')
body+=line(585,260,695,260)
body+=text(595,235,'SV / rearrangement','small')
body+=rect(160,440,960,110,'purple')
body+=text(190,482,'Teaching point','label')
body+=text(190,515,'Enhancer hijacking links structural variation, chromatin state, and oncogene activation — but the figure should stay mechanism-focused.')
body+=text(190,545,'Examples for placeholders: medulloblastoma GFI1/GFI1B and BCL11B lineage-ambiguous leukemia.','tiny')
write('W02-A005_enhancer_hijacking.svg','Enhancer hijacking: structural variation rewires regulatory context','A rearrangement can move an oncogene into an active enhancer neighborhood.',body)
