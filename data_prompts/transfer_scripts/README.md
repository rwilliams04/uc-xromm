The `transfer.py` script demonstrates how the Globus transfer python client
library can be utilized for initiating a transfer between predefined endpoints.
The scheduler code, however, is problematic as it spawns a new process for each
transfer task that never gets killed.

The `task.py` script demonstrates the task scheduling logic in isolation.  Try
running this script a few time and then run `ps` to observe the spawned
processes that are left running even after the scheduled task is completed.
