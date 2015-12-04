# Gold (trimmed) Flowcell for pipeline testing #

Highly trimmed Illumina flowcell, for testing purposes. The (partial) reads from the `.bcls` come from an
Illumina X10 test quality run at the Wolfson Wohl Cancer Research Centre (mainly PhiX and NA12878).

bcl2fastq should be run with all `ignore` flags activated for a successful conversion:

```
bcl2fastq --ignore-missing-bcls --ignore-missing-filter --ignore-missing-positions --ignore-missing-controls
```

Prior art (from older sequencing machines) can be found in the Picard `testdata`, although this flowcell 
contains more metadata that could be useful:

https://github.com/broadinstitute/picard/tree/master/testdata/picard/illumina/125T125T/Data/Intensities/BaseCalls/L001

Please contact Roman Valls Guimera (`brainstorm at nopcode org`) for further information.
