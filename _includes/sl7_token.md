
To get a token that allows you to access files (and rucio) in SL7

~~~
setup justin
justin time # this just tells justin you want to authenticate
~~~
{: .language-bash}

The first time it will ask you to open a web browser, authenticate and enter the long string it delivers to you. 

~~~
To authorize this computer to run the justin command, visit this page with your
usual web browser and follow the instructions within the next 10 minutes:
https://dunejustin.fnal.gov/authorize/_W_azUJcLhYmAOqClYz9RAsnKbDgzQ6lNA

Check that the Session ID displayed on that page is -cprbbe

Once you've followed the instructions on that web page, you can run the justin
command without needing to authorize this computer again for 7 days.
~~~
{: .output}

That gave you authorization to use justin. Now do the command again to get an actual token.

~~~
justin get-token
~~~
{: .language-bash}

You will have to do this sequence weekly as your justin access expires. 

> ## Note: 
> Despite the name of this command it gets you both a token and a special X.509 proxy and it is the latter you are actually using to talk to rucio in these SL7 examples