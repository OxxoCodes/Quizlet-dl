# Quizlet-dl
Quizlet-dl is a command-line program designed to download and export Quizlets in JSON format. 

This program currently  supports URLs which point directly to a study set or to a user - folders, classes, and premium content are not currently supported.

# Usage

```python quizlet-dl.py [URL] [Save Directory]```

# Dependencies
- Python 3.2+, which can be downloaded [here.](https://www.python.org/downloads/) It's recommended to check "Add Python 3.x to PATH" during installation.
- Selenium, which can be installed by running: ```pip install selenium```
- Firefox, which can be downloaded [here.](https://www.mozilla.org/en-US/firefox/new/)
- Geckodriver, which is distributed with Quizlet-dl. In the case that an updated version is required, Geckodriver can be downloaded [here.](https://github.com/mozilla/geckodriver/releases) Please ensure geckodriver.exe is located in the same directory as quizlet-dl.py
