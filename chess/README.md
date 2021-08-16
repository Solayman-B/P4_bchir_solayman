# P4_bchir_solayman

Summaries
---------

* General description
* Requirements
* Installation
* Run the script

General description
-------------

This script is a chess tournament manager, you can add players, date, place, and choose between multiples games modes.
It uses Swiss method to organize the different rounds. You can save and continue a tournament on the go, and reuse the players from others tournaments.
All the information are automatically saved in a local database with TinyDB.

Requirements
---------

This script uses the following packets:

* python-dateutil==2.8.1
* tinydb==4.5.0
* virtualenv==20.4.6

Installation
------------

First, you can download this project by :

clicking on « code » then « download ZIP »

or [click here to download it directly](https://github.com/Solayman-B/P4_bchir_solayman/archive/refs/heads/main.zip)

Unzip the file when the download is completed

You can also install Git via this link and use :

    gh repo clone Solayman-B/P4_bchir_solayman


To use this script properly, you need to use [python3](https://www.python.org/downloads/)

Then you can create a virtual environment:

    python3 -m venv env # env is the name of the directory, but you can choose another one if you want

On Windows, run:

    env\Scripts\activate.bat

On Unix or macOS, run:

    source env/bin/activate

And to deactivate simply use:

    deactivate

You can install all the required paquets with:

    pip install -r requirements.txt

To generate a flake8-html file, go on the folder containing the project and use:

    flake8 --max-line-length 119 --format=html --htmldir=flake-report chess/

it will generate a flake-report folder containing the html file

Run
---

Go on the folder containing the project and use `python3 main.py` to run the code and follow the inscuctions.


