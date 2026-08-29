"""Ayllu Counsel — stdlib Space. No Gradio.

Continuance of retired Counsel. Legal Matter Command.
SHA3-256 UNSIGNED-honest receipts. Human Lock fail-closed.
Λ = Conjecture 1. Not legal advice.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from allodial import score as allodial_score

GENESIS = "0" * 64
MODEL = "grok-4.5"
A11OY = "https://a-11-oy.com"
HF = "https://huggingface.co/api"
DISCLAIMER = (
    "Informational only. Does not constitute legal advice. Not a law firm. "
    "No attorney-client relationship. Λ = Conjecture 1. SLSA L1. UNSIGNED-honest."
)
HTML = Path(__file__).with_name("index.html")
PREV = {"hash": GENESIS}


def sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def dump(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


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
    PREV["hash"] = body["hash"]
    return body


def pull(url: str, timeout: int = 10):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "szl-counsel/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return json.loads(res.read().decode())
    except Exception as exc:
        return {"_unavailable": str(exc), "url": url, "honesty": "UNAVAILABLE"}


def grok(prompt: str) -> tuple[str, str]:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        return "UNAVAILABLE — XAI_API_KEY absent. Fail closed.", "UNAVAILABLE"
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": DISCLAIMER + " You are Ayllu Counsel. No fabricated citations."},
            {"role": "user", "content": prompt[:6000]},
        ],
        "max_tokens": 480,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as res:
            data = json.loads(res.read().decode())
        return data["choices"][0]["message"]["content"], "CONJECTURE"
    except Exception as exc:
        return f"UNAVAILABLE — {exc}", "UNAVAILABLE"


def read_json(handler: BaseHTTPRequestHandler) -> dict:
    n = int(handler.headers.get("Content-Length") or 0)
    raw = handler.rfile.read(n) if n else b"{}"
    try:
        data = json.loads(raw.decode())
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            html = HTML.read_bytes() if HTML.exists() else b"<h1>Counsel</h1>"
            self._send(200, html, "text/html; charset=utf-8")
            return
        if path in ("/health", "/healthz"):
            self._send(
                200,
                json.dumps(
                    {
                        "ok": True,
                        "organ": "counsel",
                        "lambda_status": "Conjecture 1",
                        "energy": None,
                        "signer": "UNSIGNED-honest",
                    }
                ).encode(),
                "application/json",
            )
            return
        if path == "/api/docket":
            payload = {"health": pull(f"{A11OY}/healthz"), "feed": pull(f"{A11OY}/api/a11oy/v1/vert/legal/feed?limit=8"), "disclaimer": DISCLAIMER}
            self._send(200, json.dumps(payload).encode(), "application/json")
            return
        if path == "/api/estate":
            models = pull(f"{HF}/models?author=SZLHOLDINGS&limit=40")
            spaces = pull(f"{HF}/spaces?author=SZLHOLDINGS&limit=40")
            def ids(blob):
                return [x.get("id") for x in blob if isinstance(x, dict)] if isinstance(blob, list) else blob
            self._send(200, json.dumps({"models": ids(models), "spaces": ids(spaces)}).encode(), "application/json")
            return
        if path == "/api/allodial":
            self._send(200, json.dumps(allodial_score()).encode(), "application/json")
            return
        self._send(404, b'{"error":"not found"}', "application/json")

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        data = read_json(self)
        if path == "/api/brief":
            prompt = str(data.get("prompt") or "").strip()
            lock = bool(data.get("lock"))
            prev = str(data.get("prev") or PREV["hash"])
            if not prompt:
                rec = mint("brief", "BLOCKED", "MEASURED", prev, prompt, None)
                self._send(400, json.dumps({"text": "Empty submission.", "receipt": rec}).encode(), "application/json")
                return
            if not lock:
                rec = mint("brief", "BLOCKED", "MEASURED", prev, prompt, None)
                self._send(200, json.dumps({"text": "BLOCKED — Human Lock required (fail-closed).", "receipt": rec}).encode(), "application/json")
                return
            text, honesty = grok(prompt)
            rec = mint("brief", "ALLOW", honesty, prev, prompt, MODEL if honesty != "UNAVAILABLE" else None)
            self._send(200, json.dumps({"text": text, "receipt": rec}).encode(), "application/json")
            return
        self._send(404, b'{"error":"not found"}', "application/json")


def main() -> None:
    port = int(os.environ.get("PORT", "7860"))
    httpd = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"counsel listening 0.0.0.0:{port}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
