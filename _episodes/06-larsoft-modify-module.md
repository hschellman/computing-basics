---
title: Expert in the Room - LArSoft How to modify a module - in progress
teaching: 15
exercises: 0
questions:
- How do I check out, modify, and build DUNE code?
objectives:  
- How to use mrb.
- Set up your environment.
- Download source code from DUNE's git repository.
- Build it.
- Run an example program.
- Modify the job configuration for the program.
- Modify the example module to make a custom histogram.
- Test the modified module.
- Stretch goal -- run the debugger.
key points:
- DUNE's software stack is built out of a tree of UPS products.
- You don't have to build all of the software to make modifications -- you can check out and build one or more products to achieve your goals.
- You can set up pre-built CVMFS versions of products you aren't developing, and UPS will check version consistency, though it is up to you to request the right versions.
- mrb is the tool DUNE uses to check out software from multiple repositories and build it in a single test release.
- mrb uses git and cmake, though aspects of both are exposed to the user.
---

<!---
#### Session Video

The session will be captured on video a placed here after the workshop for asynchronous study.

#### Live Notes

Participants are encouraged to monitor and utilize the [Livedoc for May. 2023](https://docs.google.com/document/d/19XMQqQ0YV2AtR5OdJJkXoDkuRLWv30BnHY9C5N92uYs/edit?usp=sharing) to ask questions and learn.  For reference, the [Livedoc from Jan. 2023](https://docs.google.com/document/d/1sgRQPQn1OCMEUHAk28bTPhZoySdT5NUSDnW07aL-iQU/edit?usp=sharing) is provided.



## Set up your environment

Note: Pre-recorded microlectures via YouTube links are provided in this lesson, its link preceeding the corresponding text.

[YouTube Lecture Part 1](https://youtu.be/0IQL7PmnWBo): You may need to check your login scripts:  `.bashrc`, `.shrc`, `.profile`, `.login`, etc. for experiment-specific setups for other experiments and even DUNE.  This tutorial assumes you have a "clean" login with minimal or no environment set up.  You can do simple checks to see if you have any NOvA setups in your environment, try:

~~~
  env | grep -i nova
~~~
{: .language-bash}



Other common conflicting environments come from MINERvA and MicroBooNE, but you could have just about anything. You may have to adjust your login scripts to do experiment-specific setup only when logged in to a particular experiment's computers.  Or you can define aliases that run specific setups when requested, but not automatically on login.

-->

## First learn a bit about the MRB system

Link to the [mrb]({{ site.baseurl }}/05.5-mrb) episode

## getting set up

You will need *three* login sessions.  These have different
environments set up.

* Session #1  For editing code (and searching for code)  
* Session #2  For building (compiling) the software  
* Session #3  For running the programs  

## Session 1

Start up session #1, editing code, on one of the dunegpvm*.fnal.gov
interactive nodes.  These scripts have also been tested on the
lxplus.cern.ch interactive nodes. 

> ## Note Remember the Apptainer!  
> see below for special Apptainers for CERN and build machines.
{: .callout}

Create two scripts in your home directory:

`newDev2024Tutorial.sh` should have these contents:

~~~
#!/bin/bash
export DUNELAR_VERSION=v10_00_04d00
export PROTODUNEANA_VERSION=$DUNELAR_VERSION
DUNELAR_QUALIFIER=e26:prof
DIRECTORY=2024tutorial
USERNAME=`whoami`
export WORKDIR=/exp/dune/app/users/${USERNAME}
if [ ! -d "$WORKDIR" ]; then
  export WORKDIR=`echo ~`
fi

source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh

cd ${WORKDIR}
touch ${DIRECTORY}
rm -rf ${DIRECTORY}
mkdir ${DIRECTORY}
cd ${DIRECTORY}
mrb newDev -q ${DUNELAR_QUALIFIER}
source ${WORKDIR}/${DIRECTORY}/localProducts*/setup
mkdir work
cd srcs
mrb g -t ${PROTODUNEANA_VERSION} protoduneana

cd ${MRB_BUILDDIR}
mrbsetenv
mrb i -j16
~~~
{: .language-bash}

and `setup2024Tutorial.sh` should have these contents:

~~~
DIRECTORY=2024tutorial
USERNAME=`whoami`

source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
export WORKDIR=/exp/dune/app/users/${USERNAME}
if [ ! -d "$WORKDIR" ]; then
  export WORKDIR=`echo ~`
fi

cd $WORKDIR/$DIRECTORY
source localProducts*/setup
cd work
setup dunesw $DUNELAR_VERSION -q $DUNELAR_QUALIFIER
mrbslp
~~~
{: .language-bash}

Execute this command to make the first script executable.

~~~
  chmod +x newDev2024Tutorial.sh
~~~
{: .language-bash}

It is not necessary to chmod the setup script.  Problems writing
to your home directory?  Check to see if your Kerberos ticket
has been forwarded. 

~~~
  klist
~~~
{: .language-bash}

## Session 2

Start up session #2 by logging in to one of the build nodes,
`dunebuild01.fnal.gov` or `dunebuild02.fnal.gov`.  They have 16 cores
apiece and the dunegpvm's have only four, so builds run much faster
on them.  If all tutorial users log on to the same one and try
building all at once, the build nodes may become very slow or run
out of memory.  The `lxplus` nodes are generally big enough to build
sufficiently quickly.  The Fermilab build nodes should not be used
to run programs (people need them to build code!)

> ## Note you need a modified container on the build machines and at CERN as they don't mount /pnfs
> This is done to prevent people from running interactive jobs on the dedicated build machines. 
{: .callout}

### FNAL build machines
~~~
# remove /pnfs/ for build machines
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash \
-B /cvmfs,/exp,/nashome,/opt,/run/user,/etc/hostname,/etc/hosts,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}

### CERN
~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash\
-B /cvmfs,/afs,/opt,/run/user,/etc/hostname,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}

