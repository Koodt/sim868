#!/usr/bin/python3

import git

class GitClass(object):
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self._repo = None

    def dlRepo(self):
        self._repo = git.Repo.clone_from(self.url, self.path)

    @property
    def repo(self):
        if self._repo is None:
            self.fetch_repo()
        return self._repo


if __name__ == "__main__":
    GitClass("https://github.com/Koodt/sim868.git", "/srv/kill")
