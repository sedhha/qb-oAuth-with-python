# Quickbooks XML Bill Creation Code

Folder Structure:

- files: All the new files must be dumped here
- inserted-files: All the files that were successfully inserted to the database must be dumped here
- secrets: All the Quickbooks Secrets are stored here
- logs: All the processing info is stored here

Process to **Setup**:

Process to clone the repository:
```
git clone https://github.com/sedhha/qb-oAuth-with-python
cd qb-oAuth-with-python
```
Command to setup virtual environment:
Windows System
`source venv/bin/activate`

Note:
In case at any point you see NoModuleError:
just do: `pip install <MODULE_NAME>`

- python -m venv qbenv
- qbenv/Scripts/activate (For windows: qbenv\Scripts\activate)
- pip install -r requirements.txt (python -m pip install -r requirements.txt) # if it says pip isn't recognized
  You need to copy it from oAuth playground: https://developer.intuit.com/app/developer/playground

- pip install -r requirements.txt

Once pip installation is successful you need to set the secrets and once all of the secrets config is done, you can run directly python main.py.
