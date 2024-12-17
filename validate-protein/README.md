## How to run this script 


```bash
python3 2-validate.py --input INPUT_FILE --output OUTPUT_DIRECTORY
```

**Output:**

1. Creates two separate FASTA files:
   - `valid_sequences.fasta` for protein sequences that passed validation
   - `invalid_sequences.fasta` for sequences that failed

2. Provides a summary of validation results. For an example

```bash
Validation Complete!
Total valid sequences: 5583883
Total invalid sequences: 38
Results written to valid_sequences.fasta and invalid_sequences.fasta
```
**Note on .faa vs .fasta**

BioPython's `SeqIO.parse()` function handles both formats identically since they follow the same FASTA format specification:

1. A header line starting with '>' followed by the sequence identifier
2. The actual sequence data in the following lines