### Download source code and build it

On the build node, execute the `newDev` script:

~~~
  ./newDev2024Tutorial.sh
~~~
{: .language-bash}

Note that this script will *delete* the directory planned to store
the source code and built code, and make a new directory, in order
to start clean.  Be careful not to execute this script then if you've
worked on the code some, as this script will wipe it out and start fresh.

This build script will take a few minutes to check code out and compile it.

The `mrb g` command does a `git clone` of the specified repository with an optional tag and destination name.    More information is available [here][dunetpc-wiki] and [here][mrb-reference-guide].

Some comments on the build command

~~~
  mrb i -j16
~~~
{: .language-bash}

The `-j16` says how many concurrent processes to run.  Set the number to no more than the number of cores on the computer you're running it on.  A dunegpvm machine has four cores, and the two build nodes each have 16.  Running more concurrent processes on a computer with a limited number of cores won't make the build finish any faster, but you may run out of memory.  The dunegpvms do not have enough memory to run 16 instances of the C++ compiler at a time, and you may see the word `killed` in your error messages if you ask to run many more concurrent compile processes than the interactive computer can handle.

You can find the number of cores a machine has with

~~~
  cat /proc/cpuinfo
~~~
{: .language-bash}

The `mrb` system builds code in a directory distinct from the source code.  Source code is in `$MRB_SOURCE` and built code is in `$MRB_BUILDDIR`.  If the build succeeds (no error messages, and compiler warnings are treated as errors, and these will stop the build, forcing you to fix the problem), then the built artifacts are put in `$MRB_TOP/localProducts*`.  mrbslp directs ups to search in `$MRB_TOP/localProducts*` first for software and necessary components like `fcl` files.  It is good to separate the build directory from the install directory as a failed build will not prevent you from running the program from the last successful build.  But you have to look at the error messages from the build step before running a program.  If you edited source code, made a mistake, built it unsuccessfully, then running the program may run successfully with the last version which compiled.  You may be wondering why your code changes are having no effect.  You can look in `$MRB_TOP/localProducts*` to see if new code has been added (look for the "lib" directory under the architecture-specific directory of your product).

