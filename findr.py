#!/usr/bin/env python3
import os
import argparse


def find_repo(root, repo):
    repos = []
    for root, dirs, files in os.walk(root):
        if '.git' in dirs and repo in root.split('/')[-1]:
            repos.append(root)
    for repo in repos:
        print(repo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='finds repo(s) in directory recursive'
        )
    parser.add_argument(
            'root',
            help='the root directory from where to search'
        )
    parser.add_argument(
            'repo',
            help='the repo that you are looking for')

    args = parser.parse_args()
    find_repo(args.root, args.repo)
