---
title: Data Management (2024 updated for metacat/justin/rucio)
teaching: 40
exercises: 0
questions:
- What are the data management tools and software for DUNE? 
- How are different software versions handled? 
- What are the best data management practices? 
objectives:
- Learn how to access data from DUNE Data Catalog.
- Understand the roles of the tools UPS, mrb and CVMFS. 
keypoints:
- SAM and Rucio are data handling systems used by the DUNE collaboration to retrieve data.
- Staging is a necessary step to make sure files are on disk in dCache (as opposed to only on tape).
- Xrootd allows user to stream data files. 
- The Unix Product Setup (UPS) is a tool to ensure consistency between different software versions and reproducibility.
- The multi-repository build (mrb) tool allows code modification in multiple repositories, which is relevant for a large project like LArSoft with different cases (end user and developers) demanding consistency between the builds.
- CVMFS distributes software and related files without installing them on the target computer (using a VM, Virtual Machine).
---

<!--
#### Session Video

The session will be captured on video a placed here after the workshop for asynchronous study.

<!-- The session was captured for your asynchronous review.
The session was video captured for your asynchronous review. The video from the full two day training in May 2022 is provided here as a reference.
<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Nz5goj93eq0" title="DUNE Computing Tutorial May 2022 Data Management" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>
-->

<!--

#### Live Notes