Because you ran the `newDev2024Tutorial.sh` script instead of sourcing it, the environment it
set up within it is not retained in the login session you ran it from.  You will need to set up your environment again.
You will need to do this when you log in anyway, so it is good to have
that setup script.  In session #2, type this:

~~~
  source setup2024Tutorial.sh
  cd $MRB_BUILDDIR
  mrbsetenv
~~~
{: .language-bash}

The shell command "source" instructs the command interpreter (bash) to read commands from the file `setup2024Tutorial.sh` as if they were typed at the terminal.  This way, environment variables set up by the script stay set up.
Do the following in session #1, the source editing session:

~~~
source setup2024Tutorial.sh
  cd $MRB_SOURCE
  mrbslp
~~~
{: .language-bash}

## Run your program

[YouTube Lecture Part 2](https://youtu.be/8-M2ZV-zNXs): Start up the session for running programs -- log in to a `dunegpvm` interactive 
computer for session #3

~~~
  source setup2024Tutorial.sh
  mrbslp
  setup_fnal_security
~~~
{: .language-bash}

We need to locate an input file.  Here are some tips for finding input data:

[https://wiki.dunescience.org/wiki/Look_at_ProtoDUNE_SP_data][dune-wiki-protodune-sp]

Data and MC files are typically on tape, but can be cached on disk so you don't have to wait possibly a long time for the 
file to be staged in. Check to see if a sample file is in dCache or only on tape:

~~~
cache_state.py PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}

Get the `xrootd` URL:

~~~
samweb get-file-access-url --schema=root PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}

which should print the following URL:

~~~
root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}
  
Now run the program with the input file accessed by that URL:

~~~
lar -c analyzer_job.fcl root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}

CERN Users without access to Fermilab's `dCache`: -- example input files for this tutorial have been copied to `/afs/cern.ch/work/t/tjunk/public/2024tutorialfiles/`.

After running the program, you should have an output file `tutorial_hist.root`.  Note -- please do not
store large rootfiles in `/exp/dune/app`!  The disk is rather small, and we'd like to
save it for applications, not data.  But this file ought to be quite small.
Open it in root

~~~
  root tutorial_hist.root
~~~
{: .language-bash}

and look at the histograms and trees with a `TBrowser`.  It is empty!

#### Adjust the program's job configuration

In Session #1, the code editing session, 

~~~
  cd ${MRB_SOURCE}/protoduneana/protoduneana/TutorialExamples/
~~~
{: .language-bash}

See that `analyzer_job.fcl` includes `clustercounter.fcl`.  The `module_type`
line in that `fcl` file defines the name of the module to run, and 
`ClusterCounter_module.cc` just prints out a message in its analyze() method
just prints out a line to stdout for each event, without making any 
histograms or trees.  

Aside on module labels and types:  A module label is used to identify
which modules to run in which order in a trigger path in an art job, and also
to label the output data products.  The "module type" is the name of the source
file:  `moduletype_module.cc` is the filename of the source code for a module
with class name moduletype.  The build system preserves this and makes a shared object (`.so`)
library that art loads when it sees a particular module_type in the configuration document.
The reason there are two names here is so you
can run a module multiple times in a job, usually with different inputs.  Underscores
are not allowed in module types or module labels because they are used in
contexts that separate fields with underscores.

Let's do something more interesting than ClusterCounter_module's print 
statement.

Let's first experiment with the configuration to see if we can get
some output.  In Session #3 (the running session),

~~~
  fhicl-dump analyzer_job.fcl > tmp.txt
~~~
{: .language-bash}

and open tmp.txt in a text editor.   You will see what blocks in there
contain the fcl parameters you need to adjust.
Make a new fcl file in the work directory
called `myana.fcl`  with these contents:

