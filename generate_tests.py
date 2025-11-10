import json
from pathlib import Path

JSON_PATH = Path("new_data.json")
TESTS_DIR = Path("tests/llama3_SelfDebug")
SRC_PACKAGE = "outputs.llama3_SelfDebug"  # folder name containing your solution files

if not JSON_PATH.exists():
    raise SystemExit(f"{JSON_PATH} not found. Place your benchmark JSON there.")

TESTS_DIR.mkdir(exist_ok=True)

data = json.loads(JSON_PATH.read_text())

for entry in data:
    fid = entry.get("id")
    prompt = entry.get("prompt", "")
    tests_snippet = entry.get("tests", "")
    if not fid:
        print("Skipping entry with no id")
        continue

    test_file = TESTS_DIR / f"test_{fid}.py"

    # Attempt to detect the function name from the prompt
    func_name = None
    for line in prompt.splitlines():
        line = line.strip()
        if line.startswith("def "):
            func_name = line.split()[1].split("(")[0]
            break
    if not func_name:
        func_name = fid

    # Split asserts by line, ignore empty lines
    assert_lines = [line.strip() for line in tests_snippet.splitlines() if line.strip()]

    # Build pytest functions
    test_functions = ""
    for i, assert_line in enumerate(assert_lines, start=1):
        test_functions += f"""
def test_{func_name}_{i}():
    {assert_line}
"""

    # Prepare full content
    content = f"""# Auto-generated pytest tests for {fid}
import importlib
mod = importlib.import_module('{SRC_PACKAGE}.{fid}')
from {SRC_PACKAGE}.{fid} import {func_name}

{test_functions}
"""

    # Write file
    test_file.write_text(content)
    print(f"Generated {test_file}")
