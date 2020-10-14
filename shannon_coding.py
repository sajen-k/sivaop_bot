import utils
from other_formulas import *

def shannon_coding(probabilities):
    idx_to_bin = {}
    probabilities.sort(reverse=True)
    for i in range(len(probabilities)):
        idx_to_bin[i] = ''
    utils.separate(probabilities, idx_to_bin)

    idx_to_len = {k: len(v) for k,v in idx_to_bin.items()}

    H = entropy(probabilities)
    lavg = Lavg(probabilities=probabilities, lengths=idx_to_len.values())
    eff = efficiency(H, lavg)
    red = redundancy(eff)
    cv = code_variance(probs=probabilities, lengths=idx_to_len.values(), lavg=lavg)

    return idx_to_bin, idx_to_len, H, lavg, eff, red, cv
    
if __name__ == '__main__':
    probs = input("Enter probabilities: ")
    probs = list(map(float, probs.split()))
    idx_to_bin, idx_to_len, H, lavg, eff, red, cv = shannon_coding(probs)
    for prob, bin, length in zip(probs, idx_to_bin.values(), idx_to_len.values()):
        print(prob, '\t', bin, '\t', length) 
    print("Entropy:", H)
    print("Average length:", lavg)
    print("Efficiency:", eff)
    print("Redundancy:", red)
    print("Code Variance:", cv)