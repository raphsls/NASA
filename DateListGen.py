import datetime
"""Creates a ranged date list of strings"""

def daterange(x, y):
    date_list = []
    begin = datetime.datetime.strptime(x, "%Y-%m-%d")
    end = datetime.datetime.strptime(y, "%Y-%m-%d")
    step = datetime.timedelta(days=1)
    while begin <= end:
        date_list.append(begin.strftime("%Y-%m-%d"))
        begin += step
    return date_list

if __name__ == "__main__":
    print daterange("2019-08-01", "2019-08-17")
    
