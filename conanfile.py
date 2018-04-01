from conans import ConanFile, CMake, tools
from fobis.fobis import run_fobis

import os

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
        # 
        os.chdir('FoBiS/examples/library')
        print('Change directory to %s:' %(os.cwd()) )
        #run_fobis(["build", "-f", "fobis.shared"])
        
        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        pass
    def package_info(self):
        self.cpp_info.libs = ["library"]
