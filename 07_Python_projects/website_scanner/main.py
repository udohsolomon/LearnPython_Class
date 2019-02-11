from general import *
from domain_name import *
from ip_address import *
from nmap import *
# from robots import *
from whois import *  #These are bad coding practice, don't try these in actual production environments

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address  = get_ip_address(url)
    nmap        = get_nmap('-A', domain_name)
    # robots      = get_robots(url)
    whois       = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, whois)

def create_report(name, full_url, domain_name, nmap, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url', full_url)
    write_file(project_dir + '/domain_name', domain_name)
    write_file(project_dir + '/nmap', nmap)
    # write_file(project_dir + '/robots', robots)
    write_file(project_dir + '/whois', whois)

print(gather_info('Augeos', 'https://www.augeosai.com/'))
