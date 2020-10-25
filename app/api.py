import requests


from collections import defaultdict


class ProfileNotAvailable(Exception):
    """Could not find profile."""
    pass


class ProfileData(object):
    """Universal Github / Bitbucket profile data adapter."""

    def __init__(self, username):
        self.username = username
        self.github_repos = None
        self.bitbucket_repos = None

    def fetch_profile_data(self):
        """fetch and format profile data."""
        self.load_bitbucket()
        self.load_github()

        languages = defaultdict(int)
        watchers = 0
        total_repos = 0
        original_repos = []
        forked_repos = []

        for repo in self.bitbucket_repos:
            key = repo['language'].lower() if repo.get('language') else 'n/a'
            languages[key] += 1
            original_repos.append(repo)
            total_repos += 1
        for repo in self.github_repos:
            key = repo['language'].lower() if repo.get('language') else 'n/a'
            languages[key] += 1
            watchers += repo.get('watchers')
            if repo.get('fork'):
                forked_repos.append(repo)
            else:
                original_repos.append(repo)
            total_repos += 1

        return {
            'num_total_repos': total_repos,
            'num_original_repos': len(original_repos),
            'num_forked_repos': len(forked_repos),
            'languages': languages,
            'watchers': watchers,
            'original_repos': original_repos,
            'forked_repos': forked_repos
        }

    def load_github(self):
        """request github profile api endpoint."""
        url = 'https://api.github.com/users/{}/repos'.format(self.username)
        response = requests.get(url)
        if response.status_code == 200:
            self.github_repos = response.json()
        else:
            raise ProfileNotAvailable

    def load_bitbucket(self):
        """request bitbucket profile api endpoint."""
        url = 'https://api.bitbucket.org/2.0/repositories/{}'.format(self.username)
        response = requests.get(url)
        if response.status_code == 200:
            self.bitbucket_repos = response.json()['values']
        else:
            raise ProfileNotAvailable
