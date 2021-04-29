
Common API use-cases:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. 

http://127.0.0.1:8000/?group_by=channel,country&order_by=clicks&date_to=2017-06-01&order_tpe=desc

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

http://127.0.0.1:8000/?group_by=date&order_by=date&date_from=2017-05-01&date_to=2017-05-31&os=ios

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

http://127.0.0.1:8000/?group_by=os&order_by=revenue&date_from=2017-06-01&date_to=2017-06-01&order_tpe=desc&country=US

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

http://127.0.0.1:8000/?group_by=channel&order_by=cpi&order_tpe=desc&country=CA
