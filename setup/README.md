## For WSL2 Ubuntu:
sudo apt-get update
sudo apt-get install python3-pip
### (Might be needed) sudo apt-get install libpython3-dev
sudo apt-get install python3-venv

## Setting up for environment:
python3 -m venv WSL2setup 
source WSL2setup/bin/activate

### WHY virtual environment? 
straight from stackoverflow:
## USE a venv:

- You're working on one BIG project with multiple people to mitigate versioning issues among the people
- You don't plan on updating your dependencies very often for all projects
- To have a clearer separation of your projects
- To containerize your project (again, for distribution)
- Your portfolio is fairly small (especially in the data science world where packages like Tensorflow are large and used quite frequently across all of them as you'd have to pip install the same package to each venv)
## DO NOT use a venv:
- 
- Your portfolio of projects is large AND requires a lot of heavy dependencies (like tensorflow) to mitigate installing the same package in every venv you create
- You're not distributing your projects across a team of people
- You're actively maintaining your projects and keeping global dependency versions up to date across all of them (maybe I'm the only one who's actually doing this, but whatever)
