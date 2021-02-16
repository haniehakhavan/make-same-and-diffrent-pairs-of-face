import os
from shutil import copyfile
import random
import argparse


def main():
    os.mkdir(os.path.join(args.outputPath, 'match'))
    os.mkdir(os.path.join(args.outputPath, 'mismatch'))

    others_path = os.path.join(args.datasetPath, 'others')
    index_path = os.path.join(args.datasetPath, 'index')
    for index in os.listdir(index_path):
        index_name = index.split('.')
        label = index_name[0]
        for other in os.listdir(others_path):
            if other.startswith(label + '_'):
                other_name = other.split('.')
                folder_name = other_name[0]
                if not os.path.exists(os.path.join(args.outputPath, 'match', folder_name)):
                    os.mkdir(os.path.join(args.outputPath, 'match', folder_name))
                copyfile(os.path.join(args.datasetPath, 'index', index),
                         os.path.join(args.outputPath, 'match', folder_name, index))
                copyfile(os.path.join(args.datasetPath, 'others', other),
                         os.path.join(args.outputPath, 'match', folder_name, other))
                a = random.choices(os.listdir(index_path), k=1)
                a_label = a[0].split('.')
                a2 = a_label[0]
                b = random.choices(os.listdir(others_path), k=1)
                b_label = b[0].split('.')
                b2 = b_label[0]
                while b2.startswith(a2 + '_'):
                    b = random.choices(os.listdir(others_path), k=1)
                    b_label = b[0].split('.')
                    b2 = b_label[0]
                mismatch_folder_name = a2 + '_' + b2
                while os.path.exists(os.path.join(args.outputPath, 'mismatch', mismatch_folder_name)):
                    b = random.choices(os.listdir(others_path), k=1)
                    b_label = b[0].split('.')
                    b2 = b_label[0]
                    mismatch_folder_name = a2 + '_' + b2
                if not os.path.exists(os.path.join(args.outputPath, 'mismatch', mismatch_folder_name)):
                    os.mkdir(os.path.join(args.outputPath, 'mismatch', mismatch_folder_name))
                copyfile(os.path.join(args.datasetPath, 'index', a2 + '.jpg'),
                         os.path.join(args.outputPath, 'mismatch', mismatch_folder_name, a2 + '.jpg'))
                copyfile(os.path.join(args.datasetPath, 'others', b2 + '.jpg'),
                         os.path.join(args.outputPath, 'mismatch', mismatch_folder_name, b2 + '.jpg'))


def parse_arguments():
    parser = argparse.ArgumentParser(description='paths')
    parser.add_argument('-d', '--datasetPath', help='datasetPath')
    parser.add_argument('-o', '--outputPath', help='outputPath')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main()
