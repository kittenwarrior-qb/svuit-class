"""Validate local study materials and independently check lab outcomes.

Run from any working directory with Python 3.8+. No third-party packages.
External URLs are not requested by this checker.
"""
from fractions import Fraction
import importlib.util
from pathlib import Path
import re
import sqlite3
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_links():
    errors, links = [], 0
    markdown = list(ROOT.rglob("*.md"))
    for path in markdown:
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0].strip("<>"))
            links += 1
            if not (path.parent / relative).exists():
                errors.append("{}: {}".format(path.relative_to(ROOT), target))
        if content.count("```") % 2:
            errors.append("Unbalanced code fence: {}".format(path.relative_to(ROOT)))
    assert not errors, "\n".join(errors)
    print("PASS: {} Markdown files, {} local links, code fences".format(len(markdown), links))


def check_subnets():
    subnet = load("subnet_lab", "IE101-co-so-ha-tang-cntt/thuc-hanh/subnet.py")
    result = subnet.describe("192.168.10.70/26")
    assert result["network"] == "192.168.10.64/26"
    assert result["broadcast"] == "192.168.10.127"
    assert (result["first_host"], result["last_host"], result["host_count"]) == (
        "192.168.10.65", "192.168.10.126", 62)
    assert subnet.describe("10.0.0.0/31")["host_count"] == 2
    assert subnet.describe("10.0.0.1/32")["host_count"] == 1
    assert subnet.describe("0.0.0.0/0")["host_count"] == 2 ** 32 - 2
    try:
        subnet.describe("not-an-ip")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid IP was accepted")
    print("PASS: subnet boundaries and invalid input")


def check_sql():
    lab = load("sql_lab", "IE103-quan-ly-thong-tin/thuc-hanh/lab_sql.py")
    lab.run_lab()
    connection = lab.build_database()
    try:
        for statement, parameters in [
            ("INSERT INTO loans VALUES (?, ?, ?, ?, ?)", (10, 999, "B04", "2025-10-08", None)),
            ("UPDATE loans SET returned_on = NULL WHERE loan_id = ?", (1,)),
            ("INSERT INTO loans VALUES (?, ?, ?, ?, ?)", (11, 1, "B04", "2025-10-08", "2025-10-01")),
        ]:
            try:
                connection.execute(statement, parameters)
            except sqlite3.IntegrityError:
                connection.rollback()
            else:
                raise AssertionError("Invalid SQL write was accepted: " + statement)
        # Returning a book allows it to be borrowed again without a conflict.
        connection.execute("UPDATE loans SET returned_on = ? WHERE loan_id = ?", ("2025-10-08", 3))
        connection.execute("INSERT INTO loans VALUES (?, ?, ?, ?, ?)", (12, 4, "B01", "2025-10-09", None))
        assert connection.execute("SELECT COUNT(*) FROM open_loans").fetchone() == (3,)
        print("PASS: foreign key, update trigger, date order, return/reborrow")
    finally:
        connection.close()


def check_os():
    oslab = load("os_lab", "IT007-he-dieu-hanh/thuc-hanh/mo_phong.py")
    gantt, metrics = oslab.fcfs([("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 1)])
    assert gantt == [("P1", 0, 5), ("P2", 5, 8), ("P3", 8, 9)]
    assert [metrics[p]["WT"] for p in ("P1", "P2", "P3")] == [0, 4, 6]
    assert oslab.fcfs([("P", 4, 2)])[0] == [("idle", 0, 4), ("P", 4, 6)]
    gantt, metrics = oslab.round_robin_zero_arrival([("P1", 5), ("P2", 3), ("P3", 1)], 2)
    assert gantt == [("P1", 0, 2), ("P2", 2, 4), ("P3", 4, 5),
                     ("P1", 5, 7), ("P2", 7, 8), ("P1", 8, 9)]
    assert [metrics[p]["WT"] for p in ("P1", "P2", "P3")] == [4, 5, 4]
    assert oslab.page_replacement([1, 2, 3, 1, 4, 2, 5], 3, "FIFO")[0] == 5
    assert oslab.page_replacement([1, 2, 3, 1, 4, 2, 5], 3, "LRU")[0] == 6
    assert oslab.page_replacement([1, 1, 1], 1, "LRU")[0] == 1
    assert oslab.safe_sequence([1, 1], [[1, 0], [0, 1], [1, 1]],
                               [[2, 1], [1, 2], [2, 2]]) == [0, 1, 2]
    assert oslab.safe_sequence([0], [[1], [1]], [[2], [2]]) is None
    for action in [lambda: oslab.page_replacement([1], 0, "FIFO"),
                   lambda: oslab.round_robin_zero_arrival([("P", 1)], 0),
                   lambda: oslab.safe_sequence([0], [[2]], [[1]])]:
        try:
            action()
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid OS model input accepted")
    print("PASS: FCFS, RR, FIFO, LRU, Banker and boundary cases")


def check_gauss():
    gauss = load("gauss_lab", "MA003-dai-so-tuyen-tinh/thuc-hanh/gauss.py")
    systems = [
        ([[1, 2, 5], [3, 4, 11]], "unique"),
        ([[1, 1, 1, 2], [2, 2, 2, 4]], "infinite"),
        ([[1, 1, 1], [2, 2, 3]], "none"),
        ([[0, 1, 2], [1, 0, 3]], "unique"),
        ([[0, 0, 0], [0, 0, 0]], "infinite"),
        ([[0, 0, 1]], "none"),
        ([[1, 1, 3], [1, -1, 1], [2, 0, 4]], "unique"),
        ([["1/3", 1]], "unique"),
    ]
    for system, status in systems:
        result = gauss.solve(system)
        assert result["status"] == status
        if status == "none":
            continue
        # Verify solutions against original equations, not an expected RREF copy.
        particular = result["particular"]
        assert all(sum(Fraction(a) * x for a, x in zip(row[:-1], particular)) == Fraction(row[-1])
                   for row in system)
        for vector in result["null_basis"]:
            assert all(sum(Fraction(a) * x for a, x in zip(row[:-1], vector)) == 0 for row in system)
        assert len(result["null_basis"]) + result["rank"] == len(system[0]) - 1
    assert gauss.solve(systems[0][0])["particular"] == [1, 2]
    assert gauss.solve([["1/3", 1]])["particular"] == [3]
    print("PASS: Gauss solutions, null space, rank-nullity, row swaps and consistency")


def main():
    check_links()
    check_subnets()
    check_sql()
    check_os()
    check_gauss()
    print("ALL CHECKS PASSED (local links and Python labs only)")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
