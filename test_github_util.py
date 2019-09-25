import pytest
from github import Github

import github_util
from mock_github_util import MockGithub


# This test operates exclusively on mocks.
@pytest.mark.parametrize(
    "user_id, expected_repos",
    [
        ("User1", {
            "A": 1,
            "B": 11,
            "C": 6,
            "D": 100
        }),
        ("User2", {
            "Z": 999999999,
        }),
        ("User3", {
            "GGG": 0,
        }),
        ("User4", {})
    ],
)
def test_get_mock_repos(user_id, expected_repos):
    assert_get_repos(user_id, expected_repos, MockGithub(expected_repos))


# This test connects to Github
@pytest.mark.parametrize(
    "user_id, expected_repos",
    [
        ("tohearen", {
            "tohearen/2019F-SSW-567-WS": 1,
            "tohearen/2019F-SSW-567-WS-HW-02a": 11,
            "tohearen/2019F-SSW-567-WS-PYTHON": 6,
            "tohearen/ssw555-tm06-17A": 100
        })
    ],
)
def test_get_repos(user_id, expected_repos):
    assert_get_repos(user_id, expected_repos, Github())


def assert_get_repos(user_id, expected_repos, client):
    github_util.print_pretty_repo_table(user_id, expected_repos, "Expected")
    actual_repos = github_util.get_repo_dict(user_id, client)
    github_util.print_pretty_repo_table(user_id, actual_repos, "Actual")
    for repo_name in expected_repos:
        assert actual_repos[repo_name] == expected_repos[repo_name]
