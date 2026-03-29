#!/usr/bin/env python3
"""bitwise_calc - Bitwise operations."""
import sys, argparse, json

def main():
    p = argparse.ArgumentParser(description="Bitwise calculator")
    p.add_argument("a", help="First operand (dec/hex/bin)")
    p.add_argument("op", choices=["and","or","xor","not","lshift","rshift","nand","nor"])
    p.add_argument("b", nargs="?", help="Second operand")
    args = p.parse_args()
    def parse_int(s):
        if s.startswith("0x"): return int(s, 16)
        if s.startswith("0b"): return int(s, 2)
        return int(s)
    a = parse_int(args.a)
    b = parse_int(args.b) if args.b else 0
    ops = {"and": a&b, "or": a|b, "xor": a^b, "not": ~a, "lshift": a<<b, "rshift": a>>b, "nand": ~(a&b), "nor": ~(a|b)}
    r = ops[args.op]
    print(json.dumps({"a": a, "op": args.op, "b": b, "result": r, "dec": r, "hex": hex(r), "bin": bin(r), "oct": oct(r)}))

if __name__ == "__main__": main()
