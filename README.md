BrumHack7
=========

My project basically uses data obtained from theyworkforyou and the publicwhip
to try and figure out how MPs will vote based on how it categorizes different
debates (which were used as proxies for the actual bills text).

I got about 60% accuracy, which isn't the best but you need better data.

Usage
-----

Download data from:
http://www.publicwhip.org.uk/project/data.php
https://www.theyworkforyou.com/pwdata/scrapedxml/debates/

Get which term you want from the first one (both the .txt and .dat)
The .txt contains the labels. Use this later to search for MPs in the output.

Run magic.py on the termdata after you have all the debates.
This produces a file in the directory below, which is used to train the model.

Run train.py, and after about 2 mins you should have a valid model.

