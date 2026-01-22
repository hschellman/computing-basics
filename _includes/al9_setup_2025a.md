~~~
# find a spack environment and set it up
# setup spack  (pre spack 1.0 version)

# this is for spack v1.0
source /cvmfs/dune.opensciencegrid.org/spack/v1.0/share/spack/setup-env.sh
echo "Activate dune-workflow"
spack env activate dune-workflow
echo "load GCC"
echo "GCC"
spack load gcc@12.5.0 arch=linux-almalinux9-x86_64_v2 

echo "PY-PIP"                       
spack load py-pip@23.1.2%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

~~~
{: .language-bash}

You can check your environment by doing this

~~~
# test-paths.sh
echo "which root"
which root
root --version
echo "which gcc"
which gcc
gcc --version
echo "which python"
which python
python --version
echo "which cmake"
which cmake
cmake --version
~~~
{: .language-bash}
