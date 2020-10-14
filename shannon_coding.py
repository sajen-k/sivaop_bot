import utils
from formulas import *

def shannon_coding(probabilities):
    answer = {}
    answer['idx_to_bin'] = {}
    probabilities.sort(reverse=True)
    for i in range(len(probabilities)):
        answer['idx_to_bin'][i] = ''
    utils.separate(probabilities, answer['idx_to_bin'])

    answer['idx_to_len'] = {k: len(v) for k,v in answer['idx_to_bin'].items()}

    answer['H'] = entropy(probabilities)
    answer['lavg'] = Lavg(probabilities=probabilities, lengths=answer['idx_to_len'].values())
    answer['eff'] = efficiency(answer['H'], answer['lavg'])
    answer['red'] = redundancy(answer['eff'])
    answer['cv'] = code_variance(probs=probabilities, lengths=answer['idx_to_len'].values(), lavg=answer['lavg'])

    return answer
    
if __name__ == '__main__':
    probs = input("Enter probabilities: ")
    probs = list(map(float, probs.split()))
    answer = shannon_coding(probs)
    for prob, bin, length in zip(probs, answer['idx_to_bin'].values(), answer['idx_to_len'].values()):
        print(prob, '\t', bin, '\t', length)
    print("Entropy:", answer['H'])
    print("Average length:", answer['lavg'])
    print("Efficiency:", answer['eff'])
    print("Redundancy:", answer['red'])
    print("Code Variance:", answer['cv'])