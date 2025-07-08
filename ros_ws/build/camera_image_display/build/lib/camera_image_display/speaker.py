import subprocess
import os

class Speaker:
    """
    封装 Sherpa-Onnx TTS 功能的类。
    """
    def __init__(self, tts_executable, acoustic_model, vocoder, lexicon, tokens, dict_dir):
        self.tts_executable = tts_executable
        self.acoustic_model = acoustic_model
        self.vocoder = vocoder
        self.lexicon = lexicon
        self.tokens = tokens
        self.dict_dir = dict_dir

        if not os.path.exists(self.tts_executable):
            raise FileNotFoundError(f"错误: 找不到TTS可执行文件 '{self.tts_executable}'")

    def say(self, text_to_say: str):
        if not text_to_say:
            print("警告: 传入了空文本，不进行播放。")
            return

        print(f"准备说: {text_to_say}")

        command = [
            self.tts_executable,
            f"--matcha-acoustic-model={self.acoustic_model}",
            f"--matcha-vocoder={self.vocoder}",
            f"--matcha-lexicon={self.lexicon}",
            f"--matcha-tokens={self.tokens}",
            f"--matcha-dict-dir={self.dict_dir}",
            text_to_say,
        ]

        try:
            subprocess.run(
                command,
                check=True,
                #stdout=subprocess.DEVNULL,
                #stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8')
            print(f"!!!!!! 播放时出错 !!!!!!\n错误码: {e.returncode}\n详细信息:\n{error_message}")
        except FileNotFoundError:
            print(f"错误: 无法找到命令 '{self.tts_executable}'。")