Participants are encouraged to monitor and utilize the [Livedoc for May. 2023](https://docs.google.com/document/d/19XMQqQ0YV2AtR5OdJJkXoDkuRLWv30BnHY9C5N92uYs/edit?usp=sharing) to ask questions and learn.  For reference, the [Livedoc from Jan. 2023](https://docs.google.com/document/d/1sgRQPQn1OCMEUHAk28bTPhZoySdT5NUSDnW07aL-iQU/edit?usp=sharing) is provided.

<!--Temporary Note: The May 2023 version of the DUNE Software and Computing training was imported from the May 2022 version because it was a two day event, similar to this one, see [03-data-management.md (May 2022)](https://github.com/DUNE/computing-training-basics/blob/gh-pages/_episodes/03-data-management.md) for reference.

This lesson (03-data-management.md) was imported from the [Jan. 2023 lesson](https://github.com/DUNE/computing-training-basics-short/tree/gh-pages/_episodes) which was a shortened version of the training.

Quiz blocks are added in this lesson and should be administered in the closing minutes of this lesson. Feel free to modify or add quiz questions. Some of these quiz questions might be more appropriate for 02-storage-spaces.md -->

 

## Introduction

DUNE data is stored around the world and the storage elements are not always organized in a way that they can be easily inspected. For this purpose we use the metacat data catalog to describe the data and collections and rucio to determine where replicas of files are.  There is also a legacy SAM data access system that can be used for older files. 

### What is metacat

Metacat is a file catalog - it allows you to search for files that have particular attributes and understand their provenance, including details on all of their processing steps. 

You can find extensive documentation on metacat at:

[General metacat documentation](https://metacat.readthedocs.io/en/latest/)

[DUNE metacat examples](https://dune.github.io/DataCatalogDocs/index.html)

### What is(was) SAM?  
Sequential Access with Metadata (SAM) is a data handling system developed at Fermilab.  It is designed to tracklocations of files and other file metadata.

This lecture will show you how to access data files that have been defined to the DUNE Data Catalog. Execute the following commands after logging in to the DUNE interactive node, and sourcing the main dune setups.

Once per session:
~~~
setup sam_web_client
export SAM_EXPERIMENT=dune
~~~

### What is Rucio?
Rucio is the next-generation Data Replica service and is part of DUNE's new Distributed Data Management (DDM) system that is currently in deployment. 
Rucio has two functions:
1. A rule-based system to get files to Rucio Storage Elements around the world and keep them there.
2. To return the "nearest" replica of any data file for use either in interactive or batch file use.  It is expected that most DUNE users will not be regularly using direct Rucio commands, but other wrapper scripts that calls them indirectly.

As of the date of the June 2024 tutorial:
- The Rucio client is available in CVMFS
- Most DUNE users are now enabled to use it. New users may not automatically be added. 

FIXME what is procedure for adding new users?

~~~
# get a kx509 proxy
export RUCIO_ACCOUNT=$USER
rucio:protodune-sp
cern-eos:/eos/experiment/neutplatform/protodune/rawdata/np04/detector/None/raw/07/42/28/49
castor:/neutplatform/protodune/rawdata/np04/detector/None/raw/07/42/28/49
enstore:/pnfs/dune/tape_backed/dunepro/protodune/np04/beam/detector/None/raw/07/42/28/49(597@vr0337m8)
~~~
{: .output}

which is the locations of the file on disk and tape. We can use this to copy the file from tape to our local disk.

To list raw data files for a given run:
~~~
samweb list-files "run_number 5758 and run_type protodune-sp and data_tier raw"
~~~
c

~~~
np04_raw_run005758_0001_dl3.root
np04_raw_run005758_0002_dl2.root
...
np04_raw_run005758_0065_dl10.root
np04_raw_run005758_0065_dl4.root
~~~
{: .output}

What about a reconstructed version?
~~~ 
samweb list-files "run_number 5758 and run_type protodune-sp and data_tier full-reconstructed and version (v07_08_00_03,v07_08_00_04)"
~~~
{: .language-bash}

~~~
np04_raw_run005758_0053_dl7_reco_12891068_0_20181101T222620.root
np04_raw_run005758_0025_dl11_reco_12769309_0_20181101T213029.root
np04_raw_run005758_0053_dl2_reco_12891066_0_20181101T222620.root
...
np04_raw_run005758_0061_dl8_reco_14670148_0_20190105T175536.root
np04_raw_run005758_0044_dl6_reco_14669100_0_20190105T172046.root
~~~
{: .output}

The above is truncated output to show us the one reconstructed file that is the child of the raw data file above.

To see the total number of files that match a certain query expression, then add the `--summary` option to `samweb list-files`.

`samweb` allows you to select on a lot of parameters which are documented here:

* [Useful ProtoDUNE samweb parameters][useful-samweb]

* [dune-data.fnal.gov](https://dune-data.fnal.gov) lists some official dataset definitions 

## Accessing data for use in your analysis
To access data without copying it, `XRootD` is the tool to use. However it will work only if the file is staged to the disk.

You can stream files worldwide if you have a DUNE VO certificate as described in the preparation part of this tutorial.

### Where _is_ the file?

An example to find a given file:  
~~~
samweb get-file-access-url np04_raw_run005758_0001_dl3_reco_13600804_0_20181127T081955.root --schema=root
~~~
{: .language-bash}
~~~
root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro/protodune/np04/beam/output/detector/full-reconstructed/08/61/68/00/np04_raw_run005758_0001_dl3_reco_13600804_0_20181127T081955.root
~~~
{: .output}

**Resources**: [Using the SAM Data Catalog][sam-data-control]. [More SAM documentation][sam-longer]
> ## Exercise 1
> * Use the `--location` argument to show the path of the file above on either `enstore`, `castor` or `cern-eos`.
> * Use `get-metadata` to get SAM metadata for this file. Note that `--json` gives the output in json format.
{: .challenge}


When we are analyzing large numbers of files in a group of batch jobs, we use a SAM snapshot to describe the full set of files that we are going to analyze and create a SAM Project based on that. Each job will then come up and ask SAM to give it the next file in the list. SAM has some capability to grab the nearest copy of the file. For instance if you are running at CERN and analyzing this file it will automatically take it from the CERN storage space EOS.

> ## Exercise 2
> * use the samweb describe-definition command to see the dimensions of data set PDSPProd4_MC_1GeV_reco1_sce_datadriven_v1
> * use the samweb list-definition-files command with the --summary option to see the total size of PDSPProd4_MC_1GeV_reco1_sce_datadriven_v1
> * use the samweb take-snapshot command to make a snapshot of PDSPProd4_MC_1GeV_reco1_sce_datadriven_v1
{: .challenge}

-->






## Quiz

> ## Question 01
>
> What is file metadata?
> <ol type="A">
> <li>Information about how and when a file was made</li>
> <li>Information about what type of data the file contains</li>
> <li>Conditions such as liquid argon temperature while the file was being written</li>
> <li>Both A and B</li>
> <li>All of the above</li>
> </ol>
>
> > ## Answer
> > The correct answer is D - Both A and B.
> > {: .output}
> > Comment here
> {: .solution}
{: .challenge}

> ## Question 02
>
> How do we determine a DUNE data file location?
> <ol type="A">
> <li>Do `ls -R` on /pnfs/dune and grep</li>
> <li>Use `rucio list-file-replicas` (namespace:filename)</li>
> <li>Ask the data management group</li>
> <li>None of the Above</li>
> </ol>
>
> > ## Answer
> > The correct answer is B - use `rucio list-file-replicas` (namespace:filename).
> > {: .output}
> > Comment here
> {: .solution}
{: .challenge}


## Useful links to bookmark
* Metacat: [https://dune.github.io/DataCatalogDocs](https://dune.github.io/DataCatalogDocs/index.html)
* Pre-2024 Official dataset definitions: [dune-data.fnal.gov](https://dune-data.fnal.gov)
* [UPS reference manual](http://www.fnal.gov/docs/products/ups/ReferenceManual/)
* [UPS documentation (redmine)](https://cdcvs.fnal.gov/redmine/projects/ups/wiki)
* UPS qualifiers: [About Qualifiers (redmine)](https://cdcvs.fnal.gov/redmine/projects/cet-is-public/wiki/AboutQualifiers)
* [mrb reference guide (redmine)](https://cdcvs.fnal.gov/redmine/projects/mrb/wiki/MrbRefereceGuide)
* CVMFS on DUNE wiki: [Access files in CVMFS](https://wiki.dunescience.org/wiki/DUNE_Computing/Access_files_in_CVMFS)

[Ifdh_commands]: https://cdcvs.fnal.gov/redmine/projects/ifdhc/wiki/Ifdh_commands
[xrootd-man-pages]: https://xrootd.slac.stanford.edu/docs.html
[Understanding-storage]: https://cdcvs.fnal.gov/redmine/projects/fife/wiki/Understanding_storage_volumes
[useful-samweb]: https://wiki.dunescience.org/wiki/Useful_ProtoDUNE_samweb_parameters
[dune-data-fnal]: https://dune-data.fnal.gov/
[dune-data-fnal-how-works]: https://dune-data.fnal.gov/tutorial/howitworks.pdf
[sam-data-control]: https://wiki.dunescience.org/wiki/Using_the_SAM_Data_Catalog_to_find_data
[sam-longer]: https://dune.github.io/computing-basics/sam-by-schellman/index.html
[Spack documentation]: https://fifewiki.fnal.gov/wiki/Spack
