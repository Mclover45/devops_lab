import getpass
import requests
import sys
user = input("Input Github Login: ")
password = getpass.getpass()
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls/48'
req = requests.get(url, auth=(user, password))
req = req.json()
ans = (sys.argv)
print(ans)
if str(ans) == "['pr-stats.py', '--d']":
    print('Created at:', req['created_at'])
elif str(ans) == "['pr-stats.py', '--u']":
    print('Created by:', req['user']['login'])
elif str(ans) == "['pr-stats.py', '--c']":
    print('Closed at:', req['closed_at'])
elif str(ans) == "['pr-stats.py', '--s']":
    print('Status:', req['labels'][0]['name'])
elif str(ans) == "['pr-stats.py', '--help']":
    print("Who created --u , When created --u, When closed --c, Status --s")
