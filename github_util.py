from prettytable import PrettyTable


def get_repo_dict(user_id: str, client) -> dict:
    user = client.get_user(user_id)
    repo_dict = {}
    for repo in user.get_repos():
        repo_dict[repo.full_name] = repo.get_commits().totalCount
    return repo_dict


def print_pretty_repo_table(user_id: str, repo_dict: dict, description: str):
    repo_table = PrettyTable()
    repo_table.field_names = ["Repo Name", "Number of Commits"]
    for repo_name in repo_dict:
        repo_table.add_row([repo_name, repo_dict[repo_name]])
    print("\n" + description + " Repo Report For User '" + user_id + "'\n" + repo_table.get_string())
