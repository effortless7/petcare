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

# Utility rule file for clang-tidy-check.

# Include any custom commands dependencies for this target.
include sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/compiler_depend.make

# Include the progress variables for this target.
include sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/progress.make

sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/base64-decode.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/bbpe.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/cat.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/circular-buffer.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/context-graph.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/endpoint.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/features.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/file-utils.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/fst-utils.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/homophone-replacer.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/hypothesis.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/jieba.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/keyword-spotter-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/keyword-spotter.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ctc-fst-decoder-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ctc-fst-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ctc-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-dolphin-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-dolphin-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-fire-red-asr-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-fire-red-asr-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-fire-red-asr-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-lm-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-lm.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-moonshine-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-moonshine-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-moonshine-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-nemo-enc-dec-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-nemo-enc-dec-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-paraformer-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-paraformer-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-paraformer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-recognizer-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-recognizer.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-rnn-lm.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-sense-voice-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-sense-voice-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-spleeter-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-spleeter-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-uvr-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation-uvr-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-source-separation.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-stream.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tdnn-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tdnn-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-telespeech-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-greedy-search-nemo-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-modified-beam-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-transducer-nemo-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-wenet-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-wenet-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-whisper-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-whisper-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-whisper-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-zipformer-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-zipformer-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-conformer-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-ctc-fst-decoder-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-ctc-fst-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-ctc-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-ebranchformer-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-lm-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-lm.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-lstm-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-nemo-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-nemo-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-paraformer-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-paraformer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-recognizer-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-recognizer.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-rnn-lm.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-stream.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-greedy-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-greedy-search-nemo-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-modified-beam-search-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-transducer-nemo-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-wenet-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-wenet-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-zipformer-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-zipformer2-ctc-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-zipformer2-ctc-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-zipformer2-transducer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/onnx-utils.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/packed-sequence.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/pad-sequence.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/parse-options.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/provider-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/provider.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/resample.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/session.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/silero-vad-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/silero-vad-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/slice.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/spoken-language-identification-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/spoken-language-identification.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/stack.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/symbol-table.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/text-utils.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/transducer-keyword-decoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/transpose.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/unbind.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/utils.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/vad-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/vad-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/voice-activity-detector.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/wave-reader.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/wave-writer.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/speaker-embedding-extractor-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/speaker-embedding-extractor-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/speaker-embedding-extractor-nemo-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/speaker-embedding-extractor.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/speaker-embedding-manager.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/audio-tagging-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/audio-tagging-label-file.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/audio-tagging-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/audio-tagging.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ced-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-zipformer-audio-tagging-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-zipformer-audio-tagging-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-ct-transformer-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-punctuation-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-punctuation-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-punctuation.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-cnn-bilstm-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-punctuation-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-punctuation-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/online-punctuation.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/hifigan-vocoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/jieba-lexicon.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/kokoro-multi-lang-lexicon.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/lexicon.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/melo-tts-lexicon.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-character-frontend.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-frontend.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-kokoro-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-kokoro-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-matcha-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-matcha-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-vits-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts-vits-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-tts.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/piper-phonemize-lexicon.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/vocoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/vocos-vocoder.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speech-denoiser-gtcrn-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speech-denoiser-gtcrn-model.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speech-denoiser-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speech-denoiser-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speech-denoiser.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/fast-clustering-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/fast-clustering.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-diarization-impl.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-diarization-result.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-diarization.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-segmentation-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-segmentation-pyannote-model-config.cc
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check: ../sherpa-onnx/csrc/offline-speaker-segmentation-pyannote-model.cc
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && clang-tidy -p /userdata/voice/sherpa-onnx-master/build/compile_commands.json --config-file /userdata/voice/sherpa-onnx-master/.clang-tidy /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/base64-decode.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/bbpe.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/cat.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/circular-buffer.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/context-graph.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/endpoint.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/features.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/file-utils.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/fst-utils.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/homophone-replacer.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/hypothesis.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/jieba.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/keyword-spotter-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/keyword-spotter.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ctc-fst-decoder-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ctc-fst-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ctc-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-dolphin-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-dolphin-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-fire-red-asr-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-fire-red-asr-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-fire-red-asr-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-lm-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-lm.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-moonshine-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-moonshine-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-moonshine-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-nemo-enc-dec-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-nemo-enc-dec-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-paraformer-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-paraformer-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-paraformer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-recognizer-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-recognizer.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-rnn-lm.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-sense-voice-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-sense-voice-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-spleeter-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-spleeter-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-uvr-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation-uvr-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-source-separation.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-stream.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tdnn-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tdnn-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-telespeech-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-greedy-search-nemo-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-modified-beam-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-transducer-nemo-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-wenet-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-wenet-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-whisper-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-whisper-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-whisper-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-zipformer-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-zipformer-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-conformer-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-ctc-fst-decoder-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-ctc-fst-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-ctc-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-ebranchformer-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-lm-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-lm.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-lstm-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-nemo-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-nemo-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-paraformer-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-paraformer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-recognizer-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-recognizer.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-rnn-lm.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-stream.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-greedy-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-greedy-search-nemo-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-modified-beam-search-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-transducer-nemo-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-wenet-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-wenet-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-zipformer-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-zipformer2-ctc-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-zipformer2-ctc-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-zipformer2-transducer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/onnx-utils.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/packed-sequence.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/pad-sequence.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/parse-options.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/provider-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/provider.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/resample.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/session.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/silero-vad-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/silero-vad-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/slice.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/spoken-language-identification-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/spoken-language-identification.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/stack.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/symbol-table.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/text-utils.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/transducer-keyword-decoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/transpose.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/unbind.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/utils.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/vad-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/vad-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/voice-activity-detector.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/wave-reader.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/wave-writer.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/speaker-embedding-extractor-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/speaker-embedding-extractor-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/speaker-embedding-extractor-nemo-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/speaker-embedding-extractor.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/speaker-embedding-manager.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/audio-tagging-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/audio-tagging-label-file.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/audio-tagging-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/audio-tagging.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ced-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-zipformer-audio-tagging-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-zipformer-audio-tagging-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-ct-transformer-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-punctuation-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-punctuation-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-punctuation.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-cnn-bilstm-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-punctuation-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-punctuation-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/online-punctuation.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/hifigan-vocoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/jieba-lexicon.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/kokoro-multi-lang-lexicon.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/lexicon.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/melo-tts-lexicon.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-character-frontend.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-frontend.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-kokoro-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-kokoro-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-matcha-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-matcha-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-vits-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts-vits-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-tts.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/piper-phonemize-lexicon.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/vocoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/vocos-vocoder.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speech-denoiser-gtcrn-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speech-denoiser-gtcrn-model.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speech-denoiser-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speech-denoiser-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speech-denoiser.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/fast-clustering-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/fast-clustering.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-diarization-impl.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-diarization-result.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-diarization.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-segmentation-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-segmentation-pyannote-model-config.cc /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc/offline-speaker-segmentation-pyannote-model.cc

clang-tidy-check: sherpa-onnx/csrc/CMakeFiles/clang-tidy-check
clang-tidy-check: sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/build.make
.PHONY : clang-tidy-check

# Rule to build all files generated by this target.
sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/build: clang-tidy-check
.PHONY : sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/build

sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/clean:
	cd /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc && $(CMAKE_COMMAND) -P CMakeFiles/clang-tidy-check.dir/cmake_clean.cmake
.PHONY : sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/clean

sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/depend:
	cd /userdata/voice/sherpa-onnx-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /userdata/voice/sherpa-onnx-master /userdata/voice/sherpa-onnx-master/sherpa-onnx/csrc /userdata/voice/sherpa-onnx-master/build /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc /userdata/voice/sherpa-onnx-master/build/sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sherpa-onnx/csrc/CMakeFiles/clang-tidy-check.dir/depend

