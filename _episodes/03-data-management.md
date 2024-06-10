---
title: Data Management (2024 updated for metacat/justin/rucio)
teaching: 40
exercises: 0
questions:
- What are the data management tools and software for DUNE? 
objectives:
- Learn how to access data from DUNE Data Catalog.
- Learn a bit about the JustIN workflow system for submitting batch jobs.
keypoints:
- SAM and Rucio are data handling systems used by the DUNE collaboration to retrieve data.
- Staging is a necessary step to make sure files are on disk in dCache (as opposed to only on tape).
- Xrootd allows user to stream data files. 
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

### Let's find a file
~~~
# get a kx509 proxy
export RUCIO_ACCOUNT=$USER
rucio list-file-replicas pdsp_det_reco:np04_raw_run005141_0013_dl10_reco1_18127013_0_20210318T104043Z.root --pfns --protocols=root
~~~
{: .language-bash}

returns 2 locations:

~~~
root://xrootd01.esc.qmul.ac.uk:1094//dune/RSE/pdsp_det_reco/dd/e5/np04_raw_run005141_0013_dl10_reco1_18127013_0_20210318T104043Z.root
root://fndca1.fnal.gov:1094/pnfs/fnal.gov/usr/dune/tape_backed/dunepro//protodune-sp/full-reconstructed/2021/detector/physics/PDSPProd4/00/00/51/41/np04_raw_run005141_0013_dl10_reco1_18127013_0_20210318T104043Z.root
~~~
{: .output}

which is the locations of the file on disk and tape. We can use this to copy the file to our local disk or access the file via xroot. 

### Finding files by characteristics

To list raw data files for a given run:
~~~
metacat query "files where core.file_type=detector \
 and core.run_type='protodune-sp' and core.data_tier=raw \
 and core.data_stream=physics and core.runs[any] in (5141)"
~~~
{: .language-bash}

- `core.run_type` tells you which of the many DAQ's this came from. 
- `core.file_type` tells detector from mc
- `core.data_tier` could be raw, full-reconstructed, root-tuple.  Same data different formats. 

~~~
protodune-sp:np04_raw_run005141_0013_dl7.root
protodune-sp:np04_raw_run005141_0005_dl3.root
protodune-sp:np04_raw_run005141_0003_dl1.root
protodune-sp:np04_raw_run005141_0004_dl7.root
...
protodune-sp:np04_raw_run005141_0009_dl7.root
protodune-sp:np04_raw_run005141_0014_dl11.root
protodune-sp:np04_raw_run005141_0007_dl6.root
protodune-sp:np04_raw_run005141_0011_dl8.root
~~~
{: .output}

Note the presence of both a *namespace* and a *filename* 

What about some files from a reconstructed version?
~~~ 
metacat query "files from dune:all where core.file_type=detector \
 and core.run_type='protodune-sp' and core.data_tier=full-reconstructed  \
 and core.data_stream=physics and core.runs[any] in (5141) and dune.campaign=PDSPProd4 limit 10" 
~~~
{: .language-bash}

~~~
pdsp_det_reco:np04_raw_run005141_0013_dl10_reco1_18127013_0_20210318T104043Z.root
pdsp_det_reco:np04_raw_run005141_0015_dl4_reco1_18126145_0_20210318T101646Z.root
pdsp_det_reco:np04_raw_run005141_0008_dl12_reco1_18127279_0_20210318T104635Z.root
pdsp_det_reco:np04_raw_run005141_0002_dl2_reco1_18126921_0_20210318T103516Z.root
pdsp_det_reco:np04_raw_run005141_0002_dl14_reco1_18126686_0_20210318T102955Z.root
pdsp_det_reco:np04_raw_run005141_0015_dl5_reco1_18126081_0_20210318T122619Z.root
pdsp_det_reco:np04_raw_run005141_0017_dl10_reco1_18126384_0_20210318T102231Z.root
pdsp_det_reco:np04_raw_run005141_0006_dl4_reco1_18127317_0_20210318T104702Z.root
pdsp_det_reco:np04_raw_run005141_0007_dl9_reco1_18126730_0_20210318T102939Z.root
pdsp_det_reco:np04_raw_run005141_0011_dl7_reco1_18127369_0_20210318T104844Z.root
~~~
{: .output}


To see the total number of files that match a certain query expression, then add the `-s` option to `metacat query`.

<!---`samweb` allows you to select on a lot of parameters which are documented here:

* [Useful ProtoDUNE samweb parameters][useful-samweb]

* [dune-data.fnal.gov](https://dune-data.fnal.gov) lists some official dataset definitions 

-->

See the metacat documentation for more information about queries.  [DataCatalogDocs][DataCatalogDocs]  and check out the glossary of common fields at: [MetaCatGlossary][MetaCatGlossary]

## Accessing data for use in your analysis
To access data without copying it, `XRootD` is the tool to use. However it will work only if the file is staged to the disk.

You can stream files worldwide if you have a DUNE VO certificate as described in the preparation part of this tutorial.

To learn more about using Rucio and Metacat to run over large data samples go here:

> # Full Justin/Rucio/Metacat Tutorial
> The [Justin/Rucio/Metacat Tutorial](https://docs.dunescience.org/cgi-bin/sso/RetrieveFile?docid=30145) 
{: .challenge}



> ## Exercise 1
> * Use `metacat file show -m namespace:filename` to get  metadata for this file. Note that `--json` gives the output in json format.
{: .challenge}


When we are analyzing large numbers of files in a group of batch jobs, we use a metacat dataset to describe the full set of files that we are going to analyze and use the JustIn system to run over that dataset. Each job will then come up and ask metacat and rucio to give it the next file in the list. It will try to find the nearest copy.  For instance if you are running at CERN and analyzing this file it will automatically take it from the CERN storage space EOS.

> ## Exercise 2
FIXME Need to make an example of looking at a dataset
{: .challenge}

**Resources**: [DataCatalogDocs][DataCatalogDocs]  The [Justin/Rucio/Metacat Tutorial](https://docs.dunescience.org/cgi-bin/sso/RetrieveFile?docid=30145) 






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
> <li>Use `rucio list-file-replicas` (namespace:filename) --pnfs --protocols=root</li>
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
[DataCatalogDocs]: https://dune.github.io/DataCatalogDocs/index.html
[MetaCatGlossary]: https://dune.github.io/DataCatalogDocs/glossary.html
