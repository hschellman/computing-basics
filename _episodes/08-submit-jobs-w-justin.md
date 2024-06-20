---
title:  Submit grid jobs with JustIn
teaching: 20
exercises: 0
questions:
- How to submit realistic grid jobs with JustIn
objectives:  
- Demonstrate use of JustIn for job submission with more complicated setups.
keypoints:
- Always, always, always prestage input datasets. No exceptions.
---

#  PLEASE USE THE NEW JUSTIN SYSTEM INSTEAD OF POMS

__The JustIn Tutorial is currently at: [JustIn Tutorial](https://docs.dunescience.org/cgi-bin/sso/RetrieveFile?docid=30145)__

The JustIn system is describe in detail at: 

__[JustIn Home](https://justin.dune.hep.ac.uk/dashboard/)__

__[JustIn Docs](https://justin.dune.hep.ac.uk/docs/)__


> ## Note:  The rest of this page is for POMS which is no longer fully supported.  Please use Justin
{: .callout}

<!--#### Session Video

This session will be captured on video a placed here after the workshop for asynchronous study.

#### Live Notes

Participants are encouraged to monitor and utilize the [Livedoc for May. 2023](https://docs.google.com/document/d/19XMQqQ0YV2AtR5OdJJkXoDkuRLWv30BnHY9C5N92uYs/edit?usp=sharing) to ask questions and learn.  For reference, the [Livedoc from Jan. 2023](https://docs.google.com/document/d/1sgRQPQn1OCMEUHAk28bTPhZoySdT5NUSDnW07aL-iQU/edit?usp=sharing) is provided.

-->

# Getting set up to use POMS

If you haven't used POMS in a while (several days), or it is your first time, you will need to be sure you upload a proxy and token to the server for use on your behalf. The easiest way to do that is with the `upload_file` command in the fife_utils package. If you don't already have fife_utils set up, just do

```bash
 . /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
 setup fife_utils
```

Then simply run the upload command:

```bash
upload_file --experiment=dune --poms_role=analysis --proxy --vaulttoken
```
You'll see something like this:

~~~
updating credmon on jobsub01.fnal.gov
updating credmon on jobsub02.fnal.gov
updating credmon on jobsub04.fnal.gov
updating credmon on jobsub05.fnal.gov
updating credmon on jobsubdevgpvm01.fnal.gov
updating credmon on dunegpschedd01.fnal.gov
updating credmon on dunegpschedd02.fnal.gov
Fetching options from https://fifebatch.fnal.gov/cigetcertopts.txt
Checking if /tmp/x509up_voms_dune_Analysis_UID has at least 1.0 hours left
120.00 hours remaining, enough to reuse
Checking if myproxy.fnal.gov has at least 503.0 hours left
253.67 hours remaining in MyProxy, not enough
Fetching list of IdPs from https://cilogon.org/include/ecpidps.txt
Requesting authorization from SP https://ecp.cilogon.org/secure/getcert/
Making unauthorized request to IdP https://ecp-prod.fnal.gov/idp-krb/profile/SAML2/SOAP/ECP
Making kerberized request to IdP https://ecp-prod.fnal.gov/idp-krb/profile/SAML2/SOAP/ECP
Sending response to Assertion Consumer https://ecp.cilogon.org/Shibboleth.sso/SAML2/ECP
Requesting certificate from SP https://ecp.cilogon.org/secure/getcert/
Converting PKCS12 certificate to PEM
Generating proxy for storage
Storing proxy in /tmp/x509up_voms_dune_Analysis_UID
subject  : /DC=org/DC=cilogon/C=US/O=Fermi National Accelerator Laboratory/OU=People/CN=John Blutarsky/CN=UID:bluto/CN=2468866293
issuer   : /DC=org/DC=cilogon/C=US/O=Fermi National Accelerator Laboratory/OU=People/CN=John Blutarsky/CN=UID:bluto
Your proxy is valid until: Thu Jun  1 11:54:04 2023
Generating proxy for MyProxy
Storing proxy in MyProxy server myproxy.fnal.gov
uploaded: /tmp/vt_dune_Analysis_username to POMS server
uploaded: /tmp/x509up_voms_dune_Analysis_username to POMS server
~~~

Of course your username and UID will be different. Note that you _may_ be prompted to do the CILogon authentication as discussed in the previous lesson. If so, go ahead and do that, and the workflow should resume.

# Submit with POMS: more realistic workflows

This lesson extends from earlier work: [Grid Job Submission and Common Errors]({{ site.baseurl }}/07-grid-job-submission/index.html) 

POMS is the recommended way of submitting large workflows. It offers several advantages over other systems, such as 

* Fully configurable. Any executables can be run, not necessarily only lar or art
* Automatic monitoring and campaign management options
* Multi-stage workflow dependencies, automatic dataset creation between stages
* Automated recovery options

At its core, in POMS one makes a "campaign", which has one or more "stages". In our first example there was only a single stage.  

For analysis use: [main POMS page][poms-page-ana]  
An [example campaign](https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14101).

Of course in reality you may need to run multiple steps of a workflow in a single job, or run multiple stages in separate jobs, or modify things from a default release, or iterate over multiple config sets, or any number of other arbitrarily complicated ideas. You also have to consider things like SAM metadata for your files. In this lesson we'll look at some of these more realistic cases and show how they can be set up with POMS campaigns.


## Submit work with a modified .fcl file

Suppose you want to run something with a minor modification to a fcl file. Why bother with downloading and building a custom release and shipping that to your jobs when you don't have any new code or libraries? A much simpler way is to make a local copy of the .fcl file in job and then edit the local copy as needed.

[https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14110](https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14110)

## Run a workflow with multiple executable sections (and chained inputs/outputs)

In this example we run a reco2 step followed by a michelremoving step in the same job. The output of reco2 serves as input to michelremoving. Here we only do one input file per job to preserve the 1:1 correspondence between reco1 and reco2 files (nice in this case but not necessary all the time). We see there are multiple executable stages and multiple job_output sections since we save both outputs and actually write them to different directories. REMEMBER: never put more than a few thousand files in any one directory in dCache. If you have a large campaign with many jobs, you may need to split your outputs appropriately with mutliple directories. The only exception to that is if you're copying to a dropbox location for transfer to a tape-backed area, since those will be automatically cleaned up after transfer.

You'll see we also retained the fcl editing bit and a metadata extractor for the reco2 file.

[https://pomsgpvm01.fnal.gov/poms/campaign_overview/dune/analysis?campaign_id=6280](https://pomsgpvm01.fnal.gov/poms/campaign_overview/dune/analysis?campaign_id=6280)

## Create a multi-stage workflow

Sometimes you may want to break separate components into multiple stages. We have the same components as the mutiple executable example but we split the reco2 and michelremoving since the michelremoving files are very small and we want to merge many to one (not we set n_files_per_job much higher in the michel stage). We could of course do things the same way as before but would have to manually merge later. In particular note the [stage_X] sections of the POMS config file. For each stage section you have have separate overrides and still use the same config file. We also use the add_to_dataset option for job outputs and give it the `_poms_task` special keyword; POMS will take care of automatically generating a SMA dataset consisting of the reco2 outputs, which will serve as the input dataset to the next stage.

[https://pomsgpvm01.fnal.gov/poms/show_campaign_stages/dune/analysis?campaign_name=kherner-May2022Tutorial-multi-stage](https://pomsgpvm01.fnal.gov/poms/show_campaign_stages/dune/analysis?campaign_name=kherner-May2022Tutorial-multi-stage)

## Iterate over multiple datasets or list items

Note that **Datasets do not have to be actual SAM datasets** in POMS; they can really be any value or even a list of values (though they could also be a list of SAM datasets depending on what you're doing). Here we set up a list and cycle through it. Each time you submit, POMS automatically increments the list position until you reach the end of the list. Then the "dataset" variable passed to e.g. fife_launch will take the value from the list.

[https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14113](https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14113)
**Important note about this campaign**: since it is an example I've sort of hard-coded the path to particular inputs here (the global.inputfile value) to illustrate how you can use the value from the list. In general you should NOT hard-code inputs!
**Note 2 about using list of SAM datasets:** if the values in your list consist of all or part of an actual dataset name, and you want to run over a dataset, you have to use the `--dataset` option in jobsub_submit to get it to understand that you're really using a dataset. The practical way to do that is to also have e.g. `-Osubmit.dataset=', '%(dataset)s']` as an additional override. See the draining dataset example below. You'd do the same thing if you had a lsist of datasets.

### Aside: a word on n_files_per_job and SAM consumer limits

It is possible to use the `n_files_per_job` option (in some of the examples) as a way to automatically calculate a number of jobs to submit to process your dataset (at least for workflows where you have an input dataset). In general unless your workflow absolutely cannot handle more than one input file per job (or it takes a very long time, say 24h, to process a single file), you should expect to process multiple input files. Only processing one input file per job is often extremely inefficient (you have to pay the job startup overhead for every single file), puts more load on all the various servers, and can often lead to very small output files, which are not great for dCache. By using 
n_files_per_job the system will compute the number of parallel jobs for you (basically N files in dataset / n_files_per_job with some rounding). Note that n_files_per_job should generally be driven by the desired job length (generally several hours is a good aim) and/or the desired output file size (generally aim for ~ 1 GB or greater output files sizes, subject to reasonable constraints on job run time). When doing that, be sure to set the SAM consumer limit on your job to be at least n_files_per_job, and it's usually a good idea to set it a bit higher so that if you have any job failures early on, other jobs can pick up the slack. For example if you did n_files_per_job of 3, maybe you'd set the SAM consumer limit to be e.g. 5 (again subject to run time and output file size concerns).


## Draining dataset

If you have very large datasets, or datasets that change over time (such as in keepup processing), you may want to submit only a part of it at once. Of course then you need to keep trakc of what has already been submitted from the main dataset each time. Fortunately POMS provides such functionality with the draining and drainingn dataset types. Our example uses the latter, which will carve out a dataset of at most n files at a time from the larger dataset, keeping track of which files have already been submitted to ensure no duplication between different submissions. We will use the same MC example dataset as we have been using but will now submit it in several pieces.

[https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14108](https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=14108)

There is an important difference with this campaign relative to the previous one with a list as mentioned above. Take particular note of how the submit.dataset override is included. That is what generates the --dataset option to be added to the jobsub_submit command.

# Still more complicated setups

These are just some basic examples to get you started that cover ~90% of standard use cases. Many other setups are possible! Look at the [POMS documentation](https://cdcvs.fnal.gov/redmine/projects/prod_mgmt_db/wiki/POMS_User_Documentation) for some other interesting cases, and reach out to the experts for guidance. We want to help! Here we'll just point out a couple of other cases:

"multiparam" type (interating over all combinations of multiple lists): [https://cdcvs.fnal.gov/redmine/projects/prod_mgmt_db/wiki/POMS_User_Documentation#Campaign-Stage-Datasets-and-Split-types](https://cdcvs.fnal.gov/redmine/projects/prod_mgmt_db/wiki/POMS_User_Documentation#Campaign-Stage-Datasets-and-Split-types)

{%include links.md%} 

[job-autorelease]: https://cdcvs.fnal.gov/redmine/projects/fife/wiki/Job_autorelease
[dune-openscience-grid-org]: dune.opensciencegrid.org
[larsoft-openscience-grid-org]: larsoft.opensciencegrid.org
[redmine-wiki-jobsub]: https://cdcvs.fnal.gov/redmine/projects/jobsub/wiki
[redmine-wiki-using-the-client]: https://cdcvs.fnal.gov/redmine/projects/jobsub/wiki/Using_the_Client

[fifemon-dune]: https://fifemon.fnal.gov/monitor/d/000000053/experiment-batch-details?orgId=1&var-experiment=dune
[fifemon-myjobs]: https://fifemon.fnal.gov/monitor/d/000000116/user-batch-details?orgId=1&var-cluster=fifebatch&var-user=kherner
[fifemon-whyheld]: https://fifemon.fnal.gov/monitor/d/000000146/why-are-my-jobs-held?orgId=1
[kibana]: https://fifemon.fnal.gov/kibana/goto/8f432d2e4a40cbf81d3072d9c9d688a6
[poms-page-ana]: https://pomsgpvm01.fnal.gov/poms/index/dune/analysis/
[poms-user-doc]: https://cdcvs.fnal.gov/redmine/projects/prod_mgmt_db/wiki/POMS_User_Documentation
[fife-launch-ref]: https://cdcvs.fnal.gov/redmine/projects/fife_utils/wiki/Fife_launch_Reference 
[poms-campaign-stage-info]: https://pomsgpvm01.fnal.gov/poms/campaign_stage_info/dune/analysis?campaign_stage_id=9023
[project-py-guide]: https://cdcvs.fnal.gov/redmine/projects/project-py/wiki/Project-py_guide
[DUNE_computing_tutorial_advanced_topics_20210129]: https://indico.fnal.gov/event/20144/contributions/55932/attachments/34945/42690/DUNE_computing_tutorial_advanced_topics_and_best_practices_20200129.pdf


