import os

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY


class CfiIgnore:
    """ CfiIgnore reads cfiignore file in dir_path directory. Ignore submission if id present in cfiignore"""

    def __init__(self, dir_path):
        self.ignore_list = []
        self.dir_path = dir_path
        self.fetch_ignore_list()

    def ignore(self, problem_id):
        """Returns True if problem_id is already present in cfiignore

        :param problem_id: problem-id to be checked for in cfiignore
        :return: True or False
        """

        return problem_id in self.ignore_list

    def add(self, problem_id):
        """Adds to ignore list"""

        self.ignore_list.append(problem_id)

    def fetch_ignore_list(self):
        """Reads ignore list from cfiignore file in dir_path directory"""

        try:
            file_path = self.dir_path + '\cfiignore'
            with open(file_path, 'r') as ignore_file:
                content = str(ignore_file.read(1000000))
                self.ignore_list = content.split(';')
                print self.ignore_list
        except (OSError, IOError) as ex:
            print ex.message

    def write_ignore_list(self):
        """Writes ignore list to cfiignore file in dir_path directory"""

        try:
            file_path = self.dir_path + '\cfiignore'
            file_handle = os.open(file_path, WRITE_FLAGS)
            with os.fdopen(file_handle, 'w') as file_obj:
                for identifier in self.ignore_list:
                    file_obj.write(identifier)
        except (OSError, IOError) as ex:
            print ex.message
