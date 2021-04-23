# Criptografado por @AZZ4DEFALT bb!
# Criptografado por @AZZ4DEFALT bb!
 
 # Criptografado por @AZZ4DEFALT bb!
 
 # Criptografado por @AZZ4DEFALT bb!
 
 # Criptografado por @AZZ4DEFALT bb!
 
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 # Criptografado por @AZZ4DEFALT bb!
 
 

import base64, codecs
magic = 'IyAtLSBjb2Rpbmc6IHV0Zi04IC0tCmZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4KZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAKCnByaW50ICgiIiIKClwwMzNbMTs5Mm0g4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI4pWXICDilojilojilZcgICAgXDAzM1sxOzkxbeKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVlyDilojilojilojilojilojilojilojilojilZcKXDAzM1sxOzkybeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVmuKVkOKVkOKWiOKWiOKWiOKVlOKVmuKVkOKVkOKWiOKWiOKWiOKVlOKWiOKWiOKVkSAg4paI4paI4pWRIC'
love = 'NtVSjjZmAoZGf5ZJ3vybwvybwvyMGvyMQvyMQvybwvybwvybwvybwvyMGvyMQvyMQvyMQvyMQvybwvybwvyMGvyMQvyMQvyMQvyMQvybwvybwvyMGvyMQvyMQvybwvybwvybwvybwvyMRt4cJn4cJD4cJD4cnV4cnV4cJH4cJD4cJD4cJqPyjjZmAoZGf5Zz3vybwvybwvybwvybwvybwvybwvybwvyMRt4cnV4cnV4cnV4cJH4cJqVPQvybwvybwvybwvyMGvyM3vybwvybwvybwvybwvybwvybwvybwvyMRtVPNtKQNmZ1fkBmxkorXJvBXJvBXIxFNt4cnV4cnV4cnV4cnV4cnV4cnV4cnV4cJKVBXJvBXJvBXJvBXJvBXJvBXIylQvybwvybwvybwvybwvybwvybwvybwvybwvybwvyMRtVPNt4cnV4cnV4cJEVPNtPyjjZmAoZGf5Zz3vybwvybwvyMGvyMQvyMQvybwvybwvyMUvybwvybwvybwvyMGvyM0tVBXJvBXJvBXJvBXIyBXIaFQvyMevyMQvyMQvyMQv'
god = 'lZDilojilojilZEgICAgXDAzM1sxOzkxbeKWiOKWiOKVkSAg4paI4paI4paI4paI4pWU4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKVnSDilojilojilZTilZDilZDilojilojilojilojilZEgICAg4paI4paI4pWRICAgClwwMzNbMTs5Mm3ilojilojilZEgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICDilojilojilZEgICAgXDAzM1sxOzkxbeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkSAgICDilojilojilZEgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkSAgIApcMDMzWzE7OTJt4pWa4pWQ4pWdICDilZrilZDilZrilZDilZDilZDilZDilZDilZDilZrilZDilZDilZDilZDilZDilZDilZ0gICAg4pWa4pWQ4pWdICAgIF'
destiny = 'jjZmAoZGf5ZJ3vyMevyMQvyMQvyMQvyMQvyMQvyM3vyMevyMQvyMQvyMQvyMQvyMQvyMQvyMevyMQvyM0tVPNt4cJn4cJD4cJqVPQvyMevyMQvyMevyMQvyMQvyMQvyMQvyMQvyMQvyMevyMQvyM0tVPNXKQNmZ1fkBmZloIOipaDtp2Auoz5yptbXVvVvXDbXLJk2olN9VTyhpUI0XPqpZQZmJmR7ZmWgETyanKEyVSjjZmAoZGf5ZJ1cpSjjZmAoZQfjoFOiqFOpZQZmJmR7BGSgqKWfKQNmZ1fjBmOgVTEiVTSfqz86VSjjZmAoZGfmZJ0aXDc1pzjtCFNbW2u0qUOmBv8iLKOcYzuuL2gypaEupzqyqP5wo20ioz1upP8/pG0aVPftLJk2olxXPaWyp3OioaAyVQ0tqKWfo3Oyovu1pzjcPzu0oJjtCFOlMKAjo25mMF5lMJSxXPxXp291pPN9VRWyLKI0nJM1oSAiqKNbnUEgoPjtW2u0oJjhpTSlp2IlWlxXPaOlnJ50VPtaKQNmZ1fkBmxloFpfVUAiqKNcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
