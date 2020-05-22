import requests   # import requests package

r = requests.get('https://api.github.com/') # paste the link and make sure the HTTP link is 200 block or succesful or not
print(r.status_code) #print the status_code
