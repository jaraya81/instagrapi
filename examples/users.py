from instagrapi import Client
import json

IG_CREDENTIAL_PATH = 'credential.json'
IG_USERNAME = ''
IG_PASSWORD = ''

USERNAME = 'instagram'


def write_file(data, path_file, default=None):
    """
    Write a file
    :param default:
    :param data:
    :param path_file:
    :return:
    """
    from pathlib import Path

    path_user = Path(path_file)
    path_user.parent.mkdir(exist_ok=True)

    with open(path_file, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=True, default=default)


def read_file(path_file, object_hook=None):
    """
    Read a file
    :param object_hook:
    :param path_file:
    :return:
    """
    with open(path_file, 'r', encoding='utf8') as json_file:
        return json.load(json_file, object_hook=object_hook)


def get_logger(name, **kwargs):
    import logging
    logging.basicConfig(**kwargs)
    logger = logging.getLogger(name)
    logger.debug(f"start logging '{name}'")
    return logger


if __name__ == '__main__':
    import os

    log = get_logger("users", **{
        "level": "DEBUG",
        "format": "%(asctime)s %(levelname)s %(name)s: %(message)s"
    })
    cl = None
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl = Client(read_file(IG_CREDENTIAL_PATH))
    else:
        cl = Client()
        cl.login(IG_USERNAME, IG_PASSWORD)
        write_file(cl.get_settings(), IG_CREDENTIAL_PATH)

    following = cl.user_following(cl.user_id_from_username(USERNAME), amount=500, max_id=121)
    log.info(len(following))
    followers = cl.user_followers(cl.user_id_from_username(USERNAME), amount=500, max_id=121)
    log.info(len(followers))
