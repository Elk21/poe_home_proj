from git import Repo, Commit
import os, io

PATH_TO_TFT_GIT_REPO = "tft_git_repo"  # set path to your TFT git repo
GIT_URL = "https://github.com/The-Forbidden-Trove/tft-data-prices.git"
FILE_NAMES = [
    "bulk-beasts.json",
    "bulk-breach.json",
    "bulk-compasses.json",
    "bulk-expedition.json",
    "bulk-heist.json",
    "bulk-invitation.json",
    "bulk-legion-jewels.json",
    "bulk-lifeforce.json",
    "bulk-maps.json",
    "bulk-sets.json",
    "bulk-simulacrum.json",
    "bulk-stacked-deck.json",
    "bulk-vessel.json",
    "bulk-watcher's-eye.json",
    "hideout.json",
    "service.json",
]


def extract_file_from_commit(commit: Commit, file_name: str) -> None:
    """
    Extracts file from git commit with given name.

    Args:
        commit (git.Commit): The commit to extract file from.
        file_name (str): The name of the file to extract.
    """
    source_file = commit.tree / f"lsc/{file_name}"
    target_dir = f'data/tft/{file_name.split(".")[0]}'
    tagret_file = f"{commit}.json"

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with io.BytesIO(source_file.data_stream.read()) as f:
        with open(f"{target_dir}/{tagret_file}", "wb+") as f2:
            f2.write(f.read())


def get_tft_history_files(
    file_names: list[str] = FILE_NAMES, n: int = 5
) -> None:
    """
    Fetches `n` commits from the TFT price repo and extracts the specified files from them.

    Args:
        log (str): The output of git log command.
        file_names (List[str]): Names of the files to extract from each commit.
        n (int, optional): Number of commits to fetch from the repo. Defaults to 3.
    """
    for i, commit in enumerate(repo.iter_commits()):
        if i == n:
            break
        print(i, commit)
        commit = repo.commit(commit)

        for f in file_names:
            extract_file_from_commit(commit, f)

if __name__=="__main__":
    if not os.path.exists(PATH_TO_TFT_GIT_REPO):
        Repo.clone_from(GIT_URL, PATH_TO_TFT_GIT_REPO)
    repo = Repo(PATH_TO_TFT_GIT_REPO)
    log = repo.git.log()
    get_tft_history_files() 

