from formulas import *
from shannon_coding import shannon
from huffman_coding import huffman

def solve(args, coding):
    try:
        probs = sorted(list(map(float, args.split())), reverse=True)
    except Exception as e:
        return e
    
    answer = coding(probs)

    if isinstance(answer, str): return answer

    answer['idx_to_len'] = {k: len(v) for k,v in answer['idx_to_bin'].items()}
    answer['Entropy'] = entropy(probs)
    answer['Average length'] = Lavg(probabilities=probs, lengths=answer['idx_to_len'].values())
    answer['Efficiency'], answer['Redundancy'] = efficiency_redundancy(answer['Entropy'], answer['Average length'])
    answer['Code Variance'] = code_variance(probs=probs, lengths=answer['idx_to_len'].values(), lavg=answer['Average length'])

    result = ''

    for prob, bin, length in zip(probs, answer['idx_to_bin'].values(), answer['idx_to_len'].values()):
        result += '\n' + str(prob) + '\t' + bin + '\t' + str(length)

    for k, v in answer.items():
        result += ('\n' + k + ':' + str(v)) if k not in ['idx_to_bin', 'idx_to_len'] else ''

    return result

functions = {'shannon': shannon, 'huffman': huffman}

if __name__ == '__main__':
    args = input("Enter probabilities: ")
    coding = input("Enter coding: ")

    if coding not in ['shannon', 'huffman', 'lz']:
        print("Invalid coding.")

    result = solve(args, functions[coding])
    print(result)