from django.core.management.base import BaseCommand
import os

 class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new django project name. 1 Time use only.')

        #parser.add_argument('-p', '--perfix'

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        PROJECT_DIR = os.getcwd()
        #Create a dictionary, loop through the files. Any folder missing gets the rename.
        LIST_DIR = ['.env', '.git', '.gitignore', 'core', 'db.sqlite3', 'LICENSE', 'manage.py', 'README.md', 'requirements.txt', 'static_in_env', 'templates']

        if bool(set(os.listdir(PROJECT_DIR)).difference(LIST_DIR)):
            folder_to_rename = set(os.listdir(PROJECT_DIR)).difference(LIST_DIR).pop()
            folder_to_rename = '/' + folder_to_rename

            baseFile = '/settings/base.py'
            wsgiFile = '/wsgi.py'
            x = folder_to_rename +''.join(baseFile)
            y = folder_to_rename +''.join(wsgiFile)

            files_to_rename = [x, y, 'manage.py']
      
        #Error: No such file or directory '/demo/settings/base.py
        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

                filedata = filedata.replace(folder_to_rename, new_project_name)

                with open(f, 'w') as file:
                    file.write(filedata)

        os.rename(folder_to_rename, new_project_name)  

        self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % new_project_name))