---
title: Storage Spaces (2024)
teaching: 30
exercises: 15
questions:
- What are the types and roles of DUNE's data volumes? 
- What are the commands and tools to handle data?  
objectives:  
- Understanding the data volumes and their properties
- Displaying volume information (total size, available size, mount point, device location)
- Differentiating the commands to handle data between grid accessible and interactive volumes
keypoints:
- Home directories are centrally managed by Computing Division and meant to store setup scripts, do NOT store certificates here.
- Network attached storage (NAS) /dune/app is primarily for code development.
- The NAS /dune/data is for store ntuples and small datasets.
- dCache volumes (tape, resilient, scratch, persistent) offer large storage with various retention lifetime.
- The tool suites idfh and XRootD allow for accessing data with appropriate transfer method and in a scalable way.
---

## This is an updated version of the 2023 training



<!-- #### Session Video

The session will be captured on video a placed here after the workshop for asynchronous study.

#### Live Notes

Participants are encouraged to monitor and utilize the [Livedoc for May. 2023](https://docs.google.com/document/d/19XMQqQ0YV2AtR5OdJJkXoDkuRLWv30BnHY9C5N92uYs/edit?usp=sharing) to ask questions and learn.  For reference, the [Livedoc from Jan. 2023](https://docs.google.com/document/d/1sgRQPQn1OCMEUHAk28bTPhZoySdT5NUSDnW07aL-iQU/edit?usp=sharing) is provided.

Temporary Note: This lesson (02-storage-spaces.md) was imported from the [Jan. 2023 lesson](https://github.com/DUNE/computing-training-basics-short/tree/gh-pages/_episodes) which was a shortened version of the training. The May 2022 training event was a two day event, see [02-storage-spaces.md (May 2022)](https://github.com/DUNE/computing-training-basics/blob/gh-pages/_episodes/02-storage-spaces.md) for reference. Quiz blocks were added. -->

## Introduction
There are four types of storage volumes that you will encounter at Fermilab (or CERN): 

- local hard drives
- network attached storage
- large-scale, distributed storage
- Rucio Storage Elements (RSE's)

Each has its own advantages and limitations, and knowing which one to use when isn't all straightforward or obvious. But with some amount of foresight, you can avoid some of the common pitfalls that have caught out other users.


## Vocabulary

**What is POSIX?** A volume with POSIX access (Portable Operating System Interface [Wikipedia](https://en.wikipedia.org/wiki/POSIX)) allow users to directly read, write and modify using standard commands, e.g. using bash scripts, fopen(). In general, volumes mounted directly into the operating system.

**What is meant by 'grid accessible'?** Volumes that are grid accessible require specific tool suites to handle data stored there. Grid access to a volume is NOT POSIX access. This will be explained in the following sections.

**What is immutable?** A file that is immutable means that once it is written to the volume it cannot be modified. It can only be read, moved, or deleted. This property is in general a restriction imposed by the storage volume on which the file is stored. Not a good choice for code or other files you want to change.  

## Interactive storage volumes (mounted on dunegpvmXX.fnal.gov)

**Home area** is similar to the user's local hard drive but network mounted
* access speed to the volume very high, on top of full POSIX access
* network volumes are NOT safe to store certificates and tickets
* important: users have a single home area at FNAL used for all experiments 
* not accessible from grid worker nodes
* not for code developement (size of less than 2 GB)
* at Fermilab, need a valid Kerberos ticket in order to access files in your Home area
* periodic snapshots are taken so you can recover deleted files. (/nashome/.snapshot)
* permissions are set so your collaborators cannot see files in your home area

> ## Note: your home area is small and private
> You want to use your home area for things that only you should see.  If you want to share files with collaborators you need to put them in the /app/ or /data/ areas described below. 
{: .callout}

**Locally mounted volumes** are physical disks, mounted directly on the computer
* physically inside the computer node you are remotely accessing
* mounted on the machine through the motherboard (not over network)
* used as temporary storage for infrastructure services (e.g. /var, /tmp,)
* can be used to store certificates and tickets. (These are saved there automatically with owner-read enabled and other permissions disabled.)
* usually very small and should not be used to store data files or for code development
* files on these volumes are not backed up

**Network Attached Storage (NAS)** element behaves similar to a locally mounted volume.
* functions similar to services such as Dropbox or OneDrive
* fast and stable POSIX access to these volumes
* volumes available only on a limited number of computers or servers
* not available on larger grid computing (FermiGrid, Open Science Grid, etc.)
* /exp/dune/app/....yourdir has periodic snapshots in /exp/dune/app/... yourdir/.snap, but /exp/dune/data does NOT
* easy to share files with colleagues using /exp/dune/data and /exp/dune/app

## Grid-accessible storage volumes

At Fermilab, an instance of dCache+Enstore is used for large-scale, distributed storage with capacity for more than 100 PB of storage and O(10000) connections. Whenever possible, these storage elements should be accessed over xrootd (see next section) as the mount points on interactive nodes are slow, unstable, and can cash the node to become unusable. Here are the different dCache volumes:

**Persistent dCache**: the data in the file is actively available for reads at any time and will not be removed until manually deleted by user
There is now a second persistent dCache volume that is dedicated for DUNE Physics groups and managed by the respective physics conveners of those 
physics group.  https://wiki.dunescience.org/wiki/DUNE_Computing/Using_the_Physics_Groups_Persistent_Space_at_Fermilab gives more details on how to get 
access to these groups.  In general if you need to store more than 5TB in persistent dCache you should be working with the Physics Groups areas.

**Scratch dCache**: large volume shared across all experiments. When a new file is written to scratch space, old files are removed in order to make room for the newer file. removal is based on Least Recently Utilized (LRU) policy.

**Tape-backed dCache**: disk based storage areas that have their contents mirrored to permanent storage on Enstore tape.  
Files are not available for immediate read on disk, but needs to be 'staged' from tape first ([see video of a tape storage robot](https://www.youtube.com/watch?v=kiNWOhl00Ao)).

**Resilient dCache**: NOTE: DIRECT USAGE is being phased out and if the Rapid Code Distribution function in POMS/jobsub does not work for you, consult with the FIFE team for a solution (handles custom user code for their grid jobs, often in the form of a tarball. Inappropriate to store any other files here (NO DATA OR NTUPLES)).

**Rucio Storage Elements**: Rucio Storage Elements (or RSEs) are storage elements provided by collaborating institution for official DUNE datasets.  Data stored in DUNE RSE's must be fully cataloged in the [metacat][metacat] catalog and is managed by the DUNE data management team. This is where you find the big official data samples. 

> ## Note - When reading from dcache always use the root: syntax, not direct /pnfs
> The Fermilab dcache areas have NFS mounts.  These are for your convenience, they allow you to look at the directory structure and, for example, remove files.  However, NFS access is slow and can hang the machine if I/O heavy processes use it.  Always use the `xroot root://<site>` ... when reading/accessing files instead of `/pnfs/` directly.  Once you have your dune environment set up the `pnfs2xrootd` command can do the conversion to `root:` format for you. 
{: .callout} 

## Summary on storage spaces
Full documentation: [Understanding Storage Volumes](https://cdcvs.fnal.gov/redmine/projects/fife/wiki/Understanding_storage_volumes)

|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
|    | Quota/Space | Retention Policy | Tape Backed? | Retention Lifetime on disk |	Use for	| Path | Grid Accessible |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Persistent dCache	| No/~100 TB/exp | Managed by Experiment| No| Until manually deleted | immutable files w/ long lifetime	| /pnfs/dune/persistent	| Yes |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Persistent PhysGrp	| Yes/~500 TB/exp | Managed by PhysGrp| No| Until manually deleted | immutable files w/ long lifetime	| /pnfs/dune/persistent/physicsgroups	| Yes |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Scratch dCache | No/no limit | LRU eviction - least recently used file deleted | No | Varies, ~30 days (*NOT* guaranteed) | immutable files w/ short lifetime | /pnfs/\<exp\>/scratch	| Yes |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Tape backed| dCache	No/O(10) PB | LRU eviction (from disk) | Yes | Approx 30 days | Long-term archive | /pnfs/dune/... | Yes |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| NAS Data | Yes (~1 TB)/ 32+30 TB total | Managed by Experiment | No | Until manually deleted | Storing final analysis samples | /exp/dune/data | No |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| NAS App | Yes (~100 GB)/ ~15 TB total | Managed by Experiment | No | Until manually deleted | Storing and compiling software | /exp/dune/app | No |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Home Area (NFS mount)	| Yes (~10 GB) | Centrally Managed by CCD | No | Until manually deleted | Storing global environment scripts (All FNAL Exp) | /nashome/\<letter\>/\<uid\>| No |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|
| Rucio	| 10 PB | Centrally Managed by DUNE  | Yes | Each file has retention policy | Official DUNE Data samples | use rucio/justin to access| Yes |
|-------------+------------------+----------+-------------+----------------+------------+--------------+-----------|


![Storage Picture](../fig/Storage.png){: .image-with-shadow }

## Monitoring and Usage
Remember that these volumes are not infinite, and monitoring your and the experiment's usage of these volumes is important to smooth access to data and simulation samples. To see your persistent usage visit [here](https://fifemon.fnal.gov/monitor/d/000000175/dcache-persistent-usage-by-vo?orgId=1&var-VO=dune) (bottom left):

And to see the total volume usage at Rucio Storage Elements around the world:

**Resource** [DUNE Rucio Storage](https://dune.monitoring.edi.scotgrid.ac.uk/app/dashboards#/view/7eb1cea0-ca5e-11ea-b9a5-15b75a959b33?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-1d,to:now)))

> ## Note - do not blindly copy files from personal machines to DUNE systems.
> You may have files on your personal machine that contain personal information, licensed software or (god forbid) malware or pornography.  Do not transfer any files from your personal machine to DUNE machines unless they are directly related to work on DUNE.  You must be fully aware of any file's contents. We have seen it all and we do not want to. 
{: .callout} 

## Commands and tools
This section will teach you the main tools and commands to display storage information and access data.

### ifdh 

Another useful data handling command you will soon come across is ifdh. This stands for Intensity Frontier Data Handling. It is a tool suite that facilitates selecting the appropriate data transfer method from many possibilities while protecting shared resources from overload. You may see *ifdhc*, where *c* refers to *client*.

> ## Note
>  ifdh is much more efficient than NSF file access.  Please use it and/or xroot when accessing remote files. 
{: .challenge}

Here is an example to copy a file. Refer to the [Mission Setup]({{ site.baseurl }}/setup.html) for the setting up the `DUNELAR_VERSION`.

> ## Note
> For now do this in the Apptainer
{: .challenge}

~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash \
-B /cvmfs,/exp,/nashome,/pnfs/dune,/opt,/run/user,/etc/hostname,/etc/hosts,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}

once in the Apptainer
~~~
#source ~/dune_presetup_2024.sh
#dune_setup
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
kx509
export ROLE=Analysis
voms-proxy-init -rfc -noregen -voms=dune:/dune/Role=$ROLE -valid 120:00
setup ifdhc
ifdh cp root://fndcadoor.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/physics/full-reconstructed/2023/mc/out1/MC_Winter2023_RITM1592444_reReco/54/05/35/65/NNBarAtm_hA_BR_dune10kt_1x2x6_54053565_607_20220331T192335Z_gen_g4_detsim_reco_65751406_0_20230125T150414Z_reReco.root /dev/null
~~~
{: .language-bash}

Note, if the destination for an ifdh cp command is a directory instead of filename with full path, you have to add the "-D" option to the command line.

**Resource:** [idfh commands](https://cdcvs.fnal.gov/redmine/projects/ifdhc/wiki/Ifdh_commands)

> ## Exercise 1
> Using the ifdh command, complete the following tasks:
> * create a directory in your dCache scratch area (/pnfs/dune/scratch/users/${USER}/) called "DUNE_tutorial_2024" 
> * copy /exp/dune/app/users/${USER}/my_first_login.txt file to that directory
> * copy the my_first_login.txt file from your dCache scratch directory (i.e. DUNE_tutorial_2024) to /dev/null
> * remove the directory DUNE_tutorial_2024
> * create the directory DUNE_tutorial_2024_data_file
> Note, if the destination for an ifdh cp command is a directory instead of filename with full path, you have to add the "-D" option to the command line. Also, for a directory to be deleted, it must be empty.
> 
> > ## Answer
> > ~~~
> > ifdh mkdir /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024
> > ifdh cp -D /exp/dune/app/users/${USER}/my_first_login.txt /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024
> > ifdh cp /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024/my_first_login.txt /dev/null
> > ifdh rm /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024/my_first_login.txt
> > ifdh rmdir /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024
> > ifdh mkdir /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024_data_file
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

### xrootd 
The eXtended ROOT daemon is a software framework designed for accessing data from various architectures in a complete scalable way (in size and performance). 

XRootD is most suitable for read-only data access.
[XRootD Man pages](https://xrootd.slac.stanford.edu/docs.html)

Issue the following command. Please look at the input and output of the command, and recognize that this is a listing of /pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024. Try and understand how the translation between a NFS path and an xrootd URI could be done by hand if you needed to do so.

~~~
xrdfs root://fndca1.fnal.gov:1094/ ls /pnfs/fnal.gov/usr/dune/scratch/users/${USER}/
~~~
{: .language-bash}

Note that you can do
~~~
lar -c <input.fcl> <xrootd_uri> 
~~~
{: .language-bash}

to stream into a larsoft module configured within the fhicl file. As well, it can be implemented in standalone C++ as

~~~
TFile * thefile = TFile::Open(<xrootd_uri>)
~~~
{: .language-c++}

or PyROOT code as

~~~
thefile = ROOT.TFile.Open(<xrootd_uri>)
~~~
{: .language-python}

### What is the right xroot path for a file.

If a file is in `/pnfs/dune/tape_backed/dunepro/protodune-sp/reco-recalibrated/2021/detector/physics/PDSPProd4/00/00/51/41/np04_raw_run005141_0003_dl9_reco1_18127219_0_20210318T104440Z_reco2_51835174_0_20211231T143346Z.root`

the command 

~~~
pnfs2xrootd /pnfs/dune/tape_backed/dunepro/protodune-sp/reco-recalibrated/2021/detector/physics/PDSPProd4/00/00/51/41/np04_raw_run005141_0003_dl9_reco1_18127219_0_20210318T104440Z_reco2_51835174_0_20211231T143346Z.root
~~~
{: .language-bash}


will return the correct xrootd uri: 

~~~
root://fndca1.fnal.gov:1094//pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/reco-recalibrated/2021/detector/physics/PDSPProd4/00/00/51/41/np04_raw_run005141_0003_dl9_reco1_18127219_0_20210318T104440Z_reco2_51835174_0_20211231T143346Z.root
~~~
{: .output}

you can then 

~~~ 
root -l <that long root: path>
~~~ 
{: .language-bash}

to open the root file.  

This even works if the file is in Europe - which you cannot do with a direct /pnfs!

~~~
root -l root://dune.dcache.nikhef.nl:1094/pnfs/nikhef.nl/data/dune/generic/rucio/usertests/b4/49/np04hd_raw_run026420_0000_dataflow0_datawriter_0_20240524T170759_20240604T204802_keepup_hists.root
~~~
{: .language-bash}

See the next section on [data management](({{ site.baseurl }}/03-data-management)) for instructions on finding files worldwide. 

> ## Note Files in /tape_backed/ may not be immediately accessible, those in /persistent/ and /scratch/ are. 
{: .callout}

## Let's practice

> ## Exercise 2
> Using a combination of `ifdh` and `xrootd` commands discussed previously:
> * Use `ifdh locateFile <file> root` to find the directory for this file `PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_off_43352322_0_20210427T162252Z.root`
> * Use `xrdcp` to copy that file to `/pnfs/dune/scratch/users/${USER}/DUNE_tutorial_2024_data_file`
> * Using `xrdfs` and the `ls` option, count the number of files in the same directory as `PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_off_43352322_0_20210427T162252Z.root`
{: .challenge}

Note that redirecting the standard output of a command into the command `wc -l` will count the number of lines in the output text. e.g. `ls -alrth ~/ | wc -l`

~~~
ifdh locateFile PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_off_43352322_0_20210427T162252Z.root root
xrdcp root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/01/67/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_off_43352322_0_20210427T162252Z.root root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/scratch/users/${USER}/DUNE_tutorial_2024_data_file/PDSPProd4a_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_off_43352322_0_20210427T162252Z.root
xrdfs root://fndca1.fnal.gov:1094/ ls /pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune-sp/full-reconstructed/2021/mc/out1/PDSPProd4a/18/80/01/67/ | wc -l
~~~
{: .language-bash}


> ## Is my file available or stuck on tape?
> /tape_backed/ storage at Fermilab is migrated to tape and may not be on disk?
> You can check this by doing the following **in an AL9 window**
> ~~~
> gfal-xattr  <xrootpath> user.status
> ~~~
> {: .language-bash}
> if it is on disk you get
> ~~~
> ONLINE
> ~~~
> {: .output}
> if it is only on tape you get
> ~~~
> NEARLINE
> ~~~
> {: .output}
>  (This command doesn't work on SL7 so use an AL9 window)
{: .challenge}


### The df command

To find out what types of volumes are available on a node can be achieved with the command `df`. The `-h` is for _human readable format_. It will list a lot of information about each volume (total size, available size, mount point, device location).
~~~
df -h
~~~
{: .language-bash}

> ## Exercise 3
> From the output of the `df -h` command, identify:
> 1. the home area
> 2. the NAS storage spaces
> 3. the different dCache volumes
{: .challenge}

## Quiz

> ## Question 01
>
> Which volumes are directly accessible (POSIX) from grid worker nodes?
> <ol type="A">
> <li>/exp/dune/data</li>
> <li>DUNE CVMFS repository</li>
> <li>/pnfs/dune/scratch</li>
> <li>/pnfs/dune/persistent</li>
> <li>None of the Above</li>
> </ol>
>
> > ## Answer
> > The correct answer is B - DUNE CVMFS repository.
> > {: .output}
> {: .solution}
{: .challenge}

> ## Question 02
>
> Which data volume is the best location for the output of an analysis-user grid job?
> <ol type="A">
> <li>dCache scratch (/pnfs/dune/scratch/users/${USER}/)</li>
> <li>dCache persistent (/pnfs/dune/persistent/users/${USER}/)</li>
> <li>Enstore tape (/pnfs/dune/tape_backed/users/${USER}/)</li>
> <li>user’s home area (`~${USER}`)</li>
> <li>NFS data volume (/dune/data or /dune/app)</li>
> </ol>
>
> > ## Answer
> > The correct answer is A, dCache scratch (/pnfs/dune/scratch/users/${USER}/).
> > {: .output}
> {: .solution}
{: .challenge}

> ## Question 03
>
> You have written a shell script that sets up your environment for both DUNE and another FNAL experiment. Where should you put it?
> <ol type="A">
> <li>DUNE CVMFS repository</li>
> <li>/pnfs/dune/scratch/</li>
> <li>/exp/dune/app/</li>
> <li>Your GPVM home area</li>
> <li>Your laptop home area</li>
> </ol>
>
> > ## Answer
> > The correct answer is D - Your GPVM home area.
> > {: .output}
> {: .solution}
{: .challenge}

> ## Question 04
>
> What is the preferred way of reading a file interactively?
> <ol type="A">
> <li>Read it across the nfs mount on the GPVM</li>
> <li>Download the whole file to /tmp with xrdcp</li>
> <li>Open it for streaming via xrootd</li>
> <li>None of the above</li>
> </ol>
>
> > ## Answer
> > The correct answer is C - Open it for streaming via xrootd. Use `pnfs2xrootd` to generate the streaming path. 
> > {: .output}
> > Comment here
> {: .solution}
{: .challenge}

## Useful links to bookmark

* [ifdh commands (redmine)](https://cdcvs.fnal.gov/redmine/projects/ifdhc/wiki/Ifdh_commands)
* [Understanding storage volumes (redmine)](https://cdcvs.fnal.gov/redmine/projects/fife/wiki/Understanding_storage_volumes)
* How DUNE storage works: [pdf](https://dune-data.fnal.gov/tutorial/howitworks.pdf)

---

{%include links.md%} 
