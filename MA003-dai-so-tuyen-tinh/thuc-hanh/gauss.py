"""Exact Gauss-Jordan elimination for a rational augmented matrix.

Accept integers, Fraction objects or rational strings such as '1/3'.
The final column is the RHS. Not intended for large numerical workloads.
"""
from fractions import Fraction


def solve(augmented):
    if not augmented or len(augmented[0]) < 2:
        raise ValueError("Need at least one equation and one unknown")
    width = len(augmented[0])
    if any(len(row) != width for row in augmented):
        raise ValueError("Rows must have equal lengths")
    matrix = [[Fraction(value) for value in row] for row in augmented]
    variables, pivot_row, pivot_cols = width - 1, 0, []
    for column in range(variables):
        candidate = next((r for r in range(pivot_row, len(matrix)) if matrix[r][column]), None)
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        divisor = matrix[pivot_row][column]
        matrix[pivot_row] = [value / divisor for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row != pivot_row:
                factor = matrix[row][column]
                matrix[row] = [v - factor * p for v, p in zip(matrix[row], matrix[pivot_row])]
        pivot_cols.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    inconsistent = any(all(value == 0 for value in row[:-1]) and row[-1] != 0 for row in matrix)
    free_cols = [c for c in range(variables) if c not in pivot_cols]
    result = {"rref": matrix, "rank": len(pivot_cols), "pivots": pivot_cols,
              "free_columns": free_cols, "status": "none" if inconsistent else
              ("infinite" if free_cols else "unique"), "particular": None, "null_basis": []}
    if inconsistent:
        return result
    particular = [Fraction(0) for _ in range(variables)]
    for row, column in enumerate(pivot_cols):
        particular[column] = matrix[row][-1]
    basis = []
    for free in free_cols:
        vector = [Fraction(0) for _ in range(variables)]
        vector[free] = Fraction(1)
        for row, column in enumerate(pivot_cols):
            vector[column] = -matrix[row][free]
        basis.append(vector)
    result.update(particular=particular, null_basis=basis)
    return result


def display(result):
    print("status:", result["status"], "rank:", result["rank"])
    for row in result["rref"]:
        print("[" + ", ".join(str(v) for v in row) + "]")
    if result["particular"] is not None:
        print("particular:", [str(v) for v in result["particular"]])
        print("null basis:", [[str(v) for v in row] for row in result["null_basis"]])


if __name__ == "__main__":
    for name, system in [
        ("unique", [[1, 2, 5], [3, 4, 11]]),
        ("infinite", [[1, 1, 1, 2], [2, 2, 2, 4]]),
        ("none", [[1, 1, 1], [2, 2, 3]]),
    ]:
        print("\nExample:", name)
        display(solve(system))
