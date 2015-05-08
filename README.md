JMeter setup
===
Script to setup JMeter locally.

Dependencies
---
 - [Python](https://www.python.org/) - 2.7.*
 - [virtualenv](https://virtualenv.pypa.io/en/latest/)
 - [pip](https://pip.pypa.io/en/stable/)

If using Debian based systems, this will get you up and running:
  ```
  sudo apt-get install python2.7 python-virtualenv python-pip`
  ```

Local setup
---
  ```
  git clone https://github.com/mccricardo/jmeter_setup.git
  cd jmeter_setup
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

Installing JMeter
---

After running the first command, edit your `config.py` with the desired 
configurations. If the generic configurations didn't change, you should only 
need to update `PATH_TO_INSTALL`.

  ```
  cp config.py.example config.py
  python setup_jmeter.py
  ```