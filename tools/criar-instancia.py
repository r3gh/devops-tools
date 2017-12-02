import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("\nAdicionando chave SSH...")
keypair_name = 'r3gh-sshkey'
pub_key = open(".ssh/id_rsa.pub", 'r').read().strip()
if not cloud.search_keypairs(keypair_name):
    cloud.create_keypair(keypair_name, pub_key)
print("A chave \'{}\' foi adicionada!".format(keypair_name))

print("\nAbrindo portas...")
sec_group_name = 'r3gh-group'
ports = [22, 80, 5432, 8080]
if not cloud.search_security_groups(sec_group_name):
    cloud.create_security_group(sec_group_name, 'Grupo de acesso a network')
    for port in ports:
        cloud.create_security_group_rule(sec_group_name, port, port, 'TCP')
print("As portas [{}] foram abertas no grupo \'{}\'!".format(', '.join(str(p) for p in ports),
                                                             sec_group_name))
