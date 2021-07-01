from urllib.parse import urlparse
import csv

def read_config():
    with open('wap.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        #skip the titles in the csv
        next(reader, None)
        wapConfig = list(reader)
    return wapConfig

def nginxConfig(external, backend):
    externalUrl = urlparse(external)
    if not externalUrl.port:
        port = 443
    else:
        port = externalUrl.port

    serverBlock = """    server {{
                             listen {0} ssl;
                             server_name {1};
                             location {2} {{
                                 proxy_pass {3};
                                 proxy_set_header Host $host;
                                 proxy_set_header X-Real-IP $remote_addr;
                                 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
                                 }}
                            }} \n""".format(port, externalUrl.hostname,
                                            externalUrl.path, backend)
    return serverBlock

def write_config(new_config):
    with open('nginx.conf.template', 'r') as f:
        nginxconf = f.readlines()
    for block in new_config:
        nginxconf.append(block)
    with open('nginx.conf', 'w') as f:
        f.writelines(nginxconf)

def convert(config):
    newConfig = []
    for line in config:
        newConfig.append(nginxConfig(line[1], line[0]))
    #template http block has an open bracket, we need to close it
    newConfig.append('    }')
    write_config(newConfig)

def main():
    old_config = read_config()
    convert(old_config)

main()



