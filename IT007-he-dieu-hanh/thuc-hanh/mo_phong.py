"""Small deterministic OS models; not a real operating-system scheduler."""
from collections import deque


def fcfs(processes):
    """Processes: (name, arrival, burst), input order breaks arrival ties."""
    if any(arrival < 0 or burst <= 0 for _, arrival, burst in processes):
        raise ValueError("Arrival must be nonnegative; burst must be positive")
    if len({p[0] for p in processes}) != len(processes):
        raise ValueError("Process names must be unique")
    time, gantt, metrics = 0, [], {}
    for _, (name, arrival, burst) in sorted(enumerate(processes), key=lambda item: (item[1][1], item[0])):
        if time < arrival:
            gantt.append(("idle", time, arrival))
            time = arrival
        start = time
        time += burst
        gantt.append((name, start, time))
        metrics[name] = {"CT": time, "TAT": time - arrival,
                         "WT": start - arrival, "RT": start - arrival}
    return gantt, metrics


def round_robin_zero_arrival(processes, quantum):
    """Only AT=0 for all processes; queue follows input order; overhead=0."""
    if quantum <= 0 or any(burst <= 0 for _, burst in processes):
        raise ValueError("Quantum and burst must be positive")
    if len({p[0] for p in processes}) != len(processes):
        raise ValueError("Process names must be unique")
    queue = deque(processes)
    time, gantt, completion, first = 0, [], {}, {}
    while queue:
        name, remaining = queue.popleft()
        first.setdefault(name, time)
        duration = min(quantum, remaining)
        gantt.append((name, time, time + duration))
        time += duration
        remaining -= duration
        if remaining:
            queue.append((name, remaining))
        else:
            completion[name] = time
    metrics = {name: {"CT": completion[name], "TAT": completion[name],
                      "WT": completion[name] - burst, "RT": first[name]}
               for name, burst in processes}
    return gantt, metrics


def page_replacement(sequence, frames, policy):
    if frames <= 0 or policy not in ("FIFO", "LRU"):
        raise ValueError("Need positive frames and FIFO or LRU policy")
    resident, order, history, faults = [], deque(), [], 0
    for page in sequence:
        hit = page in resident
        if hit:
            if policy == "LRU":
                order.remove(page)
                order.append(page)
        else:
            faults += 1
            if len(resident) == frames:
                victim = order.popleft()
                resident[resident.index(victim)] = page
            else:
                resident.append(page)
            order.append(page)
        history.append((page, "H" if hit else "F", tuple(resident)))
    return faults, history


def safe_sequence(available, allocation, maximum):
    """Banker safety test. Return one sequence of row indices, or None."""
    width = len(available)
    if len(allocation) != len(maximum):
        raise ValueError("Allocation/maximum row counts differ")
    if any(len(row) != width for row in allocation + maximum):
        raise ValueError("Resource dimensions differ")
    if any(value < 0 for row in [available] + allocation + maximum for value in row):
        raise ValueError("Negative resource count")
    if any(a > m for ar, mr in zip(allocation, maximum) for a, m in zip(ar, mr)):
        raise ValueError("Allocation exceeds maximum")
    need = [[m - a for a, m in zip(ar, mr)] for ar, mr in zip(allocation, maximum)]
    work, finished, sequence = list(available), set(), []
    while len(finished) < len(allocation):
        for index, row in enumerate(need):
            if index not in finished and all(n <= w for n, w in zip(row, work)):
                work = [w + a for w, a in zip(work, allocation[index])]
                finished.add(index)
                sequence.append(index)
                break
        else:
            return None
    return sequence


if __name__ == "__main__":
    print("FCFS:", fcfs([("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 1)]))
    print("RR, AT=0:", round_robin_zero_arrival([("P1", 5), ("P2", 3), ("P3", 1)], 2))
    for mode in ("FIFO", "LRU"):
        faults, history = page_replacement([1, 2, 3, 1, 4, 2, 5], 3, mode)
        print(mode, "faults:", faults)
        for step in history:
            print(step)
    print("Safe sequence:", safe_sequence([1, 1], [[1, 0], [0, 1], [1, 1]],
                                         [[2, 1], [1, 2], [2, 2]]))
