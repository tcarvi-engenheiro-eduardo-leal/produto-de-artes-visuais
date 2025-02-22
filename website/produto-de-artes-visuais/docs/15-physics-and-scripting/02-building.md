# Bulding Blender
### Documentation
- https://wiki.blender.org/wiki/Building_Blender
- Blender uses the CMake build system.
    - https://cmake.org/
    - https://cmake.org/cmake/help/latest/guide/tutorial/index.html
### Requisitos
- cmake, svn
    - `brew install cmake svn`
        - `cmake --version`
        - `svn --version`
- Compiler Versions
    - Linux GCC:
        - Official Release Version = 11.2.1
        - Minimum Supported Version = 11.0.0
    - Linux Clang:
        - Official Release Version = 8.0
    - macOS Xcode:
        - Official Release Version = 13.2
        - Minimum Supported Version = 11.0
    - Windows Visual Studio:
        - Official Release Version = 2019 (16.11.9)
        - Minimum Supported Version = 2019 (16.9.16)

### Clone do código-fonte

```console
mkdir -p ~/src/projects.blender.org
```
  
```console
cd ~/src/projects.blender.org
```
  
```console title="clone"
git clone https://projects.blender.org/blender/blender.git
```
  
```console
cd blender
```
  
```console
make update
```
  
```console title="build Blender with the default settings"
make
```
- After the build finished, you will find Blender.app ready to run in ~/blender-git/build_darwin/bin.

### Update the earlier build

```console
cd ~/src/projects.blender.org/blender
```
  
```console
make update
````
  
```console
make
```
- If building fails, it sometimes helps to remove the ~/blender-git/build_darwin folder to get a completely clean build.

### Comand Line Interface

```console title="Build dependencies fo Blender."
make deps 
```

```console title="List all available commands."
make help 
```
```console title="Build Blender"
make
```
```console title="Update source code, add-ons and libraries to latest versions."
make update
```
```console title="Run automated tests."
make test 
```
- By default, make outputs the build and project files to to ../build_platform.
- The Blender executable will be located in ../build_platform/bin.

### Build as an Xcode project
- See (https://wiki.blender.org/wiki/Building_Blender/Mac)

- Build Options
    - https://wiki.blender.org/wiki/Building_Blender/Options

```console title="DEBUG"
make debug 
```
- Configurações do debug:
    - On Windows in Visual Studio or Xcode on macOS, a single build folder can contain both release and debug builds, and you can switch between them in the IDE.
    - For other platforms, the easiest way to set up a debug build is to build the debug target. This will create a separate build in ../build_platform_debug 
    make debug

Developer Options
```console title="Build for development"
make developer
````
  
```console title="Debug development build"
make debug developer
```

We recommend developers to configure CMake to enable address sanitizer, automated tests and options for faster builds. More details about tools for Blender development are here.

The most common options can be enabled by using the developer target, which can be combined with other targets. For example:

### CMAKE options:
- By default, the CMakeCache.txt configuration file will be in ../build_platform.
- There are a multiple ways to edit it.
    - Editing CMakeCache.txt in a text editor.

### Production build
- Blender's release builds use the option WITH_BUILDINFO
- This includes build date and time, which means each build will be slightly different from the previous.
- Typically you can just disable the WITH_BUILDINFO option, if you don't want this.