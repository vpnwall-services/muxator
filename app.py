#/usr/bin/env python3
import argparse


class Muxator(App):


async def main(self, args)o:
    if os.geteuid() == 0:
        print('You cannot run this script as root')
        sys.exit(1)
    if os.path.exists(args.envfile):
        with open(args.envfile, 'r') as file:
            deployment_variables = yaml.safe_load(file)
    else:
        sys.exit(1)

def run_deployment_tool():
    parser = argparse.ArgumentParser(description='V6 Deployment Tool V2')
    parser.add_argument('-i', '--listen_address',
                        help='IP to serve the proxy on',
                        required=True)
    parser.add_argument('-p', '--listen_port',
                        help='Port to serve the proxy on',
                        required=True)
    parser.add_argument('-n', '--number',
                        help='Number of Tor connections to open',
                        required=True)
    args = parser.parse_args()
    app = Muxator(args)
    app.run()
