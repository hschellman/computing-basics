

**Table of Contents for setup**
- [Objectives](#objectives)
- [Requirements](#requirements)
- [Step 1: DUNE membership](#step-1-dune-membership)
- [Step 2: Getting accounts](#step-2-getting-accounts)
   - [With FNAL](#with-fnal)
   - [With CERN](#with-cern)
- [Step 3: Mission setup (rest of this page)](#step-3-mission-setup-(rest-of-this-page))
- [0. Basic setup on your computer.](#0.-basic-setup-on-your-computer.)
- [1. Kerberos business](#1.-kerberos-business)
- [2. ssh-in](#2.-ssh-in)
- [3. Get a clean shell](#3.-get-a-clean-shell)
- [Software setup <a name="software_setup"></a>](#software_setup)
   - [4.1 Setting up DUNE software - Scientific Linux 7 version <a name="SL7_setup"></a>](SL7setup)
   - [Caveats for later](#caveats-for-later)
   - [4.2 Setting up DUNE software - Alma9 version <a name="AL9_setup"></a>](#AL9_setup)
   - [Caveats for later](#caveats-for-later)
- [4.2 Setting up DUNE software - Alma9 version](#4.2-setting-up-dune-software---alma9-version)
   - [Caveats](#caveats)
- [5. Exercise! (For SL7 - it's easy)](#5.-exercise!-(for-sl7---it's-easy))
- [5. Exercise! (For AL9 - it's easy)](#5.-exercise!-(for-al9---it's-easy))
- [6. Getting setup for streaming and grid access](#6.-getting-setup-for-streaming-and-grid-access)
   - [Tokens method <a name="tokens"></a>](#tokens)
      - [1. Get and store your token](#1.-get-and-store-your-token)
      - [2. Tell the system where your token is](#2.-tell-the-system-where-your-token-is)
- [Set up on CERN machines <a name="setup_CERN"></a>](#setup_CERN)
   - [1. Setup in Alma9](#1.-setup-in-alma9)
   - [2. For SL7](#2.-for-sl7)
      - [Source the DUNE environment SL7 setup script](#source-the-dune-environment-sl7-setup-script)
   - [3. Getting authentication for data access](#3.-getting-authentication-for-data-access)
   - [4. Access tutorial datasets](#4.-access-tutorial-datasets)
   - [5. Notify us](#5.-notify-us)
- [Useful Links](#useful-links)

**Table of Contents for 01-introduction**
- [DUNE Computing Consortium](#dune-computing-consortium)
- [Schedule](#schedule)
   - [Workshop Introduction Video from December 2024](#workshop-introduction-video-from-december-2024)
- [Basic setup reminder](#basic-setup-reminder)
- [Instructional Crew](#instructional-crew)
- [Support](#support)

**Table of Contents for 01.5-documentation**
- [Documentation access](#documentation-access)
- [DUNE tools list](#dune-tools-list)
- [Docdb (Requires FNAL SSO)](#docdb-(requires-fnal-sso))
- [DUNE wiki (Requires FNAL SSO)](#dune-wiki-(requires-fnal-sso))
   - [Tutorials list on the wiki](#tutorials-list-on-the-wiki)
- [CERN EDMS](#cern-edms)
- [Github repositories](#github-repositories)
- [DUNE Computing FAQ](#dune-computing-faq)

**Table of Contents for 02-storage-spaces**
- [This is an updated version of the 2023 training](#this-is-an-updated-version-of-the-2023-training)
      - [Live Notes](#live-notes)
   - [Workshop Storage Spaces Video from December 2024](#workshop-storage-spaces-video-from-december-2024)
- [Introduction](#introduction)
- [Vocabulary](#vocabulary)
- [Interactive storage volumes (mounted on dunegpvmXX.fnal.gov or lxplus.cern.ch)](#interactive-storage-volumes-(mounted-on-dunegpvmxx.fnal.gov-or-lxplus.cern.ch))
   - [Your home area](#your-home-area)
      - [at Fermilab](#at-fermilab)
      - [at CERN](#at-cern)
   - [Locally mounted volumes](#locally-mounted-volumes)
   - [Network Attached Storage (NAS)](#network-attached-storage-(nas))
      - [At Fermilab](#at-fermilab)
      - [At CERN](#at-cern)
   - [Grid-accessible storage volumes](#grid-accessible-storage-volumes)
      - [Persistent dCache](#persistent-dcache)
      - [Scratch dCache](#scratch-dcache)
      - [Tape-backed dCache](#tape-backed-dcache)
      - [Rucio Storage Elements](#rucio-storage-elements)
   - [CVMFS](#cvmfs)
   - [What is my quota?](#what-is-my-quota)
      - [Your home area at FNAL](#your-home-area-at-fnal)
      - [Your home area at CERN](#your-home-area-at-cern)
      - [The /app/ and /data/ areas at FNAL](#the-/app/-and-/data/-areas-at-fnal)
      - [EOS at CERN](#eos-at-cern)
      - [Fermilab dCache](#fermilab-dcache)
- [Summary on storage spaces](#summary-on-storage-spaces)
- [Monitoring and Usage](#monitoring-and-usage)
- [Commands and tools](#commands-and-tools)
   - [ifdh](#ifdh)
   - [xrootd](#xrootd)
   - [What is the right xroot path for a file.](#what-is-the-right-xroot-path-for-a-file.)
   - [The df command](#the-df-command)
- [Quiz](#quiz)
- [Useful links to bookmark](#useful-links-to-bookmark)

**Table of Contents for 02.3-cvmfs**
- [CVMFS](#cvmfs)
- [Restrictions](#restrictions)
- [Useful links to bookmark](#useful-links-to-bookmark)

**Table of Contents for 03-data-management**
- [Session Video](#session-video)
      - [Live Notes](#live-notes)
- [Introduction](#introduction)
   - [What we need to do to produce accurate physics results](#what-we-need-to-do-to-produce-accurate-physics-results)
   - [How we do it ?](#how-we-do-it-)
   - [How do I use this.](#how-do-i-use-this.)
- [How to find and access official data](#how-to-find-and-access-official-data)
- [Official datasets <a name="Official_Datasets"></a>](#Official_Datasets)
   - [Fast web catalog queries](#fast-web-catalog-queries)
   - [Command line tools and advanced queries](#command-line-tools-and-advanced-queries)
   - [metacat web interface](#metacat-web-interface)
   - [Example of finding reconstructed Monte Carlo](#example-of-finding-reconstructed-monte-carlo)
   - [you can use the web data catalog to do advanced searches](#you-can-use-the-web-data-catalog-to-do-advanced-searches)
- [What is metacat?](#what-is-metacat)
   - [Find a file in metacat](#find-a-file-in-metacat)
   - [Example of doing a metacat search](#example-of-doing-a-metacat-search)
   - [then do queries to find particular groups of files](#then-do-queries-to-find-particular-groups-of-files)
   - [What do those fields mean?](#what-do-those-fields-mean)
   - [find out how much raw data there is in a run using the summary option](#find-out-how-much-raw-data-there-is-in-a-run-using-the-summary-option)
   - [Fast web catalog queries](#fast-web-catalog-queries)
   - [Command line tools and advanced queries](#command-line-tools-and-advanced-queries)
   - [metacat web interface](#metacat-web-interface)
   - [Example of finding reconstructed Monte Carlo](#example-of-finding-reconstructed-monte-carlo)
   - [you can use the web data catalog to do advanced searches](#you-can-use-the-web-data-catalog-to-do-advanced-searches)
   - [find out how much data there is in a dataset](#find-out-how-much-data-there-is-in-a-dataset)
   - [What describes a dataset?](#what-describes-a-dataset)
   - [What files are in that dataset and how do I use them?](#what-files-are-in-that-dataset-and-how-do-i-use-them)
- [Finding those files on disk](#finding-those-files-on-disk)
- [Getting file locations using Rucio](#getting-file-locations-using-rucio)
   - [What is Rucio?](#what-is-rucio)
   - [You will need to authenticate to read files](#you-will-need-to-authenticate-to-read-files)
- [Accessing `rucio` and `justin` require a bit more](#accessing-`rucio`-and-`justin`-require-a-bit-more)
   - [getting a token for xroot access in AL9](#getting-a-token-for-xroot-access-in-al9)
   - [finding a file](#finding-a-file)
- [More finding files by characteristics using metacat](#more-finding-files-by-characteristics-using-metacat)
- [Accessing data for use in your analysis](#accessing-data-for-use-in-your-analysis)
- [Quiz](#quiz)
- [Useful links to bookmark](#useful-links-to-bookmark)

**Table of Contents for 03.2-UPS**
- [What is UPS and why do we need it?](#what-is-ups-and-why-do-we-need-it)
   - [UPS basic commands](#ups-basic-commands)

**Table of Contents for 04-Spack**
- [What is Spack and why do we need it?](#what-is-spack-and-why-do-we-need-it)
- [Minimal spack for root analysis and file access](#minimal-spack-for-root-analysis-and-file-access)
- [A more flexible environment with more packages but you have to make choices of versions](#a-more-flexible-environment-with-more-packages-but-you-have-to-make-choices-of-versions)
   - [Spack basic commands](#spack-basic-commands)

**Table of Contents for 05-end-of-basics**
- [You can ask questions here:](#you-can-ask-questions-here)
- [You can continue on with these additional modules.](#you-can-continue-on-with-these-additional-modules.)

**Table of Contents for 05.1-improve-code-efficiency**
- [Improve your Code efficiency](#improve-your-code-efficiency)
   - [Session Video](#session-video)
   - [Live Notes](#live-notes)
   - [Code Make-over](#code-make-over)
   - [CPU optimization:](#cpu-optimization)
- [Memory optimization:](#memory-optimization)
- [I/O optimization:](#i/o-optimization)
- [Build time optimization:](#build-time-optimization)
- [Workflow optimization:](#workflow-optimization)
- [Software readability and maintainability:](#software-readability-and-maintainability)
- [Coding for Thread Safety](#coding-for-thread-safety)

**Table of Contents for 10-closing-remarks**
- [Video Session](#video-session)
- [Two Days of Training](#two-days-of-training)
- [Survey time!](#survey-time!)
- [Next Steps](#next-steps)
- [Long Term Support](#long-term-support)

**Table of Contents for about**

**Table of Contents for al9_setup**
- [How to set up a basic session in al9](#how-to-set-up-a-basic-session-in-al9)
   - [a tip](#a-tip)
- [Set up software](#set-up-software)
- [Get a token](#get-a-token)
   - [getting a token for xroot access in AL9](#getting-a-token-for-xroot-access-in-al9)

**Table of Contents for al9_speedrun**
- [2025 Speedrun of AL9 setup and test](#2025-speedrun-of-al9-setup-and-test)
   - [getting a token for xroot access in AL9](#getting-a-token-for-xroot-access-in-al9)

**Table of Contents for Common-Error-Messages**
- [Common Error Messages](#common-error-messages)
   - [Error: /usr/bin/xauth: unable to write authority file](#error-/usr/bin/xauth-unable-to-write-authority-file)
   - [bash: setup: command not found](#bash-setup-command-not-found)
   - [SyntaxError: future feature annotations is not defined](#syntaxerror-future-feature-annotations-is-not-defined)
   - [Spack : Error: somecode matches multiple packages](#spack--error-somecode-matches-multiple-packages)

**Table of Contents for ComputerSetup**
- [Computer setup](#computer-setup)
   - [Back up your machine](#back-up-your-machine)
   - [Open a unix terminal window](#open-a-unix-terminal-window)
   - [Learn how to use the Unix Shell](#learn-how-to-use-the-unix-shell)
   - [Install an x-windows emulator](#install-an-x-windows-emulator)
      - [MacOS](#macos)
      - [Unix](#unix)
      - [Windows](#windows)
   - [Extra - Get a code editor](#extra---get-a-code-editor)
      - [OSX](#osx)
      - [Unix](#unix)
      - [Windows](#windows)
- [Useful Links](#useful-links)

**Table of Contents for figures**

**Table of Contents for guide**
   - [Instructor Guide](#instructor-guide)

**Table of Contents for helpers**

**Table of Contents for InstallConda**
- [Installing conda and root](#installing-conda-and-root)
- [Download miniconda](#download-miniconda)
- [Install conda](#install-conda)
- [Making an environment with root in it](#making-an-environment-with-root-in-it)
- [Try out your new environment](#try-out-your-new-environment)
- [Testing](#testing)

**Table of Contents for OfficialDatasets**
- [Official datasets <a name="Official_Datasets"></a>](#Official_Datasets)
   - [Fast web catalog queries](#fast-web-catalog-queries)
   - [Command line tools and advanced queries](#command-line-tools-and-advanced-queries)
   - [metacat web interface](#metacat-web-interface)
   - [Example of finding reconstructed Monte Carlo](#example-of-finding-reconstructed-monte-carlo)
   - [you can use the web data catalog to do advanced searches](#you-can-use-the-web-data-catalog-to-do-advanced-searches)

**Table of Contents for pnfs2xrootd**

**Table of Contents for putty**
   - [PuTTY](#putty)
- [Kerberos Ticket Manager](#kerberos-ticket-manager)
- [Xming](#xming)
- [Configuring PuTTY](#configuring-putty)

**Table of Contents for setup_ruby**

**Table of Contents for setup**
- [Objectives](#objectives)
- [Requirements](#requirements)
- [Step 1: DUNE membership](#step-1-dune-membership)
- [Step 2: Getting accounts](#step-2-getting-accounts)
   - [With FNAL](#with-fnal)
   - [With CERN](#with-cern)
- [Step 3: Mission setup (rest of this page)](#step-3-mission-setup-(rest-of-this-page))
- [0. Basic setup on your computer.](#0.-basic-setup-on-your-computer.)
- [1. Kerberos business](#1.-kerberos-business)
- [2. ssh-in](#2.-ssh-in)
- [3. Get a clean shell](#3.-get-a-clean-shell)
- [Software setup <a name="software_setup"></a>](#software_setup)
   - [4.1 Setting up DUNE software - Scientific Linux 7 version <a name="SL7_setup"></a>](SL7setup)
   - [Caveats for later](#caveats-for-later)
   - [4.2 Setting up DUNE software - Alma9 version <a name="AL9_setup"></a>](#AL9_setup)
   - [Caveats for later](#caveats-for-later)
- [4.2 Setting up DUNE software - Alma9 version](#4.2-setting-up-dune-software---alma9-version)
   - [Caveats](#caveats)
- [5. Exercise! (For SL7 - it's easy)](#5.-exercise!-(for-sl7---it's-easy))
- [5. Exercise! (For AL9 - it's easy)](#5.-exercise!-(for-al9---it's-easy))
- [6. Getting setup for streaming and grid access](#6.-getting-setup-for-streaming-and-grid-access)
   - [Tokens method <a name="tokens"></a>](#tokens)
      - [1. Get and store your token](#1.-get-and-store-your-token)
      - [2. Tell the system where your token is](#2.-tell-the-system-where-your-token-is)
- [Set up on CERN machines <a name="setup_CERN"></a>](#setup_CERN)
   - [1. Setup in Alma9](#1.-setup-in-alma9)
   - [2. For SL7](#2.-for-sl7)
      - [Source the DUNE environment SL7 setup script](#source-the-dune-environment-sl7-setup-script)
   - [3. Getting authentication for data access](#3.-getting-authentication-for-data-access)
   - [4. Access tutorial datasets](#4.-access-tutorial-datasets)
   - [5. Notify us](#5.-notify-us)
- [Useful Links](#useful-links)

**Table of Contents for sites**

**Table of Contents for sl7_setup**
- [launch the Apptainer](#launch-the-apptainer)
- [then do the following to set up DUNE code](#then-do-the-following-to-set-up-dune-code)
- [then do the following to get authentication to remote data and batch systems](#then-do-the-following-to-get-authentication-to-remote-data-and-batch-systems)
- [Accessing `rucio` and `justin` require a bit more](#accessing-`rucio`-and-`justin`-require-a-bit-more)

**Table of Contents for sl7_speedrun**
- [Accessing `rucio` and `justin` require a bit more](#accessing-`rucio`-and-`justin`-require-a-bit-more)
- [check root](#check-root)
- [check rucio](#check-rucio)

**Table of Contents for Tokens**
- [SL7 Tokens <a name="SL7_token"></a>](#SL7_token)
- [Accessing `rucio` and `justin` require a bit more](#accessing-`rucio`-and-`justin`-require-a-bit-more)
- [AL9 Tokens <a name="AL9_token"></a>](#AL9_token)
   - [getting a token for xroot access in AL9](#getting-a-token-for-xroot-access-in-al9)

**Table of Contents for TutorialsMasterList**
- [[Computing Basics](https://dune.github.io/computing-basics/)](#[computing-basics](https//dune.github.io/computing-basics/))
- [[The Justin Workflow System](https://dunejustin.fnal.gov/docs/)](#[the-justin-workflow-system](https//dunejustin.fnal.gov/docs/))
- [[LArTPC Reconstruction Training](https://indico.ph.ed.ac.uk/event/268/)](#[lartpc-reconstruction-training](https//indico.ph.ed.ac.uk/event/268/))
- [[FAQ](https://github.com/orgs/DUNE/projects/19/views/1)](#[faq](https//github.com/orgs/dune/projects/19/views/1))

**Table of Contents for Windows**
- [Instructions for running remote terminal sessions on unix machines from Windows](#instructions-for-running-remote-terminal-sessions-on-unix-machines-from-windows)
- [Kerberos Ticket Manager](#kerberos-ticket-manager)
- [Terminal emulators](#terminal-emulators)
   - [MobaXterm](#mobaxterm)
   - [PuTTY/Xming](#putty/xming)
      - [PuTTY](#putty)
      - [Xming with PuTTY](#xming-with-putty)
      - [Configuring PuTTY for remote use](#configuring-putty-for-remote-use)
- [Done!](#done!)