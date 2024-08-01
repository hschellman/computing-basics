---
title: Basic Computer Setup  
teaching: 30
exercises: 30
questions:
- How do I get my laptop or desktop set up to do scientific computing
objectives:
- Learn how to use command line tools
- Install software you need to do scientific programing
keypoints:
- This will be useful for a lot of projects
- It is also something almost all people who get paid to program are expected to know well
---

## 0. Back up your machine

We are going to be messing with your operating system at some level so it is extremely wise to do a complete backup of your machine to an external drive right now.

Also turn off automatic updates.  Operating system updates can mess with your setup.  Generally, back up before doing updates so you can revert if necessary.

## 1. Open a unix terminal window

First figure out how to open a terminal on your system.  The Carpentries Shell Training has a [section that explains this][New Shell]

This should be easy on Linux and MacOS but a bit more complicated in Windows.


On Linux use xterm, on MacOS go to Utilities and start a Terminal.

On Windows it's a bit more complicated as the underlying operating system is not a unix variant.  

> We suggest using the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about) (WSL). That page has download instructions.



## 2. Learn how to use the Unix Shell

<!-- First figure out [how to open a terminal on your system][New Shell]
-->

There is a nice tutorial from the Carpentries at: [Unix Shell Basics][Unix Shell Basics].

It tells you how to start a terminal session in Windows, Mac OSX and Unix systems.

Please do that [unix shell tutorial][Unix Shell Basics] to learn about the basic command line.


## 3. Install an x-windows emulator

#### MacOS

MacOS  has a `Terminal` app in `Utilities`

but you need to install [XQuartz][XQuartz]

test it out by typing

~~~
xterm &
~~~
{: .language-bash}

You should get a terminal window. You can close it.


#### Unix

Should already have a terminal

test by doing

~~~
xterm &
~~~
{: .language-bash}

#### Windows

See the information about [Windows]({{ site.baseurl }}/Windows.html) terminal connections. 

- To do Linux locally, many people like to run an instance of [Windows SubSystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about).  But it is non-trivial to set up. 

- Alternatively, if you have access to a remote linux system through your institution you can use the Windows terminal/X-windows connections described in [Windows]({{ site.baseurl }}/Windows.html) to connect to that system and work there. 

> # Note
> You should now be ready to go for the ({{ site.baseurl }}/setup.html) 
{: .callout}

## Extra - Get a compiler/code editor

Although you will mainly be using python to code to begin with, most HEP code is actually C++ and it is good to have access to a C++ compiler.  Bonus is that you normally get a good editor as well.

#### OSX
Compiler/editor: On OSX, you should install [Xcode][Xcode] from the [App store](https://www.apple.com/app-store/).  It will take a lot of disk space. When you try to use it it will ask you to install command line tools.  Do so.

Compiler/editor: Even though Xcode is what you use to compile and has an editor, many people prefer to use the [Visual Studio Code](https://code.visualstudio.com) application from Microsoft for editing/testing code.

You can also use vim or emacs if you are old school.

#### Unix
- Compiler: your compiler will be gcc

- Editor: Heck - just use vim. Or emacs, or [VSCode][Visual Studio Code].

#### Windows
Likely you should load up the full [Visual Studio][Visual Studio] as it has a nice C++ compiler


### Useful Links

[HSF Training Center][HSF Training Center]

[Unix Shell Basics][Unix Shell Basics]

[Git][Git]

[Visual Studio Code][Visual Studio Code]

[Visual Studio][Visual Studio]

[GNU gcc][GNU gcc]

[Xcode][Xcode]

[XQuartz][XQuartz]

[Windows Subsystem for Linux][Windows Subsystem for Linux]

{%include links.md%}

[New Shell]: https://swcarpentry.github.io/shell-novice/#open-a-new-shell
[HSF Training Center]: https://hsf-training.org/training-center/
[Windows Subsystem for Linux]: https://learn.microsoft.com/en-us/windows/wsl/about
[Unix Shell Basics]: https://swcarpentry.github.io/shell-novice/
[Git]: https://swcarpentry.github.io/git-novice
[Visual Studio Code]: https://code.visualstudio.com
[Visual Studio]:https://visualstudio.microsoft.com/vs/
[GNU gcc]: https://gcc.gnu.org
[App Store]: https://www.apple.com/app-store/
[Xcode]: https://developer.apple.com/xcode/
[XQuartz]: https://www.xquartz.org
