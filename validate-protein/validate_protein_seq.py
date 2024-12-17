from Bio import SeqIO
from Bio.Seq import Seq
from pathlib import Path
import sys
import argparse

def is_valid_protein(sequence):
    """
    Validates if a sequence is a protein sequence.
    Allows for up to 2 ambiguous characters to account for X, * etc.
    """
    amino_acids = set("ACDEFGHIKLMNPQRSTVWY")
    seq_set = set(sequence.upper())
    return len(seq_set - amino_acids) <= 2

def validate_fasta(input_file, output_dir):
    """
    Validates protein sequences and writes to output files during processing.
    Returns count of valid and invalid sequences.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    valid_file = output_dir / "valid_sequences.fasta"
    invalid_file = output_dir / "invalid_sequences.fasta"
    
    valid_count = 0
    invalid_count = 0
    processed_count = 0
    
    print(f"Starting validation of {input_file}...")
    print("Writing results to files as sequences are processed...")
    
    with open(valid_file, 'w') as valid_handle, open(invalid_file, 'w') as invalid_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            processed_count += 1
            if processed_count % 1000 == 0:  # Print status every 1000 sequences
                print(f"Processed {processed_count} sequences...")
            
            if is_valid_protein(str(record.seq)):
                SeqIO.write(record, valid_handle, "fasta")
                valid_count += 1
            else:
                SeqIO.write(record, invalid_handle, "fasta")
                invalid_count += 1
    
    return valid_count, invalid_count

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Validate protein sequences in a FASTA file.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Add command line arguments
    parser.add_argument('--input', 
                       required=True,
                       help='Input FASTA file path')
    parser.add_argument('--output',
                       required=True,
                       help='Output directory path')
    
    # Parse arguments
    args = parser.parse_args()
    
    valid_count, invalid_count = validate_fasta(args.input, args.output)
    
    print("\nValidation Complete!")
    print(f"Total valid sequences: {valid_count}")
    print(f"Total invalid sequences: {invalid_count}")
    print(f"Results written to {args.output}/valid_sequences.fasta and {args.output}/invalid_sequences.fasta")

if __name__ == "__main__":
    main()
