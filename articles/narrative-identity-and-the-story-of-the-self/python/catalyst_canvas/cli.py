from pathlib import Path
import argparse, csv, json
from .models import CanvasConfig, CanvasRecord
from .validation import validate_config, validate_record
from .scoring import confidence_band, domain_strength, governance_priority_score, interpretation_readiness, review_priority, risk_score
from .governance import build_canvas_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue

def _pref(row, prefix):
    return {k.removeprefix(prefix): float(v) for k, v in row.items() if k.startswith(prefix) and v != ""}
def load_config(path):
    p=json.loads(path.read_text(encoding="utf-8"))
    c=CanvasConfig(p["article_title"],p["article_slug"],p.get("module_name","catalyst_canvas"),{k:float(v) for k,v in p["metric_weights"].items()},{k:float(v) for k,v in p["risk_weights"].items()},{k:float(v) for k,v in p["readiness_weights"].items()},{k:float(v) for k,v in p["thresholds"].items()})
    validate_config(c); return c
def load_records(path, config, strict):
    out=[]
    with path.open("r", encoding="utf-8", newline="") as h:
        for row in csv.DictReader(h):
            r=CanvasRecord(row["item"], row["claim_context"], row.get("article_title",config.article_title), row.get("article_slug",config.article_slug), _pref(row,"metric_"), _pref(row,"risk_"), _pref(row,"readiness_"), row.get("owner","editorial"), row.get("status","active"), row.get("notes",""))
            validate_record(r, config, strict); out.append(r)
    return out
def run(article_root: Path, input_path=None, config_path=None, output_dir=None, strict=False):
    article_root=article_root.resolve(); config=load_config(config_path or article_root/"canvas/catalyst_canvas_config.json"); records=load_records(input_path or article_root/"data/catalyst_canvas_assessment.csv", config, strict); output_dir=output_dir or article_root/"outputs"
    rows=[{"article_slug":config.article_slug,"item":r.item,"claim_context":r.claim_context,"domain_strength":round(domain_strength(r,config),4),"risk_score":round(risk_score(r,config),4),"interpretation_readiness":round(interpretation_readiness(r,config),4),"governance_priority_score":round(governance_priority_score(r,config),4),"review_priority":review_priority(r,config),"confidence_band":confidence_band(r,config),"owner":r.owner,"status":r.status,"governance_note":governance_note(r,config)} for r in records]
    rows=sorted(rows,key=lambda x:x["governance_priority_score"], reverse=True); cards=[build_canvas_card(r, config) for r in records]; queue=[r for r in rows if r["review_priority"]!="standard"]
    write_csv(output_dir/"tables/catalyst_canvas_audit.csv", rows); write_csv(output_dir/"tables/catalyst_canvas_governance_queue.csv", queue or rows[:1]); write_json(output_dir/"json/catalyst_canvas_cards.json", cards); write_json(output_dir/"json/catalyst_canvas_governance_queue.json", [c for c in cards if c["review"]["priority"]!="standard"]); write_markdown_queue(output_dir/"markdown/catalyst_canvas_governance_queue.md", queue or rows[:1]); write_json(article_root/"canvas/catalyst_canvas_cards.json", cards); write_json(article_root/"canvas/catalyst_canvas_governance_queue.json", [c for c in cards if c["review"]["priority"]!="standard"]); print("Catalyst Canvas audit complete")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[1]); ap.add_argument("--input", type=Path); ap.add_argument("--config", type=Path); ap.add_argument("--output-dir", type=Path); ap.add_argument("--strict", action="store_true"); a=ap.parse_args(); run(a.article_root,a.input,a.config,a.output_dir,a.strict)
if __name__=="__main__": main()
