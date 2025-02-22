# Source Code

- Install xcode tools
```terminal
xcode-select --install
```  
  
- Install other tools
```terminal
brew install cmake svn
``` 
  
- Clone and update
```terminal
mkdir ~/src/projects.blender.org/blender-git
```  
```terminal
cd ~/src/projects.blender.org/blender-git
```  
```terminal
git clone https://projects.blender.org/blender/blender.git
``` 
```terminal
cd ~/src/projects.blender.org/blender-git/blender
``` 
```terminal
make update
```
  
- Building
```terminal
make
``` 
  
- After the build finished, you will find Blender.app ready to run in ~/src/projects.blender.org/blender-git/build_darwin/bin.

- [File Structure](https://wiki.blender.org/wiki/Source/File_Structure)
