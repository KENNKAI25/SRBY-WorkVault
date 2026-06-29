#!/usr/bin/env python3
# Self-contained dashboard builder. Session-agnostic: locates workspace via glob.
# Reads SR Sales Data + stock, injects into template.html (same folder), writes dashboard HTML.
import re, json, os, glob, sys

def find_base():
    for p in glob.glob('/sessions/*/mnt/SRBY-WorkVault'):
        if os.path.isdir(p): return p
    # fallback: walk up from script
    raise SystemExit("ERROR: workspace SRBY-WorkVault not found")

BASE_WS = find_base()
SAR = os.path.join(BASE_WS, "04 - Sales Data", "Saramonic")
SR  = os.path.join(SAR, "SR Sales Data")
MONTHS = ["2025-10","2025-11","2025-12","2026-01","2026-02","2026-03","2026-04","2026-05","2026-06"]

def num(s):
    s=s.strip().replace(",","")
    if s=="":return None
    try:return float(s)
    except:return None
def rows(path):
    out=[]
    for line in open(path,encoding="utf-8"):
        line=line.rstrip("\n")
        if not line.startswith("|"):continue
        out.append(line.split("|")[1:-1])
    return out

skus={}; cur=""
for r in rows(os.path.join(SR,"Sales by SKU (Value).md"))[3:]:
    if len(r)<12:continue
    t=r[0].strip(); name=r[1].strip()
    if name in("","Total"):continue
    if t:cur=t
    skus.setdefault(name,{"type":cur or "Other","value":{},"qty":{}})
    skus[name]["type"]=cur or skus[name]["type"]
    skus[name]["value"]={MONTHS[i]:(num(r[2+i]) or 0) for i in range(9)}
for r in rows(os.path.join(SR,"Sales by SKU (QTY).md"))[3:]:
    if len(r)<11:continue
    name=r[0].strip()
    if name in("","Total"):continue
    skus.setdefault(name,{"type":"Other","value":{},"qty":{}})
    skus[name]["qty"]={MONTHS[i]:(num(r[1+i]) or 0) for i in range(9)}

dealers={}; cl=""
for r in rows(os.path.join(SR,"Sales by Dealer (Value by Location).md"))[3:]:
    if len(r)<12:continue
    loc=r[0].strip(); name=r[1].strip()
    if loc=="Total":continue
    if loc:cl=loc
    if name=="":continue
    dealers.setdefault(name,{"location":cl,"value":{},"qty":{},"skus":{},"skuMon":{}})
    dealers[name]["location"]=cl
    dealers[name]["value"]={MONTHS[i]:(num(r[2+i]) or 0) for i in range(9)}
cd=""
for r in rows(os.path.join(SR,"Sales by Dealer (QTY).md"))[3:]:
    if len(r)<12:continue
    c=r[0].strip(); sku=r[1].strip()
    if c=="Total":continue
    if c:cd=c
    if sku=="":continue
    vals=[(num(r[2+i]) or 0) for i in range(9)]
    d=dealers.setdefault(cd,{"location":"","value":{},"qty":{},"skus":{},"skuMon":{}})
    d.setdefault("skuMon",{}); d.setdefault("skus",{})
    d["skus"][sku]=d["skus"].get(sku,0)+sum(vals)
    sm=d["skuMon"].setdefault(sku,[0]*9)
    for i,m in enumerate(MONTHS):
        sm[i]+=vals[i]; d["qty"][m]=d["qty"].get(m,0)+vals[i]

def norm(s): return re.sub(r'[^a-z0-9]','',s.lower()).replace("saramonic","")
stock={}
for line in open(os.path.join(SAR,"Saramonic Stock Data.md"),encoding="utf-8"):
    if not line.startswith("|"):continue
    c=[x.strip() for x in line.split("|")[1:-1]]
    if len(c)<6:continue
    title=c[1]; av=num(c[5])
    if title in("Title","") or av is None:continue
    stock[norm(title)]=stock.get(norm(title),0)+av

# ---------- v1.1 extra data ----------
import re as _re2
def ndnorm(s): return _re2.sub(r'[^a-z0-9]','',s.lower())

