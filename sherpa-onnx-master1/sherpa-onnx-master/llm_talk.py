import subprocess
import os

class Speaker:
    """
    一个封装了 Sherpa-Onnx TTS 功能的类，用于播放语音。
    初始化时加载一次模型路径，之后可以多次调用 .say() 方法。
    """

    def __init__(self,
                 tts_executable: str,
                 acoustic_model: str,
                 vocoder: str,
                 lexicon: str,
                 tokens: str,
                 dict_dir: str):
        """
        使用所有必需的模型和程序路径来初始化 Speaker。
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

    def say(self, text_to_say: str):
        """
        将给定的文本通过系统音频播放出来。
        """
        if not text_to_say:
            print("警告: 传入了空文本，不进行播放。")
            return

        print(f"准备说: {text_to_say}")

        # 构建完整的命令行指令，使用 --key=value 的格式
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
            # 使用 subprocess 运行命令。
            # 我们将 stdout 隐藏，但保留 stderr，以便在出错时捕获详细日志
            subprocess.run(
                command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError as e:
            # 如果命令执行失败，打印出详细的错误信息
            error_message = e.stderr.decode('utf-8')
            print(f"!!!!!! 播放时出错 !!!!!!\n"
                  f"错误码: {e.returncode}\n"
                  f"详细信息:\n{error_message}")
        except FileNotFoundError:
            print(f"错误: 无法找到命令 '{self.tts_executable}'。")


def simulate_llm_output():
    """
    这是一个模拟函数，用来模仿大模型逐句生成文本。
    """
    yield "你好，我是一个大型语言模型。"
    yield "现在，我被封装在了一个'Speaker'类里。"
    yield "这让调用我说话变得非常方便和整洁。"


if __name__ == "__main__":
    # --- 1. 配置 ---
    # 在这里集中配置所有路径
    try:
        speaker = Speaker(
            tts_executable="./build/bin/sherpa-onnx-offline-tts-play-alsa",
            acoustic_model="./matcha-icefall-zh-baker/model-steps-3.onnx",
            vocoder="./vocos-22khz-univ.onnx",
            lexicon="./matcha-icefall-zh-baker/lexicon.txt",
            tokens="./matcha-icefall-zh-baker/tokens.txt",
            dict_dir="./matcha-icefall-zh-baker/dict",
        )

        # --- 2. 使用 ---
        # 现在，您只需要调用 speaker.say() 即可
        # 您可以在您的主代码中创建这个 speaker 对象，然后在任何需要的地方调用它
       # for sentence in simulate_llm_output():
       #     speaker.say(sentence)

        speaker.say("当夜幕降临，星光点点，伴随着微风拂面，我在静谧中感受着时光的流转，思念如涟漪荡漾，梦境如画卷展开，我与自然融为一体，沉静在这片宁静的美丽之中，感受着生命的奇迹与温柔.")

    except FileNotFoundError as e:
        print(e)

    print("\n所有演示播放完成！") 