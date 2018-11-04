#!/usr/bin/python3

class GitClass(object):
    def __init__(self):
        from git import Repo
        self.Repo = Repo

    def dlRepo(self, url, path):
        self.url = url
        self.path = path
        self._repo = self.Repo.clone_from(self.url, self.path)

    def createNewBranch(self, repoTarget, branch):
        self.repoTarget = repoTarget
        self.branch = branch
        self.repoW = self.Repo(self.repoTarget)
        self.new_branch = self.repoW.create_head(self.branch)

    def selectNeededBranch(self, repoTarget, branch):
        self.repoTarget = repoTarget
        self.branch = branch
        self.repoW = self.Repo(self.repoTarget)
        self.new_branch = self.repoW.heads.checkout(self.branch)

    def selectMasterBranch(self, repoTarget):
        self.repoTarget = repoTarget
        self.repoW = self.Repo(self.repoTarget)
        self.new_branch = self.repoW.heads.master.checkout()

    @property
    def repo(self):
        if self._repo is None:
            self.dlRepo()
        return self._repo


if __name__ == '__main__':
    wgClass = GitClass()
#    wgClass.dlRepo('https://github.com/Koodt/sim868.git', '/srv/kill')
    wgClass.createNewBranch('/srv/kill', 'newBranch')

#    wgClass.selectMasterBranch('/srv/kill')
