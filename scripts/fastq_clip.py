from argparse import ArgumentParser
import sys
from itertools import ifilter

from Bio import SeqIO

QUALITY_CONVERSION_TYPES = ["fastq-sanger", "fastq-solexa", "fastq-illumina"]

def is_long_enough(read_length):
    def too_small(record):
        return len(str(record.seq)) > read_length
    return too_small

def trim_records(records, read_length):
    for record in records:
        yield record[0:read_length]

def main(in_file, in_format, read_length):

    with open(in_file, "r") as in_handle:
        parser = SeqIO.parse(in_handle, in_format)
        too_small = ifilter(is_long_enough(read_length), parser)
        SeqIO.write(trim_records(too_small, read_length), sys.stdout, in_format)

if __name__ == "__main__":
    parser = ArgumentParser(description="simple script for converting "
                            "fastq quality scores.")
    parser.add_argument("--read-length", type=int, help="Length to clip reads to.")
    parser.add_argument("--in-format", help="Quality format of fastq-file.",
                        default="fastq-sanger",
                        choices=QUALITY_CONVERSION_TYPES)
    parser.add_argument("in_file", help="FASTQ file to clip.")
    args = parser.parse_args()
    main(args.in_file, args.in_format, args.read_length)
