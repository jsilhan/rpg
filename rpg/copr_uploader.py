from rpg.command import Command
from os.path import expanduser

class CoprUploader:
    
    def setup__copr_config(self, username, login, token):
        config_path = expanduser('~') + '/.config/copr'
        begin = '[copr-cli] \n'
        username = 'username = ' + username + '\n'
        login = 'login = ' + login + '\n'
        token = 'token = ' + token + '\n'
        copr_url = 'copr_url = http://copr-fe-dev.cloud.fedoraproject.org'
        with open(config_path, 'w') as config_file:
            config_file.write(begin + username + login + token + copr_url)
                
    
    def create_copr(self, name, chroots, description='', instructions=''):
        command = 'copr-cli create'
        parameters = ''
        for chroot in chroots:
            parameters = parameters + ' --chroot ' + str(chroot)
        if description:
            parameters = parameters + ' --description \'' + description + '\''
        if instructions:
            parameters = parameters + ' --instructions \'' + instructions + '\''
        parameters = parameters + ' ' + name
        Command(command + parameters).execute()
        
    def build_copr(self, name, srpm_url):
        command = 'copr-cli build '
        parameters = name + ' ' + srpm_url
        Command(command + parameters).execute()
         
