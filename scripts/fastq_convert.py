from argparse import ArgumentParser
import sys

from Bio import SeqIO

QUALITY_CONVERSION_TYPES = ["fastq-sanger", "fastq-solexa", "fastq-illumina"]

def main(in_file, in_format, out_format):
    with open(in_file, "r") as in_handle:
        SeqIO.convert(in_handle, in_format, sys.stdout, out_format)

if __name__ == "__main__":
    parser = ArgumentParser(description="simple script for converting "
                            "fastq quality scores.")
    parser.add_argument("--in-format", help="Quality format to convert from.",
                        choices=QUALITY_CONVERSION_TYPES)
    parser.add_argument("--out-format", help="Quality format to convert to.",
                        choices=QUALITY_CONVERSION_TYPES)
    parser.add_argument("in_file", help="FASTQ file to convert.")
    args = parser.parse_args()
    main(args.in_file, args.in_format, args.out_format)
