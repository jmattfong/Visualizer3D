#!/usr/bin/env python

# code_gen.py
#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
# Copyright (C) 2016, Matthew Fong

import sys
from os import listdir, makedirs
from os.path import isfile, isdir, join, exists
from string import Template

def main() :
    if len(sys.argv) < 3  :
        print 'Usage :', sys.argv[0], '<resource_dir> <out_dir>'
        exit(1)

    res_parent_dir = sys.argv[1]
    out_dir = sys.argv[2]
    generated_class = generate(res_parent_dir, out_dir)
    if not exists(out_dir):
        makedirs(out_dir)
    out = open(join(out_dir, 'R.java'), 'w')
    out.write(generated_class)

def generate(res_parent_dir, out_dir) :
    enums = ''
    for res_dir in listdir(res_parent_dir) :
        res_dir_path = join(res_parent_dir, res_dir)
        if not isdir(res_dir_path) :
            print 'Resource directory is structured incorrectly -', res_dir_path, 'is not a directory.'
            print 'All resources must have a parent directory.'
            exit(2)

        enum_values = ''
        for res_file in listdir(res_dir_path) :
            res_file_path = join(res_dir_path, res_file)
            if not isfile(res_file_path) :
                print 'Resource directory is structured incorrectly -', res_file_path, 'is a directory.'
                print 'All resources must be plain files.'
                exit(3)

            enum_value_name = res_file.split('.')[0]
            enum_values += ENUM_VALUE.substitute(name=enum_value_name)

        enums += ENUM_TEMPLATE.substitute(name=res_dir, contents=enum_values)

    return MAIN_TEMPLATE.substitute(file_name='R.java', script_name=sys.argv[0], contents=enums)

MAIN_TEMPLATE = Template("""/**
 * ${file_name}
 *
 * THIS FILE IS GENERATED. DO NOT MODIFY.
 * See ${script_name}
 */

public class R {
    ${contents}
}
""")

ENUM_TEMPLATE = Template("""
    public enum ${name} {${contents}
    }
""")

ENUM_VALUE = Template("""
        ${name},""")

if __name__ == "__main__" : main()
