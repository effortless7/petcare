# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /userdata/voice/sherpa-onnx-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /userdata/voice/sherpa-onnx-master/build

# Include any dependencies generated for this target.
include sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/compiler_depend.make

# Include the progress variables for this target.
include sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/progress.make

# Include the compile flags for this target's objects.
include sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/flags.make

sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o: sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/flags.make
sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o: ../sherpa-onnx/csrc/sherpa-onnx-offline-language-identification.cc
sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o: sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/userdata/voice/sherpa-onnx-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o"
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o -MF CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o.d -o CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o -c /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/sherpa-onnx-offline-language-identification.cc

sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.i"
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/sherpa-onnx-offline-language-identification.cc > CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.i

sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.s"
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/sherpa-onnx-offline-language-identification.cc -o CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.s

# Object files for target sherpa-onnx-offline-language-identification
sherpa__onnx__offline__language__identification_OBJECTS = \
"CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o"

# External object files for target sherpa-onnx-offline-language-identification
sherpa__onnx__offline__language__identification_EXTERNAL_OBJECTS =

bin/sherpa-onnx-offline-language-identification: sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/sherpa-onnx-offline-language-identification.cc.o
bin/sherpa-onnx-offline-language-identification: sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/build.make
bin/sherpa-onnx-offline-language-identification: lib/libsherpa-onnx-core.a
bin/sherpa-onnx-offline-language-identification: lib/libkaldi-native-fbank-core.a
bin/sherpa-onnx-offline-language-identification: lib/libkissfft-float.a
bin/sherpa-onnx-offline-language-identification: lib/libkaldi-decoder-core.a
bin/sherpa-onnx-offline-language-identification: lib/libsherpa-onnx-kaldifst-core.a
bin/sherpa-onnx-offline-language-identification: lib/libssentencepiece_core.a
bin/sherpa-onnx-offline-language-identification: _deps/onnxruntime-src/lib/libonnxruntime.a
bin/sherpa-onnx-offline-language-identification: lib/libsherpa-onnx-fstfar.a
bin/sherpa-onnx-offline-language-identification: lib/libsherpa-onnx-fst.a
bin/sherpa-onnx-offline-language-identification: lib/libpiper_phonemize.a
bin/sherpa-onnx-offline-language-identification: lib/libespeak-ng.a
bin/sherpa-onnx-offline-language-identification: lib/libucd.a
bin/sherpa-onnx-offline-language-identification: sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/userdata/voice/sherpa-onnx-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/sherpa-onnx-offline-language-identification"
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sherpa-onnx-offline-language-identification.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/build: bin/sherpa-onnx-offline-language-identification
.PHONY : sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/build

sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/clean:
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && $(CMAKE_COMMAND) -P CMakeFiles/sherpa-onnx-offline-language-identification.dir/cmake_clean.cmake
.PHONY : sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/clean

sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/depend:
	cd /userdata/voice/sherpa-onnx-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /userdata/voice/sherpa-onnx-master /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc /userdata/voice/sherpa-onnx-master/build /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sherpa-onnx/csrc/CMakeFiles/sherpa-onnx-offline-language-identification.dir/depend

