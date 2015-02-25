The transfer of experimental data from the Ross Lab to Midway can be run as an `sbatch` script that executes a set of globus commands nightly on Midway.

Taka (`kazutaka`) was made a member of the `cron-account` group, enabling him to
submit the required `sbatch` script.   The [`cron_template.sbatch`](https://github.com/rcc-uchicago/uc-xromm/blob/master/globus/transfer_scripts/cron-template.sbatch) is a basic template that can be used for this.

The nightly transfers will require Taka to have an SSH public key registered with Globus online. The public/private key pair will be generated on Midway.  See the [config
steps](config.md) required to generate the appropriate key pairs.  Note that the `sbatch` script should reference this key.

Steps to setup the transfer script:

- [x] generate SSH keypairs for each source system
- [x] copy each public key to the respective source system
- [x] update the `sbatch` template to reflect SSH key pairs and source file paths
- [x] test individual transfer commands in the `sbatch` script to ensure they work
- [ ] rename and submit the resulting `sbatch` script.
