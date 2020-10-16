def add_bin(probs_to_bin, rel_idx, idx, bin):
    for i in range(rel_idx, idx):
        if i in probs_to_bin:
            probs_to_bin[i] += bin

def separate(values, probs_to_bin, rel_idx=0):
    if len(values) == 1:
        return
    idx_to_diff = {}
    for a in range(1, len(values)):
        s1 = sum(values[:a])
        s2 = sum(values[a:])
        idx_to_diff[a] = abs(s1-s2)
    idx = sorted(idx_to_diff.items(), key=lambda item: item[1])[0][0] + rel_idx

    add_bin(probs_to_bin, rel_idx, idx, '0')
    add_bin(probs_to_bin, idx, len(values) + rel_idx, '1')
    
    separate(values[:idx - rel_idx], probs_to_bin, rel_idx)
    separate(values[idx - rel_idx:], probs_to_bin, idx)
