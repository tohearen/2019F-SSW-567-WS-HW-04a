import pytest

import github_util


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
    github_util.print_pretty_repo_table(user_id, expected_repos, "Expected")
    actual_repos = github_util.get_repo_dict(user_id)
    github_util.print_pretty_repo_table(user_id, actual_repos, "Actual")
    for repo_name in expected_repos:
        assert actual_repos[repo_name] >= expected_repos[repo_name]
