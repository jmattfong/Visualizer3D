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
    if len(sys.argv) < 5  :
        print 'Usage :', sys.argv[0], '<resource_dir> <out_dir> <class_name> <package>'
        exit(1)

    res_parent_dir = sys.argv[1]
    out_dir = sys.argv[2]
    class_name = sys.argv[3]
    package = sys.argv[4]

    generated_class = generate(res_parent_dir, class_name, package)
    out_dir = join(*([out_dir] + package.split('.')))
    if not exists(out_dir):
        makedirs(out_dir)
    out = open(join(out_dir, class_name + '.java'), 'w')
    out.write(generated_class)

def generate(res_parent_dir, class_name, package) :
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
            enum_values += ENUM_VALUE.substitute(name=enum_value_name, path=join(res_dir, res_file))

        enums += ENUM_TEMPLATE.substitute(name=res_dir, contents=enum_values)

    return MAIN_TEMPLATE.substitute(class_name=class_name, script_name=sys.argv[0], enums=enums, package=package)

MAIN_TEMPLATE = Template("""package ${package};
/**
 * ${class_name}.java
 *
 * THIS FILE IS GENERATED. DO NOT MODIFY.
 * See ${script_name}
 */

public final class ${class_name} {
    ${enums}
    private ${class_name}() {}
}
""")

ENUM_TEMPLATE = Template("""
    public enum ${name} implements Resource {${contents}
        ;

        public final String path;
        private ${name}(String path) {
            this.path = path;
        }

        @Override
        public String getPath() {
            return this.path;
        }
    }
""")

ENUM_VALUE = Template("""
        ${name}("${path}"),""")

if __name__ == "__main__" : main()
