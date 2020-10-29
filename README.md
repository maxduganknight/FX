# FX
This is a personal project I started to keep track of foreign exchange variation. I was tired of checking the 
exchange rate manually every day and would sometimes forget so I tried to automate the process. 

The fx_notifier script uses a python library called forex to pull an exchange rate daily and notify a 
specified person via email if the exchange rate is above a certain threshold. I am using this code to help
decide when to do a foreign currency exchange between USD and GBP. 

I have set up a cron jobs on AWS to run the script at the same time every day (an hour after the forex package 
pulls its updated exchange rate data at 15:00 CET) and alert me about the USD to GBP exchange rate. I have 
also set up cron jobs to alert others about various exchange rates at their request. 
