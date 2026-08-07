Token Vault Management {#tms-vault-hierarchy}
=============================================

Token vaults are where merchants store their customer and payment data. A `Business Center` internal user can enable the `TMS` vault.  
Vaults are assigned to an owner, and all data within the vault belongs to the owner. You can grant permission to individual MIDs to create, retrieve, update, and delete tokens within a vault. Created tokens belong to the owner of the vault, not the creator of the token. If you remove a MID from a vault, it can no longer access any tokens within that vault, including tokens created under that MID.
IMPORTANT It is not currently possible to merge vaults, so ensure that merchants are set up with the correct vault by creating a new vault or granting access to an existing vault.
