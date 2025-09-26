from streamlit.testing.v1 import AppTest

def test_app_runs():
    at = AppTest.from_file("anchor_v1.py").run()
    assert at is not None
