# tests/test_smoke.py
import importlib.util
from pathlib import Path

def test_anchor_imports():
    assert Path("anchor_v1.py").exists()
    spec = importlib.util.spec_from_file_location("anchor", "anchor_v1.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # should not raise
