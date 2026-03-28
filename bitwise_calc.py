#!/usr/bin/env python3
"""bitwise_calc - Bitwise operations and binary visualization."""
import sys

def show(val, label=''):
    if label: print(f"{label}:")
    print(f"  Dec: {val}")
    print(f"  Hex: 0x{val:x}")
    print(f"  Oct: 0o{val:o}")
    print(f"  Bin: 0b{val:b}")
    bits = f"{val:b}"
    print(f"  Bits set: {bits.count('1')}/{len(bits)}")

def parse_val(s):
    s = s.strip()
    if s.startswith('0b'): return int(s, 2)
    if s.startswith('0x'): return int(s, 16)
    if s.startswith('0o'): return int(s, 8)
    return int(s)

OPS = {'and':'&','or':'|','xor':'^','not':'~','lshift':'<<','rshift':'>>','nand':'~&'}

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: bitwise_calc.py <val> [OP val]\n  bitwise_calc.py 0xFF and 0x0F\n  bitwise_calc.py not 42\n  bitwise_calc.py 255"); return
    if args[0] == 'not':
        v = parse_val(args[1])
        show(v, 'Input'); show(~v & ((1 << v.bit_length()) - 1), 'NOT')
    elif len(args) == 1:
        show(parse_val(args[0]))
    elif len(args) >= 3:
        a, op, b = parse_val(args[0]), args[1].lower(), parse_val(args[2])
        show(a, 'A'); show(b, 'B')
        if op in ('and','&'): r = a & b
        elif op in ('or','|'): r = a | b
        elif op in ('xor','^'): r = a ^ b
        elif op in ('lshift','<<','shl'): r = a << b
        elif op in ('rshift','>>','shr'): r = a >> b
        else: print(f"Unknown op: {op}"); return
        show(r, f'A {op} B')

if __name__ == '__main__': main()
