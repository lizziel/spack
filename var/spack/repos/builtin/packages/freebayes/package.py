# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Freebayes(MesonPackage):
    """Bayesian haplotype-based genetic polymorphism discovery and
    genotyping."""

    homepage = "https://github.com/ekg/freebayes"
    url = "https://github.com/freebayes/freebayes/releases/download/v1.3.5/freebayes-1.3.5-src.tar.gz"
    git = "https://github.com/ekg/freebayes.git"

    version(
        "1.3.5",
        sha256="7e2635690e916ed85cec36b3263e6e5357413a4f2bf3035362d9749335e8a696",
    )
    version(
        "1.1.0",
        commit="39e5e4bcb801556141f2da36aba1df5c5c60701f",
        submodules=True,
        deprecated=True,
    )

    depends_on("cmake", type="build")
    depends_on("zlib")

    # Deps for @1.3.5 and beyond
    depends_on("ninja", type="build", when="@1.3.5:")
    depends_on("htslib", when="@1.3.5:")
    depends_on("zlib", when="@1.3.5:")
    depends_on("xz", when="@1.3.5:")
    depends_on("parallel", when="@1.3.5:")
    depends_on("vcftools", when="@1.3.5:")
    depends_on("bc", when="@1.3.5:")
    depends_on("samtools", when="@1.3.5:")

    parallel = False

    @when("@:1.1.0")
    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        b = prefix.bin
        makefile.filter(
            "cp bin/freebayes bin/bamleftalign /usr/local/bin/",
            "cp bin/freebayes bin/bamleftalign {0}".format(b),
        )

    @when("@:1.1.0")
    @run_before("install")
    def make_prefix_dot_bin(self):
        mkdir(prefix.bin)

    @when("@:1.1.0")
    def meson(self, spec, prefix):
        pass

    @when("@:1.1.0")
    def build(self, spec, prefix):
        make()

    @when("@:1.1.0")
    def install(self, spec, prefix):
        make("install")
