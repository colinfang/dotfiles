# GNU Compiler Collection (GCC)

- `gcc`: GNC C Compiler
    - [Example] `gcc-12`
- `g++`: GNU C++ Compiler
    - `--version`
    - Depend on `gcc`


# Version

| Ubuntu | gcc  | gcc universe | clang universe |
| ------ | ---- | ------------ | -------------- |
| 20.04  | 9.3  | 10           | 12             |
| 22.04  | 11.2 | 11           | 14             |
| 24.04  | 13.2 | 14           | 18             |

- Check default version
    - <https://packages.ubuntu.com/search?suite=noble&keywords=gcc>
    - Search e.g. `gcc-12` for a specific version


# C++ Standards Support

- GCC
    - <https://gcc.gnu.org/projects/cxx-status.html>
- Default standard used for each compiler version
    - <https://gist.github.com/ax3l/53db9fa8a4f4c21ecc5c4100c0d93c94>
- `-std=c++23`
    - Added in GCC 13
    - Added in Clang 17
    - Use `-std=c++2b` for old versions
- `-std=c++20`
    - Added in GCC 10
    - Use `-std=c++2a` for old versions
- `-std=c++17`
- `-std=c++14`
- `-std=c++11`
- GNU extension
    - `-std=gnu++11` instead of `-std=c++11`
    - <https://stackoverflow.com/questions/10613126/what-are-the-differences-between-std-c11-and-std-gnu11>


# Install The Latest g++

- [Convention] Universe is better than `ppa:ubuntu-toolchain-r/test`
    - Prior to Ubuntu 22.04, built-in `security` channel already contains new version of `g++` & `clang` hence `universe` is not necessary.
    - `add-apt-repository universe`
- <https://wiki.ubuntu.com/ToolChain>
    - `ppa:ubuntu-toolchain-r/ppa` hosts updates from release branches (e.g. Ubuntu 14.04 `gcc-4.8.2` -> `gcc-4.8.3`).
    - `ppa:ubuntu-toolchain-r/test` hosts newer upstream versions.


```bash
apt install g++-12 gfortran-12

# Make sure there is no alternatives set.
update-alternatives --display gcc
update-alternatives --display g++
update-alternatives --display gfortran

update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 120 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-12

update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-10 \
    --slave /usr/bin/gfortran gfortran /usr/bin/gfortran-10
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-9 \
    --slave /usr/bin/gfortran gfortran /usr/bin/gfortran-9
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-7 \
    --slave /usr/bin/gfortran gfortran /usr/bin/gfortran-7
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 50 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-5 \
    --slave /usr/bin/gfortran gfortran /usr/bin/gfortran-5

# Check
update-alternatives --display gcc
# Switch version
update-alternatives --config gcc
```


# Install The Latest clang & clangd

- <http://apt.llvm.org/>


```bash
# Only needed if the latest version is not available in ubuntu official channel
# curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add -
# This channel provides the latest version only
# For a certain version, use e.g. `llvm-toolchain-jammy-16`
# apt-add-repository "deb http://apt.llvm.org/jammy/ llvm-toolchain-jammy main"
# apt update
apt install clang-21 clangd-21

update-alternatives --install /usr/bin/clang clang /usr/bin/clang-21 2100 \
    --slave /usr/bin/clang++ clang++ /usr/bin/clang++-21 \
    --slave /usr/bin/clangd clangd /usr/bin/clangd-21

update-alternatives --install /usr/bin/clang clang /usr/bin/clang-16 1600 \
    --slave /usr/bin/clang++ clang++ /usr/bin/clang++-16 \
    --slave /usr/bin/clangd clangd /usr/bin/clangd-16

update-alternatives --install /usr/bin/clang clang /usr/bin/clang-15 1500 \
    --slave /usr/bin/clang++ clang++ /usr/bin/clang++-15 \
    --slave /usr/bin/clangd clangd /usr/bin/clangd-15
```


# Include What You Use

- <https://include-what-you-use.org/downloads/>
- Require `libclang-dev` (`libclang-10-dev`)
- `-DCMAKE_CXX_INCLUDE_WHAT_YOU_USE="/usr/bin/iwyu;-Xiwyu;any;-Xiwyu;iwyu;-Xiwyu;args"`

```dockerfile
RUN cd /opt && git clone --depth 1 -b clang_14 https://github.com/include-what-you-use/include-what-you-use.git && \
    cd /opt/include-what-you-use && \
    cmake -B build . && \
    cmake --build build --parallel 4 && \
    ln -s "$PWD/build/bin/include-what-you-use" /usr/bin/iwyu
```


# Sanitizer

- TODO
- Detect memory & address issues
- Need to recompile, much faster than Valgrind
- <https://github.com/google/sanitizers>
- <https://developers.redhat.com/blog/2021/05/05/memory-error-checking-in-c-and-c-comparing-sanitizers-and-valgrind>


# Working Environment

- [VS Code](</VS Code/C++.md>)
- [Lint](Lint.md)
