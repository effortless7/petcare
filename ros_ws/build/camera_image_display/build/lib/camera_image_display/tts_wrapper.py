import os
from typing import Optional

class Speaker:
    """
    封装了 Sherpa-Onnx TTS 功能的类，用于播放语音。
    初始化时加载一次模型路径，之后可以多次调用 speak 方法。
    """
    _instance: Optional['Speaker'] = None

    def __init__(self,
                 tts_executable: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/build/bin/sherpa-onnx-offline-tts-play-alsa",
                 acoustic_model: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/matcha-icefall-zh-baker/model-steps-3.onnx",
                 vocoder: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/vocos-22khz-univ.onnx",
                 lexicon: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/matcha-icefall-zh-baker/lexicon.txt",
                 tokens: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/matcha-icefall-zh-baker/tokens.txt",
                 dict_dir: str = "/home/elf/sherpa-onnx-master1/sherpa-onnx-master/matcha-icefall-zh-baker/dict"):
        """
        使用所有必需的模型和程序路径来初始化 Speaker
        """
        self.tts_executable = tts_executable
        self.acoustic_model = acoustic_model
        self.vocoder = vocoder
        self.lexicon = lexicon
        self.tokens = tokens
        self.dict_dir = dict_dir

        if not os.path.exists(self.tts_executable):
            raise FileNotFoundError(
                f"错误: 找不到TTS可执行文件 '{self.tts_executable}'"
            )

    @classmethod
    def get_instance(cls) -> 'Speaker':
        """
        获取Speaker的单例实例
        """
        if cls._instance is None:
            cls._instance = Speaker()
        return cls._instance

    def speak(self, text: str):
        """
        将给定的文本通过系统音频播放出来
        """
        if not text or not text.strip():
            print("警告: 传入了空文本，不进行播放。")
            return

        import subprocess
        print(f"准备说: {text}")

        command = [
            self.tts_executable,
            f"--matcha-acoustic-model={self.acoustic_model}",
            f"--matcha-vocoder={self.vocoder}",
            f"--matcha-lexicon={self.lexicon}",
            f"--matcha-tokens={self.tokens}",
            f"--matcha-dict-dir={self.dict_dir}",
            text.strip(),
        ]

        try:
            subprocess.run(
                command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8')
            print(f"!!!!!! 播放时出错 !!!!!!\n"
                  f"错误码: {e.returncode}\n"
                  f"详细信息:\n{error_message}")
        except FileNotFoundError:
            print(f"错误: 无法找到命令 '{self.tts_executable}'。")

# 为了保持向后兼容，提供一个全局的speak函数
def speak(text: str):
    """
    全局speak函数，内部使用Speaker类的单例
    """
    Speaker.get_instance().speak(text)
