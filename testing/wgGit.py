#!/usr/bin/python3

import git

class GitClass(object):
    def __init__(self):

    def dlRepo(self, url, path):
        self.url = url
        self.path = path
        self._repo = git.Repo.clone_from(self.url, self.path)

    @property
    def repo(self):
        if self._repo is None:
            self.fetch_repo()
        return self._repo


if __name__ == "__main__":
    loader = GitClass()
    loader.dlRepo("https://github.com/Koodt/sim868.git", "/srv/kill")
