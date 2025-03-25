import re
from datetime import datetime

from .common import TEMP_COMMIT_PREFIX, get_repo, get_version_from_last_commit, print_git_log


def fss_command():
    repo = get_repo()

    try:
        current = repo.head.commit
    except (ValueError, TypeError):
        print("No commits to fuck off")
        return

    # Check if all commits are temp commits
    temp_commits = []
    non_temp_commit = None

    while current:
        if re.match(f"{TEMP_COMMIT_PREFIX} .*", current.message):
            temp_commits.append(current)
            current = current.parents[0] if current.parents else None
        else:
            non_temp_commit = current
            break

    if non_temp_commit is None:
        print("Warning: All commits in current branch are temporary commits")
        return

    if not temp_commits:
        print("No temporary commits to fuck off")
        return

    # Get version and create new branch
    version = get_version_from_last_commit()
    new_branch = f"temp/{version}_{datetime.now().strftime('%y%m%d')}"

    # Create and switch to new branch
    repo.git.checkout("-b", new_branch)
    print(f"Created new branch: {new_branch}")

    # Reset main branch to last non-temp commit
    main_branch = repo.active_branch.name
    repo.git.checkout(main_branch)
    repo.git.reset(non_temp_commit.hexsha)
    print(f"Reset {main_branch} to last non-temp commit")

    print_git_log()
