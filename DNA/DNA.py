from utils import test_solution


def count_dna_nucleotides(filename: str) -> tuple[int]:
    with open(filename) as f:
        s = f.read()
    return (s.count('A'), s.count('C'), s.count('G'), s.count('T'))


if __name__ == '__main__':
    test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    test_output = (20, 12, 17, 21)
    test_solution(count_dna_nucleotides, test_input, test_output)