~~~
#include "analyzer_job.fcl"

physics.analyzers.clusterana.module_type: "ClusterCounter3"
~~~
{: .language-bash}

Try running it:

~~~
  lar -c myana.fcl root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}


but you will get error messages about "product not found".
Inspection of `ClusterCounter3_module.cc` in Session #1 shows that it is
looking for input clusters.  Let's see if we have any in the input file,
but with a different module label for the input data.

Look at the contents of the input file:

~~~
  product_sizes_dumper root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root | grep -i cluster
~~~
{: .language-bash}

There are clusters with module label "pandora" but not
`lineclusterdc` which you can find in the tmp.txt file above.  Now edit `myana.fcl` to say

~~~
#include "analyzer_job.fcl"

physics.analyzers.clusterana.module_type: "ClusterCounter3"
physics.analyzers.clusterana.ClusterModuleLabel: "pandora"
~~~
{: .language-bash}

and run it again:

~~~
  lar -c myana.fcl root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}


Lots of information on job configuration via FHiCL is available at this [link][redmine-327]

#### Editing the example module and building it

[YouTube Lecture Part 3](https://youtu.be/S29HEzIoGwc): Now in session #1, edit `${MRB_SOURCE}/protoduneana/protoduneana/TutorialExamples/ClusterCounter3_module.cc`

Add

~~~
#include "TH1F.h"
~~~
{: .source}

to the section with includes.

Add a private data member

~~~
TH1F *fTutorialHisto;
~~~
{: .source}

to the class.  Create the histogram in the `beginJob()` method:

~~~
fTutorialHisto = tfs->make<TH1F>("TutorialHisto","NClus",100,0,500);
~~~

Fill the histo in the `analyze()` method, after the loop over clusters:

~~~
fTutorialHisto->Fill(fNClusters);
~~~
{: .source}

Go to session #2 and build it.  The current working directory should be the build directory:

~~~
make install -j16
~~~
{: .language-bash}


Note -- this is the quicker way to re-build a product.  The `-j16` says to use 16 parallel processes,
which matches the number of cores on a build node. The command

~~~
mrb i -j16
~~~
{: .language-bash}

first does a cmake step -- it looks through all the `CMakeLists.txt` files and processes them,
making makefiles.  If you didn't edit a `CMakeLists.txt` file or add new modules or fcl files
or other code, a simple make can save you some time in running the single-threaded `cmake` step.

Rerun your program in session #3 (the run session)

~~~
  lar -c myana.fcl root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}

Open the output file in a TBrowser:

~~~
  root tutorial_hist.root
~~~
{: .language-bash}

and browse it to see your new histogram.  You can also run on some data.

~~~
  lar -c myana.fcl -T dataoutputfile.root root://fndca1.fnal.gov/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2020/detector/physics/PDSPProd4/00/00/53/87/np04_raw_run005387_0041_dl7_reco1_13832298_0_20201109T215042Z.root
~~~
{: .language-bash}

The `-T dataoutputfile.root` changes the output filename for the `TTrees` and
histograms to `dataoutputfile.root` so it doesn't clobber the one you made
for the MC output.

This iteration of course is rather slow -- rebuilding and running on files in `dCache`.  Far better,
if you are just changing histogram binning, for example, is to use the output TTree.
`TTree::MakeClass` is a very useful way to make a script that reads in the `TBranches` of a `TTree` on
a file.  The workflow in this tutorial is also useful in case you decide to add more content
to the example `TTree`.

#### Run your program in the debugger

