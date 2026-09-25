# Build a Data Graph Explorer - FCC College Algebra with Python
import csv
import io

SAMPLE_CSV = """name,age,salary
Alice,30,52000
Bob,45,61000
Carol,25,48000
Dave,38,57500
"""

def load_csv(text):
    rows = list(csv.DictReader(io.StringIO(text)))
    return rows

def column_stats(rows, col):
    vals = [float(r[col]) for r in rows]
    n = len(vals)
    mean = sum(vals) / n
    srt = sorted(vals)
    median = srt[n//2] if n % 2 else (srt[n//2-1] + srt[n//2]) / 2
    return {'min': min(vals), 'max': max(vals), 'mean': round(mean, 2), 'median': median}

def ascii_bar_chart(rows, col, width=40):
    vals = [float(r[col]) for r in rows]
    mx = max(vals)
    lines = []
    for r, v in zip(rows, vals):
        bar = '#' * int(v / mx * width)
        lines.append(f"{r['name']:<8}|{bar} {v:g}")
    return chr(10).join(lines)

if __name__ == '__main__':
    rows = load_csv(SAMPLE_CSV)
    print(column_stats(rows, 'salary'))
    print(ascii_bar_chart(rows, 'salary'))
