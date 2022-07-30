# Quickbooks XML Bill Creation Code

Folder Structure:

- files: All the new files must be dumped here
- inserted-files: All the files that were successfully inserted to the database must be dumped here
- secrets: All the Quickbooks Secrets are stored here
- logs: All the processing info is stored here

Process to **Setup**:

Command to setup virtual environment:
Windows System
`source venv/bin/activate`

Note:
In case at any point you see NoModuleError:
just do: `pip install <MODULE_NAME>`

- python -m venv qbenv
- qbenv/Scripts/activate
- pip install -r requirements.txt
  You need to copy it from oAuth playground: https://developer.intuit.com/app/developer/playground

- pip install -r requirements.txt
