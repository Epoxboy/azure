# Azure related scripts
1, generate_storage_sas_tokens_script.py
it'll generate storage sas tokens, just be ware of the access policy will be cleared everytime when you run set_container_acl ()and you have to make sure you use the same id name and permissions in order to not remove the old access policies when you generate the new sas.


