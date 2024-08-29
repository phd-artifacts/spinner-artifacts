virtualenv .venv
source .venv/bin/activate
pip3 install git+https://github.com/LSC-Unicamp/spinner

singularity pull docker://docker.io/ompcluster/runtime-dev
mv runtime-dev_latest.sif ./ompc-tb