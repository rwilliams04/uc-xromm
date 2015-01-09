The transfer of experimental data from the Ross Lab to Midway can be run as an `sbatch` script that executes a set of globus commands nightly on Midway.

Taka (`kazutaka`) was made a member of the `cron-account` group, enabling him to
submit the required `sbatch` script.   The [`cron_template.sbatch`](cron_template.sbatch) is a basic template that can be used for this.

The nightly transfers will require Taka to have SSH public keys on each source
system that pair with a private key generated on Midway.  See the [config
steps](config.md) required to generate the appropriate key pairs.  Note that the `sbatch` script should reference these keys.

Steps to setup the transfer script:

- [x] generate SSH keypairs for each source system
- [x] copy each public key to the respective source system
- [ ] update the `sbatch` template to reflect SSH key pairs and source file paths
- [ ] test individual transfer commands in the `sbatch` script to ensure they work
- [ ] rename and submit the resulting `sbatch` script.