[YouTube Lecture Part 4](https://youtu.be/xcgVKmpKgfw): In session #3 (the running session)

~~~
  setup forge_tools

  ddt `which lar` -c myana.fcl root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/06/50/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_18800650_2_20210414T012053Z.root
~~~
{: .language-bash}

Click the "Run" button in the window that pops up.  The `which lar` is needed because ddt cannot find
executables in your path -- you have to specify their locations explicitly.

In session #1, look at `ClusterCounter3_module.cc` in a text editor that lets you know what the line numbers are.
Find the line number that fills your new histogram.  In the debugger window, select the "Breakpoints"
tab in the bottom window, and usethe right-mouse button (sorry mac users -- you may need to get an external
mouse if you are using VNC.  `XQuartz` emulates a three-button mouse I believe).  Make sure the "line"
radio button is selected, and type `ClusterCounter3_module.cc` for the filename.  Set the breakpoint
line at the line you want, for the histogram filling or some other place you find interesting.  Click
Okay, and "Yes" to the dialog box that says ddt doesn't know about the source code yet but will try to
find it when it is loaded.

Click the right green arrow to start the program.   Watch the program in the Input/Output section.
When the breakpoint is hit, you can browse the stack, inspect values (sometimes -- it is better when
compiled with debug), set more breakpoints, etc.

You will need Session #1 to search for code that ddt cannot find.  Shared object libraries contain
information about the location of the source code when it was compiled.  So debugging something you
just compiled usually results in a shared object that knows the location of the source, but installed
code in CVMFS points to locations on the Jenkins build nodes.

#### Looking for source code:

Your environment has lots of variables pointing at installed code.  Look for variables like

~~~
  PROTODUNEANA_DIR
~~~

which points to a directory in `CVMFS`.

~~~
  ls $PROTODUNEANA_DIR/source

or $LARDATAOBJ_DIR/include
~~~

are good examples of places to look for code, for example.

#### Checking out and committing code to the git repository

For protoduneana and dunesw, this [wiki page][dunetpc-wiki-tutorial] is quite good.  LArSoft uses GitHub with a pull-request model.  See 

[https://cdcvs.fnal.gov/redmine/projects/larsoft/wiki/Developing_With_LArSoft][redmine-dev-larsoft]

[https://cdcvs.fnal.gov/redmine/projects/larsoft/wiki/Working_with_GitHub][redmine-working-github]

### Some handy tools for working with search paths

Tom has written some scripts and made aliases for convenience -- finding files in search paths like FHCIL_FILE_PATH, or FW_SEARCH_PATH, and searching within those files for content.  Have a look on the dunegpvms at /exp/dune/data/users/trj/texttools.  There is a list of aliases in aliases.txt that can be run in your login script (such as .profile).  Put the perl scripts and tkdiff and newtkdiff somewhere in your PATH.  A common place to put your favorite convenience scripts is ${HOME}/bin, but make sure to add that to your PATH.  The scripts tkdiff and newtkdiff are open-source graphical diff tools that run using TCL/TK.

## Common errors and recovery

#### Version mismatch between source code and installed products

When you perform an mrbsetenv or a mrbslp, sometimes you get a version mismatch.  The most common reason for this is that you have set up an older version of the dependent products.  `Dunesw` depends on `protoduneana`, which depends on `dunecore`, which depends on `larsoft`, which depends on *art*, ROOT, GEANT4, and many other products.  This [picture][dunesw-dependency-tree] shows the software dependency tree for dunesw v09_72_01_d00.  If the source code is newer than the installed products, the versions may mismatch.  You can check out an older version of the source code (see the example above) with

~~~
  mrb g -t <tag> repository
~~~
{: .language-bash}

Alternatively, if you have already checked out some code, you can switch to a different tag using your local clone of the git repository.

~~~
  cd $MRB_SOURCE/<product>
  git checkout <tag>
~~~
{: .language-bash}

Try `mrbsetenv` again after checking out a consistent version.

#### Telling what version is the right one

The versions of dependent products for a product you're building from source are listed in the file `$MRB_SOURCE/<product>/ups/product_deps``.  

Sometimes you may want to know what the version number is of a product way down on the dependency tree so you can check out its source and edit it.  Set up the product in a separate login session:

~~~
  source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
  setup <product> $DUNELAR_VERSION -q $DUNELAR_QUALIFIER
  ups active
~~~
{: .language-bash}

It usually is a good idea to pipe the output through grep to find a particular product version.  You can get dependency information with

~~~
  ups depend <product> $DUNELAR_VERSION -q $DUNELAR_QUALIFIER
~~~
{: .language-bash}

Note: not all dependencies of dependent products are listed by this command.  If a product is already listed, it sometimes is not listed a second time, even if two products in the tree depend on it.  Some products are listed multiple times.

There is a script in duneutil called `dependency_tree.sh` which makes graphical displays of dependency trees.

#### Inconsistent build directory

The directory $MRB_BUILD contains copies of built code before it gets installed to localProducts.  If you change versions of the source or delete things, sometimes the build directory will have clutter in it that has to be removed.

~~~
  mrb z
~~~
{: .language-bash}

will delete the contents of `$MRB_BUILDDIR` and you will have to type `mrbsetenv` again.

~~~
  mrb zd
~~~
{: .language-bash}

will also delete the contents of localProducts.  This can be useful if you are removing code and want to make sure the installed version also has it gone.

### Inconsistent environment

When you use UPS's setup command, a lot of variables get defined.  For each product, a variable called `<product>_DIR` is defined, which points to the location of the version and flavor of the product.  UPS has a command "unsetup" which often succeeds in undoing what setup does, but it is not perfect.  It is possible to get a polluted environment in which inconsistent versions of packages are set up and it is too hard to repair it one product at a time.  Logging out and logging back in again, and setting up the session is often the best way to start fresh.

### The setup command is the wrong one

If you have not sourced the DUNE software setup script

~~~
  source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
~~~
{: .language-bash}

you will find that the setup command that is used instead is one provided by the operating system and it requires root privilege to execute and setup will ask you for the root password.  Rather than typing that if you get in this situation, ctrl-c, source the setup_dune.sh script and try again.

#### Compiler and linker warnings and errors

Common messages from the `g++` compiler are undeclared variables, uninitialized variables, mismatched parentheses or brackets, missing semicolons, checking unsigned variables to see if they are positive (yes, that's a warning!) and other things.  mrb is set up to tell `g++` and clang to treat warnings as errors, so they will stop the build and you will have to fix them.  Often undeclared variables or methods that aren't members of a class messages result from having forgotten to include the appropriate include file.

The linker has fewer ways to fail than the compiler.  Usually the error message is "Undefined symbol".  The compiler does not emit this message, so you always know this is in the link step.  If you have an undefined symbol, one of three things may have gone wrong.  1)  You may have mistyped it (usually this gets caught by the compiler because names are defined in header files).  More likely, 2) You introduced a new dependency without updating the `CMakeLists.txt` file.  Look in the `CMakeLists.txt` file that steers the building of the source code that has the problem.  Look at other `CMakeLists.txt` files in other directories for examples of how to refer to libraries. ` MODULE_LIBRARIES` are linked with modules in the `ART_MAKE` blocks, and `LIB_LIBRARIES` are linked when building non-module libraries (free-floating source code, for algorithms).  3)  You are writing new code and just haven't gotten around to finishing writing something you called.

#### Out of disk quota

Do not store data files on the app disk!   Sometimes the app disk fills up nonetheless, and there is a quota of 100 GB per user on it.  If you need more than that for several builds, you have some options.  1)  Use `/exp/dune/data/users/<username>`.  You have a 400 GB quota on this volume.  They are slower than the app disk and can get even slower if many users are accessing them simultaneously or transferring large amounts of data to or ofrm them.  3)  Clean up some space on app.  You may want to tar up an old release and store the tarball on the data volume or in `dCache` for later use.

