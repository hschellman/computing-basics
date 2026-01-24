~~~
# find a spack environment and set it up
# setup spack  (pre spack 1.0 version)

# this is for spack v1.0/devel - tutorial

echo "setup-tutorial.sh"
. /cvmfs/dune.opensciencegrid.org/dune-spack/spack-develop-fermi/setup-env.sh
spack env activate dune-tutorial
echo "Activate dune-tutorial"

echo "load GCC and CMAKE so don't use system"
echo "GCC"
spack load gcc@12.5.0 arch=linux-almalinux9-x86_64_v2 
echo "CMAKE"
spack load cmake 
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
