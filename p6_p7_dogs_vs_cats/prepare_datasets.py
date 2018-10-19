#!/usr/bin/env python
import os

# unzip files, make directries
if os.path.exists('all.zip') and not (os.path.isdir('data')):
    os.system('unzip -o all.zip; unzip -o train.zip; unzip -o test.zip')
    os.system('mkdir data; mv train test data')

# make symbol links
if not os.path.exists('data/train2'):
    os.system('mkdir -p data/train2/dog data/train2/cat')
    for filename in os.listdir('data/train'):
        if 'dog' in filename:
            os.symlink('../../train/%s' % filename, 'data/train2/dog/%s' % filename)
        else:
            os.symlink('../../train/%s' % filename, 'data/train2/cat/%s' % filename)

if not os.path.exists('data/test2'):
    os.mkdir('data/test2')
    os.symlink('../test/', 'data/test2/test')
