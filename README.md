# git-cmd

Simple shortcuts for flash actions.

## Installation

    pip install shooortcuts

Or install from source:

    git clone https://github.com/imhuwq/shooortcuts.git
    cd shooortcuts
    pip install -e .

## Commands

### `ass` (Auto Save State)

Creates a temporary commit with an auto-generated version string:

    $ ass
    Created temporary commit with version: __init__    # If this is first commit
    Created temporary commit with version: a1b2c3d     # If previous commit exists

Version string rules:
- If no commits exist: uses "__init__"
- If last commit was made by `ass`: reuses its version string
- Otherwise: uses the short hash of the last commit

### `css` (Commit Saved State)

Converts temporary commits into a permanent commit:

    $ css "feat: implement new feature"

Behavior:
1. If the oldest temporary commit is an "__init__" commit:
   - Replaces it with the new commit
   - Example: `__init__` -> `feat: implement new feature`

2. If there's a non-temporary commit before temporary commits:
   - Resets to that commit
   - Creates new commit with all changes
   - Example: `normal -> temp1 -> temp2` becomes `normal -> new`

3. If all commits are temporary:
   - Creates new commit replacing all temporary commits
   - Example: `temp1 -> temp2` becomes `new`

## Use Case

Typical workflow:

    # Make some changes
    $ ass                              # Save temporary state
    Created temporary commit with version: __init__

    # Make more changes
    $ ass                              # Save another state
    Created temporary commit with version: __init__

    # Ready to commit properly
    $ css "feat: complete implementation"   # Convert to proper commit
    Created commit: feat: complete implementation

This allows you to:
1. Save work-in-progress changes frequently
2. Convert them into a clean commit when ready
3. Maintain a clean git history 
