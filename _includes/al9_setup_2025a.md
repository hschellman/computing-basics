~~~
# find a spack environment and set it up
# setup spack  (pre spack 1.0 version)

source /cvmfs/larsoft.opensciencegrid.org/spack-v0.22.0-fermi/setup-env.sh

# get the packages you need to run this - this will become simple in future
echo "ROOT"
spack load root@6.28.12%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3

echo "CMAKE"
spack load cmake@3.27.9%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "GCC"
spack load gcc@12.2.0

echo "Rucio and metacat"
spack load r-m-dd-config experiment=dune lab=fnal.gov
export RUCIO_ACCOUNT=justinreadonly

echo "IFDHC"
spack load ifdhc@2.8.0%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
spack load ifdhc-config@2.6.20%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3


echo "PY-PIP"                       
spack load py-pip@23.1.2%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "no justIN yet"
#spack load justin
~~~
{: .language-bash}