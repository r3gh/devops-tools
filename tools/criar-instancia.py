import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("\nAdicionando chave SSH...")
keypair_name = 'r3gh-sshkey'
pub_key = open(".ssh/id_rsa.pub", 'r').read().strip()
if not cloud.search_keypairs(keypair_name):
    cloud.create_keypair(keypair_name, pub_key)
print("A chave \'{}\' foi adicionada!".format(keypair_name))
