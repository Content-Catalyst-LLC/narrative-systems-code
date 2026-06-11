from pathlib import Path
import argparse, csv
from .models import NarrativeIdentityConfig, NarrativeIdentityRecord
from .validation import validate_record
from .scoring import governance_priority_score, identity_story_risk, interpretation_readiness, narrative_coherence, review_priority, revision_readiness
from .governance import build_identity_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue

def load_records(path, config):
    records=[]
    with path.open("r",encoding="utf-8",newline="") as h:
        for row in csv.DictReader(h):
            vals=[row["item"],row["claim_context"]]+[float(row[k]) for k in ["memory_continuity","temporal_progression","agency","relational_grounding","promise_responsibility","future_openness","change_handling","memory_revision","uncertainty_notes","counter_memory","silence_respect","openness_to_retelling","reduction_risk","forced_coherence","power_blindness","trauma_extraction","algorithmic_capture","source_context","cultural_context","method_limits","ethics_governance","review_owner_clarity","public_consequence"]]+[row.get("owner","editorial"),row.get("status","active"),row.get("notes","")]
            r=NarrativeIdentityRecord(*vals); validate_record(r,config); records.append(r)
    return records

def row(r,c): return {"item":r.item,"claim_context":r.claim_context,"narrative_coherence":round(narrative_coherence(r),4),"revision_readiness":round(revision_readiness(r),4),"identity_story_risk":round(identity_story_risk(r),4),"interpretation_readiness":round(interpretation_readiness(r),4),"governance_priority_score":round(governance_priority_score(r,c),4),"review_priority":review_priority(r,c),"owner":r.owner,"status":r.status,"governance_note":governance_note(r,c)}
def run(article_root: Path, input_path=None, output_dir=None):
    article_root=article_root.resolve(); config=NarrativeIdentityConfig(); input_path=input_path or article_root/"data/narrative_identity_claims.csv"; output_dir=output_dir or article_root/"outputs"
    records=load_records(input_path,config); rows=sorted([row(r,config) for r in records], key=lambda x:x["governance_priority_score"], reverse=True); cards=[build_identity_card(r,config) for r in records]; queue=[r for r in rows if r["review_priority"]!="standard"]
    write_csv(output_dir/"tables/narrative_identity_audit.csv", rows); write_csv(output_dir/"tables/narrative_identity_governance_queue.csv", queue); write_json(output_dir/"json/narrative_identity_canvas_cards.json", cards); write_json(output_dir/"json/narrative_identity_governance_queue.json", [c for c in cards if c["review"]["priority"]!="standard"]); write_markdown_queue(output_dir/"markdown/narrative_identity_governance_queue.md", queue); print("Narrative identity Canvas audit complete")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--article-root",type=Path,default=Path(__file__).resolve().parents[2]); ap.add_argument("--input",type=Path); ap.add_argument("--output-dir",type=Path); a=ap.parse_args(); run(a.article_root,a.input,a.output_dir)
if __name__=="__main__": main()
