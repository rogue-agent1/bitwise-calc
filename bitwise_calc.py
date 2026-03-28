#!/usr/bin/env python3
"""Bitwise calculator — operations, bit tricks, visualization."""
import sys

def bits(n, w=None):
    if n < 0: n = n & ((1 << (w or 32)) - 1)
    s = bin(n)[2:]
    if w: s = s.zfill(w)
    return s

def popcount(n): return bin(n).count("1")
def is_power2(n): return n > 0 and (n & (n-1)) == 0
def next_power2(n):
    n -= 1
    for i in range(6): n |= n >> (1 << i)
    return n + 1
def lowest_set(n): return n & (-n)
def clear_lowest(n): return n & (n-1)

def cli():
    if len(sys.argv) < 2:
        print("Usage: bitwise_calc <cmd> <args>"); print("  calc A op B | info N | tricks N"); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "calc":
        a, op, b = int(sys.argv[2],0), sys.argv[3], int(sys.argv[4],0)
        ops = {"and": a&b, "or": a|b, "xor": a^b, "lsh": a<<b, "rsh": a>>b, "nand": ~(a&b), "nor": ~(a|b)}
        r = ops.get(op)
        if r is None: print(f"Unknown op: {op}"); return
        print(f"  {a:>12} = {bits(a, 32)}"); print(f"  {b:>12} = {bits(b, 32)}")
        print(f"  {op:>12} = {bits(r, 32)} = {r}")
    elif cmd == "info":
        n = int(sys.argv[2], 0)
        print(f"Value: {n}"); print(f"Binary: {bits(n)}"); print(f"Hex: {hex(n)}")
        print(f"Popcount: {popcount(n)}"); print(f"Power of 2: {is_power2(n)}")
    elif cmd == "tricks":
        n = int(sys.argv[2], 0)
        print(f"n={n} ({bits(n)})"); print(f"Lowest set bit: {lowest_set(n)} ({bits(lowest_set(n))})")
        print(f"Clear lowest: {clear_lowest(n)} ({bits(clear_lowest(n))})")
        print(f"Next power of 2: {next_power2(n)}"); print(f"Is power of 2: {is_power2(n)}")

if __name__ == "__main__": cli()
