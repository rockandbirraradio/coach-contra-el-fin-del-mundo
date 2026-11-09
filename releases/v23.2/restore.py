#!/usr/bin/env python3
"""Reconstruir exactamente el HTML V23.2 de 20 misiones desde GitHub."""
from pathlib import Path
import hashlib

base = Path(__file__).resolve().parent
parts = sorted((base / "parts").glob("part-*.txt"))
if len(parts) != 14:
    raise SystemExit(f"Respaldo incompleto: se esperaban 14 partes; encontradas {len(parts)}")
source = b"".join(part.read_bytes() for part in parts)
expected_size = 4700641
expected_hash = "4cfbb274eda0a4d71da456b924b56354579299ee2252fbb521f5cd8671bd3a4e"
actual_hash = hashlib.sha256(source).hexdigest()
if len(source) != expected_size or actual_hash != expected_hash:
    raise SystemExit(f"Integridad fallida: {len(source)} bytes, SHA-256 {actual_hash}")
target = base / "Coach_20_Misiones_V23_2_Estabilizacion.html"
target.write_bytes(source)
print(f"RESPALDO RECUPERADO: {target} ({len(source)} bytes), SHA-256 correcto")
