# Open source components don't belong in hosted repos!
This repository contains a script to check if you have open source (components) artifacts stored in your hosted repositories.
The generated file can then be used to evaluate the components using the Nexus Platform.

## Requirements
* Python3
* NXRM3 OSS or PRO
* Local build of [Sonatype Hashbrowns](sonatype-nexus-community/hashbrowns). \
  Hashbrowns is a utility for scanning sha1 sums with Sonatype's Nexus IQ Server.

‼ - Large registries with NX3 might cause an orient error. 
If you run into this contact your Sonatype CS for help

## Instructions

### Download and build Sonatype Hashbrowns from source - https://github.com/sonatype-nexus-community/hashbrowns
```
git clone https://github.com/sonatype-nexus-community/hashbrowns.git
cd hashbrowns
make
```

### Step 1: Customise values in `hashbrowns-order.py`
You'll need to modify the script to include 
1. Auth creds or tokens from your NXRM. (`USER` and `TOKEN`)
1. URL to your Nexus (`REPO_HOSTNAME`)
1. Hosted Repository to evaluate`REPO`

You'll find examples of all in the script.

### Step 2: Create new virtual environment
```python
python3 -m venv venv
```
### Step 3: Activate your virtual environment
Do this in your terminal or by using your favorite IDE
#### Windows
```
my-venv\Scripts\activate.bat
```

#### MacOs *NIX Linux
```bash
source my-venv/bin/activate
```

### Step 4: Install dependencies
```python
pip install -r requirements.txt
```

### Step 5: Run script
To run the script simply type - results will be piped to the file specified.
```python
 python3 hasbrowns-order.py > hashbrowns-order.txt
 ````

### Step 6: Run hashbrowns with the generated file

```python
cd <hasbrowns directory>
./hashbrowns fry --application att-hashes  --token "Nexus!23"  --server-url "http://localhost:8070" --user "admin" --stage stage-release --path <path>/hashbrowns-order.txt
 ````

### Step 7: Review the report in Nexus IQ Server
The report URL is printed after the report runs.  Prepend the report url with the IQ server hostname and port.
* The report will list public open source components found in the hosted repositories.  These components should be removed from the hosted repositories and served by proxy repositories. 