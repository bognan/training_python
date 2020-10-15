import os



def mk_my_dir(dir_count):
    for dir_n in range(1, (int(dir_count) + 1)):
        os.mkdir('dir_' + str(dir_n))

