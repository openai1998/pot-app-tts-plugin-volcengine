#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import csv
from volcengine_tts import VolcengineTTS

def read_text_file(file_path, as_whole=False):
    """
    读取文本文件，返回文本内容列表

    参数:
        file_path: 文本文件路径
        as_whole: 是否将整个文件作为一个文本处理
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        if as_whole:
            # 读取整个文件内容作为一个字符串
            return [f.read().strip()]
        else:
            # 按行读取
            lines = [line.strip() for line in f.readlines() if line.strip()]
            return lines

def read_csv_file(file_path, delimiter=',', quotechar='"'):
    """
    读取CSV文件，返回文本内容和语言代码的列表

    参数:
        file_path: CSV文件路径
        delimiter: 列分隔符
        quotechar: 引号字符
    """
    items = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 使用csv.reader并指定分隔符和引号字符
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
            header = next(reader, None)  # 跳过表头

            # 默认列索引
            text_idx = 0
            lang_idx = 1
            speaker_idx = 2

            if header:
                # 尝试找到正确的列索引
                for i, col in enumerate(header):
                    col_lower = col.lower()
                    if 'text' in col_lower or '文本' in col_lower:
                        text_idx = i
                    elif 'lang' in col_lower or '语言' in col_lower:
                        lang_idx = i
                    elif 'speaker' in col_lower or '发音人' in col_lower:
                        speaker_idx = i

                print(f"检测到列索引: 文本={text_idx}, 语言={lang_idx}, 发音人={speaker_idx}")

            for row in reader:
                # 确保行有足够的列
                if len(row) <= max(text_idx, lang_idx):
                    print(f"警告: 跳过格式不正确的行: {row}")
                    continue

                text = row[text_idx].strip()
                lang = row[lang_idx].strip()
                speaker = row[speaker_idx].strip() if len(row) > speaker_idx else None

                if text and lang:  # 确保文本和语言都不为空
                    items.append({
                        'text': text,
                        'lang': lang,
                        'speaker': speaker if speaker else None
                    })
                else:
                    print(f"警告: 跳过缺少文本或语言的行: {row}")
    except Exception as e:
        print(f"读取CSV文件时出错: {e}")
        print("尝试使用备用方法读取...")

        # 备用方法：按行读取并手动分割
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # 获取表头
            header = lines[0].strip().split(delimiter)

            # 尝试找到正确的列索引
            text_idx = 0
            lang_idx = 1
            speaker_idx = 2

            for i, col in enumerate(header):
                col_lower = col.lower()
                if 'text' in col_lower or '文本' in col_lower:
                    text_idx = i
                elif 'lang' in col_lower or '语言' in col_lower:
                    lang_idx = i
                elif 'speaker' in col_lower or '发音人' in col_lower:
                    speaker_idx = i

            print(f"备用方法 - 检测到列索引: 文本={text_idx}, 语言={lang_idx}, 发音人={speaker_idx}")

            # 处理数据行
            for i in range(1, len(lines)):
                line = lines[i].strip()
                if not line:
                    continue

                # 手动处理引号内的逗号
                parts = []
                in_quotes = False
                current_part = ""

                for char in line:
                    if char == quotechar:
                        in_quotes = not in_quotes
                    elif char == delimiter and not in_quotes:
                        parts.append(current_part)
                        current_part = ""
                    else:
                        current_part += char

                # 添加最后一部分
                if current_part:
                    parts.append(current_part)

                # 确保行有足够的列
                if len(parts) <= max(text_idx, lang_idx):
                    print(f"警告: 跳过格式不正确的行: {line}")
                    continue

                text = parts[text_idx].strip().strip(quotechar)
                lang = parts[lang_idx].strip()
                speaker = parts[speaker_idx].strip() if len(parts) > speaker_idx else None

                if text and lang:  # 确保文本和语言都不为空
                    items.append({
                        'text': text,
                        'lang': lang,
                        'speaker': speaker if speaker else None
                    })
                else:
                    print(f"警告: 跳过缺少文本或语言的行: {line}")

    return items

def main():
    parser = argparse.ArgumentParser(description="批量文本转语音工具")
    parser.add_argument("--input", "-i", required=True, help="输入文件路径 (.txt 或 .csv)")
    parser.add_argument("--output-dir", "-o", default="output", help="输出目录 (默认: output)")
    parser.add_argument("--output", help="输出文件名 (仅在处理整个TXT文件为一个音频时使用)")
    parser.add_argument("--lang", "-l", default="zh_cn", help="语言代码 (默认: zh_cn，仅用于txt文件)")
    parser.add_argument("--speaker", "-s", help="发音人ID (仅用于txt文件)")
    parser.add_argument("--prefix", "-p", default="audio", help="输出文件名前缀 (默认: audio)")
    parser.add_argument("--delimiter", "-d", default=",", help="CSV文件分隔符 (默认: ,)")
    parser.add_argument("--quotechar", "-q", default='"', help="CSV文件引号字符 (默认: \")")
    parser.add_argument("--whole-file", "-w", action="store_true", help="将整个TXT文件作为一个文本处理，生成一个音频文件")

    args = parser.parse_args()

    # 检查输入文件是否存在
    if not os.path.exists(args.input):
        print(f"错误: 输入文件 '{args.input}' 不存在")
        return

    # 创建输出目录
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # 创建TTS实例
    tts = VolcengineTTS()

    # 根据文件类型读取输入
    file_ext = os.path.splitext(args.input)[1].lower()

    if file_ext == '.csv':
        items = read_csv_file(args.input, delimiter=args.delimiter, quotechar=args.quotechar)
        print(f"从CSV文件中读取了 {len(items)} 条记录")

        for i, item in enumerate(items):
            text = item['text']
            lang = item['lang'] or args.lang
            speaker = item['speaker'] or args.speaker

            output_file = os.path.join(args.output_dir, f"{args.prefix}_{i+1}.mp3")

            print(f"\n[{i+1}/{len(items)}] 正在处理: {text[:30]}{'...' if len(text) > 30 else ''}")
            print(f"语言: {lang}, 发音人: {speaker or '默认'}")

            try:
                tts.tts(
                    text=text,
                    lang=lang,
                    speaker=speaker,
                    output_file=output_file,
                    play=False
                )
            except Exception as e:
                print(f"错误: {e}")

    elif file_ext == '.txt':
        # 根据参数决定是否将整个文件作为一个文本处理
        lines = read_text_file(args.input, as_whole=args.whole_file)

        if args.whole_file:
            print("将整个TXT文件作为一个文本处理")

            # 使用指定的输出文件名或默认名称
            if args.output:
                output_file = os.path.join(args.output_dir, args.output)
            else:
                # 使用输入文件名作为输出文件名
                input_filename = os.path.basename(args.input)
                output_filename = os.path.splitext(input_filename)[0] + ".mp3"
                output_file = os.path.join(args.output_dir, output_filename)

            text = lines[0]  # 整个文件内容
            print(f"文本长度: {len(text)} 字符")
            print(f"前30个字符: {text[:30]}...")

            try:
                tts.tts(
                    text=text,
                    lang=args.lang,
                    speaker=args.speaker,
                    output_file=output_file,
                    play=False
                )
                print(f"\n音频已保存到: {output_file}")
            except Exception as e:
                print(f"错误: {e}")
        else:
            # 按行处理
            print(f"从TXT文件中读取了 {len(lines)} 行文本")

            for i, text in enumerate(lines):
                output_file = os.path.join(args.output_dir, f"{args.prefix}_{i+1}.mp3")

                print(f"\n[{i+1}/{len(lines)}] 正在处理: {text[:30]}{'...' if len(text) > 30 else ''}")

                try:
                    tts.tts(
                        text=text,
                        lang=args.lang,
                        speaker=args.speaker,
                        output_file=output_file,
                        play=False
                    )
                except Exception as e:
                    print(f"错误: {e}")
    else:
        print(f"错误: 不支持的文件类型 '{file_ext}'，请使用 .txt 或 .csv 文件")
        return

    print("\n所有音频文件已生成完毕！")
    print(f"输出目录: {os.path.abspath(args.output_dir)}")

if __name__ == "__main__":
    main()
