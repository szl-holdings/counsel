"""Ayllu Counsel — Hugging Face Space (Gradio).

Continuance of retired Counsel + Ayllu eleven seats.
Live scrapes a-11-oy.com legal vertical and SZLHOLDINGS Hub.
grok-4.5 only when XAI_API_KEY is present. SHA3-256 UNSIGNED-honest receipts.
Λ = Conjecture 1. SLSA L1. Not legal advice.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
import uuid

import gradio as gr

GENESIS = "0" * 64
MODEL = "grok-4.5"
A11OY = "https://a-11-oy.com"
HF = "https://huggingface.co/api"
DISCLAIMER = (
    "Informational only. Does not constitute legal advice. Not a law firm. "
    "No attorney-client relationship. Λ = Conjecture 1. SLSA L1. UNSIGNED-honest."
)


def sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def dump(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def mint(action: str, decision: str, honesty: str, prev: str, payload: object, model: str | None) -> dict:
    prev = prev if isinstance(prev, str) and len(prev) == 64 else GENESIS
    body = {
        "id": str(uuid.uuid4()),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "organ": "counsel",
        "action": action,
        "decision": decision,
        "honesty_tier": honesty,
        "lambda": "Conjecture 1",
        "slsa": "L1",
        "prev_hash": prev,
        "input_digest": sha3(dump(payload)),
        "model": model,
        "energy": None,
        "signer": "UNSIGNED-honest",
        "doctrine": "v11",
        "lock": "749/14/163",
    }
    body["hash"] = sha3(dump(body))
    return body


def pull(url: str, timeout: int = 10):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as exc:
        return {"_unavailable": str(exc), "url": url}


def grok(prompt: str, system: str, max_tokens: int = 480) -> tuple[str, str]:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        return "UNAVAILABLE — XAI_API_KEY absent", "UNAVAILABLE"
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt[:6000]},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.2,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as res:
            data = json.loads(res.read().decode("utf-8"))
        text = data["choices"][0]["message"]["content"]
        return text, "CONJECTURE"
    except Exception as exc:
        return f"UNAVAILABLE — {exc}", "UNAVAILABLE"


def show_docket():
    health = pull(f"{A11OY}/healthz")
    feed = pull(f"{A11OY}/api/a11oy/v1/vert/legal/feed?limit=8")
    return json.dumps({"health": health, "feed": feed, "disclaimer": DISCLAIMER}, indent=2)[:12000]


def show_estate():
    models = pull(f"{HF}/models?author=SZLHOLDINGS&limit=40")
    spaces = pull(f"{HF}/spaces?author=SZLHOLDINGS&limit=40")
    datasets = pull(f"{HF}/datasets?author=SZLHOLDINGS&limit=30")
    def ids(blob):
        if isinstance(blob, list):
            return [x.get("id") for x in blob if isinstance(x, dict)]
        return blob
    return json.dumps({"models": ids(models), "spaces": ids(spaces), "datasets": ids(datasets)}, indent=2)[:12000]


def run_ask(prompt, lock, prev):
    if not (prompt or "").strip():
        return "Empty submission.", "{}"
    if not lock:
        rec = mint("brief", "BLOCKED", "MEASURED", prev, prompt, None)
        return "BLOCKED — Human Lock required (fail-closed).", json.dumps(rec, indent=2)
    text, honesty = grok(prompt, DISCLAIMER + " You are Ayllu Counsel. Not a licensed attorney. No fabricated citations.")
    rec = mint("brief", "ALLOW", honesty, prev, prompt, MODEL if honesty != "UNAVAILABLE" else None)
    return text, json.dumps(rec, indent=2)


with gr.Blocks(title="Ayllu Counsel") as demo:
    gr.Markdown("# Ayllu Counsel\nLegal Matter Command. Continuance of Counsel — not a deletion. " + DISCLAIMER)
    with gr.Tab("Docket"):
        out_d = gr.Code(label="Live a-11-oy.com legal vertical")
        gr.Button("Scrape docket").click(show_docket, outputs=out_d)
    with gr.Tab("Estate"):
        out_e = gr.Code(label="Live SZLHOLDINGS Hub")
        gr.Button("Scrape Hub").click(show_estate, outputs=out_e)
    with gr.Tab("Infer"):
        prompt = gr.Textbox(label="Matter / question", lines=6)
        lock = gr.Checkbox(label="Human Lock", value=False)
        prev = gr.Textbox(label="prev_hash", value=GENESIS)
        ans = gr.Textbox(label="Completion", lines=12)
        rec = gr.Code(label="Receipt")
        gr.Button("Run grok-4.5").click(run_ask, inputs=[prompt, lock, prev], outputs=[ans, rec])

if __name__ == "__main__":
    demo.launch()
