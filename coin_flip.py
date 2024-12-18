import random

tails = 0
heads = 0
total = 100000

for i in range(0,total):
    if random.random()>=0.5:
        heads += 1
    else:
        tails += 1

pct_heads = heads/total
pct_tails = tails/total

print(f"Tails = {tails}, heads = {heads}, total = {total}")
print(f"Percent tails = {pct_tails}, percent heads = {pct_heads}")
