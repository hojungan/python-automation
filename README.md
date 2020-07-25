# python-automation

Automate GitHub repository creation.

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