# Categories — Sales by Dealer (Value by Category)
categories=[]
for r in rows(os.path.join(SR,"Sales by Dealer (Value by Category).md"))[3:]:
    if len(r)<11: continue
    cname=r[0].strip()
    if cname in("","Total"): continue
    cvals=[num(r[1+i]) or 0 for i in range(9)]
    categories.append({"name":cname,"value":cvals,"total":sum(cvals)})

# New vs Old partner — Sales by New and Old Dealer (Value)
newold={"rows":[],"prop":[]}
_mode=None
for r in rows(os.path.join(SR,"Sales by New and Old Dealer (Value).md")):
    if not r: continue
    h=r[0].strip()
    if h=="Sales Revenue": _mode="rev"; continue
    if h=="Sales Proportion": _mode="prop"; continue
    if h in("Old Partner","New Partner","Total"):
        if _mode=="rev":
            newold["rows"].append({"name":h,"value":[num(r[1+i]) or 0 for i in range(9)],
                "y2025":(num(r[16]) if len(r)>16 else None),
                "y2026":(num(r[17]) if len(r)>17 else None),
                "sub":(num(r[18]) if len(r)>18 else None)})
        elif _mode=="prop":
            newold["prop"].append({"name":h,"value":[(r[1+i].strip() if len(r)>1+i else "") for i in range(9)]})

# New dealers 2026 — first purchase month
_MONLBL={"jan":"2026-01","feb":"2026-02","mar":"2026-03","apr":"2026-04","may":"2026-05","mei":"2026-05",
         "jun":"2026-06","jul":"2026-07","aug":"2026-08","sep":"2026-09","oct":"2026-10","nov":"2026-11","dec":"2026-12"}
newdealer={}
_curm=None
for _line in open(os.path.join(SR,"New Dealer 2026.md"),encoding="utf-8"):
    s=_line.strip()
    if s.startswith("#"):
        key=s.lstrip("#").strip().split("-")[0].strip().lower()[:3]
        _curm=_MONLBL.get(key)
    elif s and _curm:
        nm=_re2.sub(r'^\d+[\.\)]\s*','',s).strip()
        if nm: newdealer[ndnorm(nm)]=_curm

sku_list=[]
for name,d in skus.items():
    v=d["value"]; q=d.get("qty",{})
    sku_list.append({"name":name,"type":d["type"],
        "value":[v.get(m,0) for m in MONTHS],"qty":[q.get(m,0) for m in MONTHS],
        "totalValue":sum(v.get(m,0) for m in MONTHS),"totalQty":sum(q.get(m,0) for m in MONTHS),
        "stock":stock.get(norm(name))})
dealer_list=[]
for name,d in dealers.items():
    v=d["value"]; q=d.get("qty",{})
    top=sorted(d["skus"].items(),key=lambda x:-x[1])[:5]
    sm=d.get("skuMon",{})
    skuMonthly=sorted([{"name":k,"m":val,"t":sum(val)} for k,val in sm.items()],key=lambda x:-x["t"])
    dealer_list.append({"name":name,"location":d.get("location",""),
        "value":[v.get(m,0) for m in MONTHS],"qty":[q.get(m,0) for m in MONTHS],
        "totalValue":sum(v.get(m,0) for m in MONTHS),"topSkus":top,"skuMonthly":skuMonthly,
        "newMonth":newdealer.get(ndnorm(name))})
monthly_total=[sum(s["value"][i] for s in sku_list) for i in range(9)]

import datetime
gen=datetime.date.today().isoformat()
data={"months":MONTHS,"skus":sku_list,"dealers":dealer_list,"monthlyTotal":monthly_total,"generated":gen,"categories":categories,"newold":newold}

SCRIPTDIR=os.path.dirname(os.path.abspath(__file__))
tpl=open(os.path.join(SCRIPTDIR,"template.html"),encoding="utf-8").read()
html=tpl.replace("__DATA__",json.dumps(data,ensure_ascii=False))
if "__DATA__" in html: raise SystemExit("ERROR: placeholder not replaced")
out=os.path.join(SAR,"Sales Analysis","Saramonic Sales Dashboard.html")
open(out,"w",encoding="utf-8").write(html)
print("OK SKUs=%d Dealers=%d Grand=%d Gen=%s"%(len(sku_list),len(dealer_list),int(sum(monthly_total)),gen))
print("OUTPUT_HTML="+out)
