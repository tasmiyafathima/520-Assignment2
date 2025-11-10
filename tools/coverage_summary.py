import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

# Paths to reports
# change the paths accordingly
JUNIT_XML = Path("reports_part2/junit_all_iteration_0.xml")
COV_XML = Path("reports_part2/coverage_all_iteration_0.xml")

# =========================
# Step 1: Parse JUnit XML
# =========================
tests_summary = defaultdict(lambda: [0, 0])  # module_name -> [passed, total]

if JUNIT_XML.exists():
    tree = ET.parse(JUNIT_XML)
    root = tree.getroot()

    for testcase in root.findall(".//testcase"):
        classname = testcase.attrib.get("classname", "")
        module_name = classname.split(".")[-1]  # e.g., test_binary_search
        tests_summary[module_name][1] += 1      # total tests
        if not testcase.findall("failure") and not testcase.findall("error"):
            tests_summary[module_name][0] += 1  # passed tests
else:
    print(f"⚠ {JUNIT_XML} not found. Tests summary will be empty.")

# =========================
# Step 2: Parse Coverage XML
# =========================
coverage_summary = {}
if COV_XML.exists():
    tree = ET.parse(COV_XML)
    root = tree.getroot()
    for pkg in root.findall(".//package"):
        for cls in pkg.findall("classes/class"):
            module_name = cls.attrib["filename"].replace("/", ".").replace(".py", "")
            lines_covered = float(cls.attrib.get("line-rate", 0)) * 100
            branches = float(cls.attrib.get("branch-rate", 0)) * 100 if "branch-rate" in cls.attrib else None
            coverage_summary[module_name] = (lines_covered, branches)
else:
    print(f"⚠ {COV_XML} not found. Coverage summary will be empty.")

# =========================
# Step 3: Print formatted table
# =========================
header = f"{'Program':<35} {'Tests Passed':<15} {'Line %':<10} {'Branch %':<10} {'Note'}"
separator = "-" * len(header)
print("\n")
# change the header accordingly
print("********* Baseline Coverage Summary for Iteration 3 ***********")
print("\n")
print(header)
print(separator)

for module, (line_pct, branch_pct) in sorted(coverage_summary.items()):
    test_name = module.split(".")[-1]
    passed, total = tests_summary.get(f"test_{test_name}", (0,0))

    # -------------------------
    # Line coverage note
    # -------------------------
    if line_pct >= 90:
        line_note = "Excellent"
    elif line_pct >= 75:
        line_note = "Good"
    elif line_pct >= 50:
        line_note = "Fair"
    else:
        line_note = "Low"

    # -------------------------
    # Branch coverage note
    # -------------------------
    if branch_pct is not None:
        if branch_pct >= 90:
            branch_note = "Excellent"
        elif branch_pct >= 75:
            branch_note = "Good"
        elif branch_pct >= 50:
            branch_note = "Fair"
        else:
            branch_note = "Low"
    else:
        branch_note = "N/A"

    # -------------------------
    # Recommendations / interpretation
    # -------------------------
    recommendations = []

    # Always add a one-line interpretation
    if line_note == "Excellent":
        recommendations.append("Line coverage is excellent; most code paths tested.")
    elif line_note == "Good":
        recommendations.append("Line coverage is good; minor paths untested.")
    elif line_note == "Fair":
        recommendations.append("Line coverage is fair; significant paths untested.")
    else:
        recommendations.append("Line coverage is low; many paths untested.")

    if branch_pct is not None:
        if branch_note == "Excellent":
            recommendations.append("Branch coverage is excellent; most conditions tested.")
        elif branch_note == "Good":
            recommendations.append("Branch coverage is good; some conditions untested.")
        elif branch_note == "Fair":
            recommendations.append("Branch coverage is fair; many conditions untested.")
        else:
            recommendations.append("Branch coverage is low; many conditions untested.")
    else:
        recommendations.append("Branch coverage not reported.")

    # Suggest adding tests if either < 90%
    if line_pct < 90 or (branch_pct is not None and branch_pct < 90):
        recommendations.append("Consider adding more test cases to improve coverage.")

    note = " | ".join(recommendations)
    branch_str = f"{branch_pct:.1f}" if branch_pct is not None else "N/A"
    print(f"{test_name:<35} {passed}/{total:<15} {line_pct:>7.1f}%   {branch_str:>7}   {note}")
