#!/bin/bash

# 这是一个中文语音合成（TTS）的快捷脚本

# 检查用户是否提供了要转换的文本和输出文件名
if [ "$#" -ne 2 ]; then
    echo "用法: ./say.sh '您要说的话' '输出文件名.wav'"
    echo "例如: ./say.sh '你好世界' 'hello.wav'"
    exit 1
fi

TEXT_TO_SAY="$1"
OUTPUT_FILENAME="$2"

echo "正在合成语音..."

# --- 这是您之前成功运行的核心命令 ---
./build/bin/sherpa-onnx-offline-tts \
  --matcha-acoustic-model=./matcha-icefall-zh-baker/model-steps-3.onnx \
  --matcha-vocoder=./vocos-22khz-univ.onnx \
  --matcha-lexicon=./matcha-icefall-zh-baker/lexicon.txt \
  --matcha-tokens=./matcha-icefall-zh-baker/tokens.txt \
  --matcha-dict-dir=./matcha-icefall-zh-baker/dict \
  --num-threads=2 \
  --output-filename="$OUTPUT_FILENAME" \
  "$TEXT_TO_SAY"

echo "成功！音频已保存到 $OUTPUT_FILENAME" 