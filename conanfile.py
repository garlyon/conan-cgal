from conans import ConanFile, CMake, tools


class CgalConan(ConanFile):
    name = "cgal"
    version = "4.12.0"
    license = "GPL/LGPL"
    url = "git@github.com:garlyon/conan-cgal.git"
    description = "Computational Geometry Algorithms Library"
    no_copy_source = True
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "with_gmp": [True, False]}
    default_options = "shared=False", "with_gmp=False"
    scm = {
        "type": "git",
        "url": "https://github.com/cgal/cgal.git",
        "revision": "releases/CGAL-4.12"
    }

    def requirements(self):
        self.requires("boost/[^1.67]@conan/stable")
        if self.options.with_gmp:
            self.requires("gmp/[>=5.0]@grif/dev")
            self.requires("mpfr/[>=3.0]@grif/dev")

    def build(self):
        with tools.environment_append(self.cmake_env_vars):
            cmake = CMake(self)
            cmake.definitions["BOOST_ROOT"] = self.deps_cpp_info["boost"].rootpath
            cmake.definitions["CGAL_DISABLE_GMP"] = "OFF" if self.options.with_gmp else "ON"
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "True"
            cmake.configure()
            cmake.build()
            cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

    @property
    def cmake_env_vars(self):
        env = {}
        if self.options.with_gmp:
            env["GMP_DIR"] = self.deps_cpp_info["gmp"].rootpath
            env["MPFR_DIR"] = self.deps_cpp_info["mpfr"].rootpath
        return env


