# Purpose
This script can be used to query Thycotic Secret Server to find what folders and secrets do not inherit from parent.

# Setup
Script looks for User, Password, and URL from env variables
```
export THYCOTIC_USER=username
export THYCOTIC_PASS=password
export THYCOTIC_URL=url
```

# Use
Show child folders that do not inherit from parent folder. The parent folder ID is easily available when browsing Thycotic.
```
python main.py folder <id>
```

Show child secrets that do not inherit from parent folder.
```
python main.py secret <id>
