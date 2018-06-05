import os, time
from datetime import datetime, timedelta

from azure.storage.blob import (
     BlockBlobService,
     ContainerPermissions,
)
from azure.storage.common.models import AccessPolicy

def generate_SAS():

        # create a BlockBlobService    
        service = BlockBlobService(account_name=account_name, account_key=account_key)
        
        # create a container, if it already exists, it'll throw an error but keep going to next step
        service.create_container(container_name)
        
        # Set access policy on container
        access_policy_ro = AccessPolicy(permission=container_permissions_ro, expiry=datetime.utcnow() + timedelta(days=+days_until_expiry))
        access_policy_rw = AccessPolicy(permission=container_permissions_rw, expiry=datetime.utcnow() + timedelta(days=+days_until_expiry))

        identifiers = {id_ro: access_policy_ro, id_rw: access_policy_rw}
        
        acl = service.set_container_acl(container_name, signed_identifiers=identifiers)
       
        # Wait 30 seconds for acl to propagate
        time.sleep(30)
       
        # Generate sas with associated access policy
        token_ro = service.generate_container_shared_access_signature(container_name,id=id_ro)  
        token_rw = service.generate_container_shared_access_signature(container_name,id=id_rw)

        # Print out tokens
        print('READ TOKEN IS :')
        print(token_ro)

        print('READ WRITE TOKEN IS :')
        print(token_rw)

       
# Main method.
if __name__ == '__main__':
    account_name   =os.environ['STORAGE_ACCOUNT_NAME']
    account_key    =os.environ['STORAGE_ACCOUNT_KEY']
    container_name =os.environ['STORAGE_CONTAINER_NAME']
    days_until_expiry = 365*5
    id_ro = 'id'              #change the policy id name will remove the old policy
    id_rw = 'id1'
    container_permissions_ro = ContainerPermissions.READ
    container_permissions_rw = ContainerPermissions.READ + ContainerPermissions.WRITE + ContainerPermissions.DELETE + ContainerPermissions.LIST
    
    generate_SAS()
