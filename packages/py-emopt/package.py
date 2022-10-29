# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-emopt
#
# You can edit this file again by typing:
#
#     spack edit py-emopt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os


class PyEmopt(PythonPackage):
    """A suite of tools for optimizing the shape and topology of electromagnetic structures."""

    # Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/anstmichaels/emopt/archive/refs/tags/v2019.5.6.tar.gz"
    git = "https://github.com/anstmichaels/emopt.git"
    # pypi = "emopt/emopt-0.2.3.1.tar.gz"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    # Versions
    version('develop', branch='develop')
    version('master',  branch='master')
    version("2019.5.6", sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    # version("0.2.3.1", sha256="ad389b8f9e786146232a4b86382286529cc979f5fc2f98cf2f740473d774a3da")

    # Relax PETSc and SLEPc constraints
    #patch('relaxslepc.patch')    #, when='@1.9:')
    # Fix install wheel error
    patch('fixegginstall.patch')
    # Fix hardcoded paths in Makefile (should switch to CMake!)
    patch('fixsrcmakefile.patch')

    # Variants
    variant('h5py', default=True, description='For saving and loading simulation data')
    variant('matplotlib', default=True, description='For plotting optimization results')
    variant('shapely', default=True, description='For handling more complicated geometric operations')
    depends_on("py-h5py", when="+h5py")
    depends_on("py-matplotlib", when="+matplotlib")
    depends_on("py-shapely", when="+shapely")

    # Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.7:", type=("build", "run"))
    depends_on("python@:2.7", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))
    depends_on("eigen", type=("build", "run"))
    depends_on("boost@1.73.0", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-petsc4py@3.12.0", type=("build", "run"))
    depends_on("py-slepc4py@3.12.0", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set('EIGEN_ROOT', self.spec['eigen'].prefix)
        env.set('BOOST_ROOT', self.spec['boost'].prefix)