#### Runtime errors

Segmentation faults:  These do not throw errors that *art* can catch. They terminate the program immediately.  Use the debugger to find out where they happened and why.

Exceptions that are caught.  The `ddt` debugger has in its menu a set of standard breakpoints.   You can instruct the debugger to stop any time an exception is thrown.  A common exception is a vector accessed past its size using `at()`, but often these are hard to track down because they could be anywhere.  Start your program with the debugger, but it is often a good idea to turn off the break-on-exception feature until after the geometry has been read in.  Some of the XML parsing code throws a lot of exceptions that are later caught as part of its normal mode of operation, and if you hit a breakpoint on each of these and push the "go" button with your mouse each time, you could be there all day.  Wait until the initialization is over, press "pause" and then turn on the breakpoints by exception.

If you miss, start the debugging session over again.  Starting the session over is also a useful technique when you want to know what happened *before* a known error condition occurs.  You may find yourself asking "how did it get in *that* condition?  Set a breakpoint that's earlier in the execution and restart the session.  Keep backing up -- it's kind of like running the program in reverse, but it's very slow.  Sometimes it's the only way.

Print statements are also quite useful for rare error conditions. If a piece of code fails infrequently, based on the input data, sometimes a breakpoint is not very useful because most of the time it's fine and you need to catch the program in the act of misbehaving.  Putting in a low-tech print statement, sometimes with a uniquely-identifying string so you can grep the output, can let you put some logic in there to print only when things have gone bad, or even if you print on each iteration, you can just look at the last bit of printout before a crash.

