from Core.Networking.Server import Server
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

def main():

    print(r"""
 _   _                  ______                    _ 
| \ | |                 | ___ \                  | |
|  \| | _____   ____ _  | |_/ /_ __ __ ___      _| |
| . ` |/ _ \ \ / / _` | | ___ \ '__/ _` \ \ /\ / / |
| |\  | (_) \ V / (_| | | |_/ / | | (_| |\ V  V /| |
\_| \_/\___/ \_/ \__,_| \____/|_|  \__,_| \_/\_/ |_| 
                                                             
    """)

    Server("0.0.0.0", 9339).start()


if __name__ == '__main__':
    main()
