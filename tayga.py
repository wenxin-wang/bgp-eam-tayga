import os


class Tayga:
    @staticmethod
    def gen_conf(conf_path, pream="", map_rules={}):
        with open(Tayga.exapath(conf_path), 'w') as fd:
            fd.write(pream)
            fd.writelines(["map %s %s\n" % (k, v) for k, v in map_rules.items()])

    @staticmethod
    def reload(pid_path):
        os.system("kill -USR2 $(cat %s)" % Tayga.exapath(pid_path))

    @staticmethod
    def exapath(path):
        return os.path.join(os.environ.get('PWD',''), path) if path[0] != '/' else path
