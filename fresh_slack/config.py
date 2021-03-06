import configparser
import os

# Defaults expected to be env vars, so use those globally
cfg = os.environ

# Reads values from config file into env vars, which ensures default behavior
# but allows them to be set in the file
def read_cfg_file(cfg_file: str = 'fresh-slack.cfg') -> None:
    fscfg = configparser.ConfigParser()
    fscfg.read(cfg_file)
    fscfg = dict(fscfg['fresh-slack'])
    for key, value in fscfg.items():
        cfg[f'FRESH_{key.upper()}'] = value
# end read_cfg_file

read_cfg_file()


slack_url = f"https://{cfg.get('FRESH_SLACK_NAME')}.slack.com/api/"
slack_token = cfg.get('FRESH_SLACK_TOKEN')
