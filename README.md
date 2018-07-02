# conan-cgal

## Create package localy
Static libraries

`conan create . garlyon/testing --keep-source && conan create . garlyon/testing --keep-source --settings build_type=Debug`

Shared libraries

`conan create . garlyon/testing --keep-source --options shared=True && conan create . garlyon/testing --keep-source --options shared=True --settings build_type=Debug`

Requires [CGAL-headers Conan packge](https://github.com/garlyon/conan-cgal-headers)
