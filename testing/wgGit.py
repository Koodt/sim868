#!/usr/bin/python3

from git import Repo

class GitClass(object):
    def __init__(self):
        pass

    def dlRepo(self, url, path):
        self.url = url
        self.path = path
        self._repo = Repo.clone_from(self.url, self.path)

    def createBranch(self, targetRepo, branch):
        self.repoTarget = targetRepo
        self.branch = branch
        self.repo = Repo(self.targetRepo.working_tree_dir)
        self.new_branch = self.repo.create_head(self.branch)

    @property
    def repo(self):
        if self._repo is None:
            self.dlRepo()
        return self._repo


if __name__ == "__main__":
    wgClass = GitClass()
#    wgClass.dlRepo("https://github.com/Koodt/sim868.git", "/srv/kill")
    wgClass.createBranch("/srv/kserver/sim868", "test")
