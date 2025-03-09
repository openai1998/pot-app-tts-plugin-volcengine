#!/usr/bin/env python
# -*- coding: utf-8 -*-

from volcengine_tts import VolcengineTTS

def main():
    # 创建TTS实例
    tts = VolcengineTTS()

    # 示例1：简体中文，默认发音人
    print("\n示例1：简体中文，默认发音人")
    tts.tts(
        text="你好，这是一个基于火山引擎的语音合成工具，无需API密钥，可以直接使用。",
        lang="zh_cn",
        output_file="example_zh.mp3"
    )

    # 示例2：英语，指定发音人
    print("\n示例2：英语，指定发音人")
    tts.tts(
        text="Hello, this is a TTS tool based on Volcengine API. No API key required.",
        lang="en",
        speaker="en_female_sarah",
        output_file="example_en.mp3"
    )

    # 示例3：日语，指定发音人
    print("\n示例3：日语，指定发音人")
    tts.tts(
        text="こんにちは、これは火山エンジンベースの音声合成ツールです。APIキーは必要ありません。",
        lang="ja",
        speaker="jp_male_satoshi",
        output_file="example_ja.mp3"
    )

    print("\n所有示例音频已生成完毕！")

if __name__ == "__main__":
    main()
