import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()


def createNewRepo(reponame):
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    gitHub = Github(username, password)
    user = gitHub.get_user()
    user.create_repo(reponame)
    return user.login


if __name__ == "__main__":
    try:
        projectPath = sys.argv[1]
        newReponame = sys.argv[2]

        login = createNewRepo(newReponame)

        os.system(f'mkdir {newReponame}')
        os.chdir(projectPath + "/" + newReponame)
        os.system(f'echo node_modules/ >> .gitignore')

        commands = [f'echo "# {newReponame}" >> README.md', f'git init', f'git remote add origin https://github.com/{login}/{newReponame}',
                    f'git add .', f'git commit -m "initial commit"', f'git push origin master']

        for c in commands:
            os.system(c)

    except:
        print("Provide Repository Name")
