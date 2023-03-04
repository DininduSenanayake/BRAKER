wd=test2

if [ -d $wd ]; then
    rm -r $wd
fi

# The expected runtime of this test is ~3 minutes.

# --gm_max_intergenic 10000 option is used here only to make the test run faster.
# It is not recommended to use this option in real BRAKER runs. The speed increase
# achieved by adjusting this option is negligible on full-sized genomes.

# For instructions on how to prepare the proteins.fa input file from OrthoDB,
# see https://github.com/gatech-genemark/ProtHint#protein-database-preparation

export GENEMARK_PATH=$GENEMARK_PATH/gmes

( time braker.pl --genome=/opt/BRAKER/example/genome.fa --prot_seq=/opt/BRAKER/example/proteins.fa --workingdir=$wd --threads=8 --gm_max_intergenic 10000 --skipOptimize ) &> test2.log
