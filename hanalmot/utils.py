import os
import jpype
import sys
from urllib.request import urlretrieve

file_path = os.path.dirname(os.path.realpath(__file__))
JAR_URL = 'https://github.com/cookieshake/hanalmot/releases/download/v0.1.1-alpha/hanalmot-0.1.1-alpha.jar'
JAR_FILE = 'hanalmot-0.1.1-alpha.jar'

def check_jar():
    def reporthook(count, block_size, total_size):
        progress_size = int(count * block_size)
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\rDownloading JAR...({}%, {:.1f} MB)\n".format(percent, progress_size / (1024 * 1024)))
        sys.stdout.flush()

    if not 'hanalmot-0.1.1-alpha.jar' in os.listdir(file_path):
        urlretrieve(JAR_URL, os.path.join(file_path, JAR_FILE), reporthook)
        sys.stdout.write('Download Complete!\n')


def init_jvm():
    jvm_path = jpype.get_default_jvm_path()
    jpype.startJVM(jvm_path, '-Djava.class.path={}'.format(os.path.join(file_path, JAR_FILE)), '-Dfile.encoding=UTF8', '-ea')


def load_hanalmot():
    check_jar()
    if not jpype.isJVMStarted():
        init_jvm()

    return jpype.JPackage('net.ingtra.hanalmot').HanalmotJava
