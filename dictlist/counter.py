import requests
response = requests.get(f'https://api.github.com/repos/kubernetes/kubernetes/pulls')

pullrequest =response.json()
pr_creators = {}
for pull in pullrequest:
    creator = pull["user"]["login"]
    if creator in pr_creators:
        pr_creators[creator] += 1
    else:
        pr_creators[creator] = 1

    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")