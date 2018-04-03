from conans import ConanFile, tools, AutoToolsBuildEnvironment


from fobis.fobis import run_fobis

import os
import pdb

class FobisExampleConan(ConanFile):
    name = "FoBiS Example"
    version = "2.2.8"
    license = "GPL v3"
    url = "https://github.com/szaghi/FoBiS"
    description = "Example of FoBiS.py, Fortran projects Building System for poor people"

    def source(self):
        self.run("git clone https://github.com/szaghi/FoBiS.git")
        #self.run("cd FoBiS/examples/library")

    def build(self):
        self.compilt:
#        with tools.chdir('FoBiS/examples/library'):
#            run_fobis(["build","-m", "Makefile", "-f", "fobos.shared" ])
#            self.run('FoBiS.py build -f fobis -m makefile1')
        #
#        os.chdir('FoBiS/examples/library')
#        path='FoBiS/examples/library'
#        #print('Change directory to %s:' %(os.getcwd()) )
#        run_fobis(["build", "-f %s/fobis.shared" %(path) ])
#        self.run('FoBiS.py build -f fobis.shared')
        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        pass
    def package_info(self):
        self.cpp_info.libs = ["library"]
