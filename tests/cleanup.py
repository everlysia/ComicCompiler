import glob
import shutil

if __name__ == '__main__':
    for directory in glob.glob("**/*-test/", recursive=True):
        print("deleting: " + directory)
        shutil.rmtree(directory)