#### No authentication/permission

You will almost always need to have a valid Kerberos ticket in your session.  Accessing your home directory on the Fermilab machines requires it.  Find your tickets with the command

~~~
  klist
~~~
{: .language-bash}

By default, they last for 25 hours or so (a bit more than a day).  You can refresh them for another 25 hours (up to
one week's worth of refreshes are allowed) with

~~~
  kinit -R
~~~
{: .language-bash}

If you have a valid ticket on one machine and want to refresh tickets on another, you can 

~~~
k5push <nodename>
~~~
{: .language-bash}

The safest way to get a new ticket to a machine is to kinit on your local computer (like your laptop) and log in again,
making sure to forward all tickets.  In a pinch, you can run kinit on a dunegpvm and enter your Kerberos password, but this is discouraged as bad actors can (and have!) installed keyloggers on shared systems, and have stolen passwords.  DO NOT KEEP PRIVATE, PERSONAL INFORMATION ON FERMILAB COMPUTERS!  Things like bank account numbers, passwords, and social security numbers are definitely not to be stored on public, shared computers.  Running `kinit -R` on a shared machine is fine.

You will need a grid proxy to submit jobs and access data in `dCache` via `xrootd` or `ifdh`.  

~~~
  setup_fnal_security
~~~
{: .language-bash}

will use your valid Kerberos ticket to generate the necessary certificates and proxies.

#### Link to art/LArSoft tutorial May 2021


[https://wiki.dunescience.org/wiki/Presentation_of_LArSoft_May_2021][dune-larsoft-may21]


[dunetpc-wiki]:  https://cdcvs.fnal.gov/redmine/projects/dunetpc/wiki/_Tutorial_
[mrb-reference-guide]: https://cdcvs.fnal.gov/redmine/projects/mrb/wiki/MrbRefereceGuide
[dune-wiki-protodune-sp]: https://wiki.dunescience.org/wiki/Look_at_ProtoDUNE_SP_data
[redmine-327]:  https://cdcvs.fnal.gov/redmine/documents/327
[dunetpc-wiki-tutorial]:  https://cdcvs.fnal.gov/redmine/projects/dunetpc/wiki/_Tutorial_
[redmine-dev-larsoft]: https://cdcvs.fnal.gov/redmine/projects/larsoft/wiki/Developing_With_LArSoft
[redmine-working-github]: https://cdcvs.fnal.gov/redmine/projects/larsoft/wiki/Working_with_GitHub
[dune-larsoft-may21]: https://wiki.dunescience.org/wiki/Presentation_of_LArSoft_May_2021
[dunesw-dependency-tree]: https://wiki.dunescience.org/w/img_auth.php/6/6f/Dunesw_v09_72_01_e20_prof_graph.pdf

{%include links.md%} 


