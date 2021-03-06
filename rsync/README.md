The transfer of experimental data from the Ross Lab to Midway will be run as an `sbatch` script that executes a set of rysnc commands nightly on Midway.

Taka (`kazutaka`) was made a member of the `cron-account` group, enabling him to
submit the required `sbatch` script.   The [`cron_template.sbatch`](cron_template.sbatch) is a basic template that can be used for this.

The nightly transfers will require Taka to have SSH public keys on each source
system that pair with a private key generated on Midway.  See the [config
steps](config.md) required to generate the appropriate key pairs.  Note that the `sbatch` script references these keys.

Steps for Taka to setup the transfer script:

1. generate SSH keypairs for each source system
2. copy each public key to the respective source system
3. update the `sbatch` template to reflect SSH key pairs and source file paths
4. rename and submit the resulting `sbatch` script.
