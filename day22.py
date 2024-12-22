# fast p1, slow p2 with extremely disgraceful code. original brute force was abhorrent and ran for 25 minutes, this has been refactored to be clean and run in 5 seconds.
d = open("day22input.txt").read().strip()
l = d.split("\n")
op, op2 = 0, 0
freqs = {}


def mix_prune(num, mix, prune):
    return (num ^ mix) % prune


for line in l:
    seen = set()
    num = int(line)
    seq = []

    for _ in range(2000):
        seq.append(num % 10)
        num = mix_prune(num, num*64, 16777216)
        num = mix_prune(num, num//32, 16777216)
        num = mix_prune(num, num*2048, 16777216)
    op += num

    for i in range(1, len(seq)-3):
        pattern = (seq[i]-seq[i-1], seq[i+1]-seq[i],
                   seq[i+2]-seq[i+1], seq[i+3]-seq[i+2])

        if pattern not in seen:
            seen.add(pattern)

            if pattern in freqs:
                freqs[pattern] += seq[i+3]
            else:
                freqs[pattern] = seq[i+3]

op2 = max(freqs.values())

print(op)
print(op2)
