#!/usr/bin/python3
"""
Module to list 10 recent commits of a GitHub repository by owner.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name
    )

    r = requests.get(url)
    commits = r.json()

    if isinstance(commits, list):
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get(
                'author', {}
            ).get('name')
            print("{}: {}".format(sha, author_name))
