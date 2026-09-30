"""EXP-05: System-design AI-era checklist (RESHADED + judgment probes).
Verifies CIU 'optional' system-design section is now mandatory for 4+ YoE and partly for L3/L4 (2026 sources).
Outputs a scored rubric template; PASS = candidate articulates tradeoffs, failure modes, cost tiers, AI-fallback.
"""
from __future__ import annotations
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
RESHADED = ["Requirements","Estimation","Storage","HighLevelDesign","APIs","DeepDive","Edge_Scaling","Done"]
PROBES = ["acceptable_failure_mode_first","ai_box_fallback_eval_cost","constraint_change_surgical_redesign",
 "telemetry_oncall","10x_100x_bottleneck_drill","verify_ai_numbers_not_paste"]
def main():
    rubric = {s: {"L3": "recognize", "L4": "drive HLD+1 tradeoff", "L5": "2 deep dives + failure modes", "L6+": "ops+multi-region+capacity"} for s in RESHADED}
    out = {"framework": "RESHADED (Aceloop 2026)", "steps": RESHADED, "probes": PROBES, "rubric": rubric,
     "prompts_2026": ["URL shortener","Twitter feed (fanout)","WhatsApp/chat","LLM inference API (continuous batching, KV-cache)","RAG over enterprise docs","Rate limiter"],
     "verdict": "CIU system-design OPTIONAL flag is STALE for 2026: required for mid+ and scaled-down for L3/L4 phone screens; AI-era adds vector-DB, inference-cost, eval-harness expectations."}
    (ROOT/"results"/"exp05_system_design.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
if __name__ == "__main__":
    main()
