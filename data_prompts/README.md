This directory contains work related to a command-line client under
development, currently called **xpub**.

* `config.py` - sample configuration file for the `xpub` command-line client.
  Instead of hard-coding a sequence of user prompts in the CLI itself, the
  various prompting sequences will be specified in a config file along these
  lines.

* `new_trial.py` - demo script showing how to create a command-line
  client that presents a series of prompts for collecting user input.
  The demo prompts the user for input needed to create a new trial (name, date,
  description, etc.) and prints out the info collected in JSON format.

* `transfer_scripts\*` - demo scripts for exploring file transfer/scheduling
  features.
