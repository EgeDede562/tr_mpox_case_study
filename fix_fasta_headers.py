from Bio import SeqIO
import os

def update_headers(fasta_file):
    # Get the desired header from the file name
    desired_header = os.path.basename(fasta_file).split('.')[0]

    # Read the FASTA file
    records = list(SeqIO.parse(fasta_file, "fasta"))

    # Update the header
    for record in records:
        record.id = desired_header
        record.description = ''

    # Write the updated records back to the file
    with open(fasta_file, "w") as output_handle:
        SeqIO.write(records, output_handle, "fasta")

def main():
    fasta_files = [f for f in os.listdir('.') if f.endswith('.fasta')]
    for fasta_file in fasta_files:
        update_headers(fasta_file)

if __name__ == "__main__":
    main()
