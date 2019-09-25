class MockGithub:
    def __init__(self, repo_dict):
        self.user = MockUser(repo_dict)

    def get_user(self, userId):
        return self.user


class MockUser:
    def __init__(self, repo_dict):
        repos = []
        for key in repo_dict:
            repos.append(MockRepo(key, repo_dict[key]))
        self.repos = repos

    def get_repos(self):
        return self.repos


class MockRepo:
    def __init__(self, full_name, commits):
        self.full_name = full_name
        self.commits = MockCommits(commits)

    def get_commits(self):
        return self.commits


class MockCommits:
    def __init__(self, commits):
        self.totalCount = commits
