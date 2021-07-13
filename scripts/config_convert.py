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

    serverBlock = ( '\tserver {{\n'
                    '\t\tlisten {0} ssl;\n'
                    '\t\tserver_name {1};\n'
                    '\t\tlocation {2} {{\n'
                    '\t\t\tproxy_pass {3};\n'
                    '\t\t\tproxy_set_header Host $host;\n'
                    '\t\t\tproxy_set_header X-Real-IP $remote_addr;\n'
                    '\t\t\tproxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n' 
                    '\t\t}}\n'
                    '\t}} \n'.format(port, externalUrl.hostname,
                                     externalUrl.path, backend))
    return serverBlock

def write_config(new_config):
    with open('../templates/nginx.conf.template', 'r') as f:
        nginxconf = f.readlines()
    for block in new_config:
        nginxconf.append(block)
    with open('../nginx.conf', 'w') as f:
        f.writelines(nginxconf)

def convert(config):
    newConfig = []
    for line in config:
        newConfig.append(nginxConfig(line[1], line[0]))
    #template http block has an open bracket, we need to close it
    newConfig.append('}')
    write_config(newConfig)

def main():
    old_config = read_config()
    convert(old_config)

main()



