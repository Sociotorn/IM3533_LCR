# IM3533_LCR
Backend Python code for communicating with an LCR meter

## Setting up the virtual environment on Linux

### Create the virtual environment

`python3 -m venv ./venv`

### Activate the virtual environment

`source venv/bin/activate`

### Check interpreter

`python3 -c "import sys; print(sys.executable)"`

### Install Dependencies

`python3 -m pip install -r requirements.txt`

## Setting up the virtual environment on Windows

### Create the virtual environment

`py -m venv ./venv`

### Activate the virtual environment

`.\venv\Scripts\activate`

### Check interpreter

`python -c "import sys; print(sys.executable)"`

### Install Dependencies

`python -m pip install -r requirements.txt`

## Converting Python to Executable on Linux

### Install PyInstaller

`pip install pyinstaller`

### Generate Executable

`pyinstaller -F ./src/main.py`

### Run Executable

`./dist/main`