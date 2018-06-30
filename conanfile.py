from conans import ConanFile, CMake, tools
import os


class CgalConan(ConanFile):
    name = "CGAL"
    version = "4.12"
    license = "GPL/LGPL"
    url = "git@github.com:garlyon/conan-cgal.git"
    description = "Computational Geometry Algorithms Library"
    no_copy_source = True
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    scm = {
        "type": "git",
        "url": "https://github.com/CGAL/cgal.git",
        "revision": "releases/CGAL-4.12"
    }
    requires = (
        "boost/[>=1.67.0]@conan/stable",
        "CGAL-headers/4.12@garlyon/testing"
    )

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CGAL_DISABLE_GMP"] = "ON"
        cmake.definitions["BOOST_ROOT"] = self.deps_cpp_info["boost"].rootpath
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        # disk space economy: reuse CGAL headers as dependency
        tools.rmdir(os.path.join(self.package_folder, "include"))
        self.copy("*", dst="include", src="include")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

