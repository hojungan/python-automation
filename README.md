# python-automation

Automate GitHub repository creation.
It creates new repository with `.gitignore` and `README.md` files.

_Not sure how to setup on MacOS._
_Anyone who knows how to setup on MacOS, feel free to make adjustment._

# Windows using Git bash

## Step 1- Set up .bashrc

Create `.bashrc` file in `C:\Users\[your user folder]` with below code

```
create() {
  currentDir=$(pwd)
  python [path/to/python-automation/main.py] "$currentDir" "$1"
}
```

Restart `.bashrc` file using `source ~/.bashrc`

## Step 2 - Install Dependencies

Change directory to `/python-automation/`
`pip install requirements.txt`

## Step 3 - Configure .env file

Provide your GitHub username and password to variables in `.env` file

---

From the Git bash you should be able to use the comman like
`create [repository-name]`
