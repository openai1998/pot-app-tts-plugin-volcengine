# HS引擎TTS语音合成工具

这是一个基于HS引擎API的本地TTS语音合成工具，无需API密钥，可以直接使用。通过调用HS引擎的公开API接口，实现高质量的多语言语音合成功能。

## 功能特点

- **无需API密钥**：直接使用HS引擎的公开API，无需认证
- **多语言支持**：支持17种语言，包括中文（简体、繁体）、英语、日语、韩语等
- **丰富的发音人选择**：每种语言提供多种不同风格的发音人选项
- **批量处理**：支持从TXT或CSV文件批量转换文本为语音
- **灵活的输出选项**：可以将合成的音频保存为文件或直接播放
- **简单易用**：提供命令行界面和Python API，方便集成到其他项目中

## 安装

1. 克隆或下载本仓库
2. 安装依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python volcengine_tts.py --text "你好，世界！"
```

这将使用默认的中文发音人合成语音并播放。

### 指定语言和发音人

```bash
python volcengine_tts.py --text "Hello, world!" --lang en --speaker en_male_adam
```

### 保存到文件

```bash
python volcengine_tts.py --text "你好，世界！" --output hello.mp3
```

### 查看可用的发音人

```bash
python volcengine_tts.py --list-speakers --lang zh_cn
```

### 完整参数说明

```
usage: volcengine_tts.py [-h] [--text TEXT] [--lang LANG] [--speaker SPEAKER]
                         [--output OUTPUT] [--no-play] [--list-speakers]

HS引擎TTS语音合成工具

optional arguments:
  -h, --help            显示帮助信息并退出
  --text TEXT, -t TEXT  要转换为语音的文本
  --lang LANG, -l LANG  语言代码 (默认: zh_cn)
  --speaker SPEAKER, -s SPEAKER
                        发音人ID
  --output OUTPUT, -o OUTPUT
                        输出文件路径
  --no-play             不播放生成的音频
  --list-speakers       列出指定语言的所有可用发音人
```

## 支持的语言和发音人

本工具支持以下17种语言，每种语言提供多种不同风格的发音人选项。

### 简体中文 (zh_cn)

| 发音人昵称 | 发音人ID                     | 风格特点         |
| ----- | ------------------------- | ------------ |
| 影视配音  | zh_male_xiaoming          | 标准男声，适合正式场合  |
| 嘻哈歌手  | zh_male_rap               | 活力四射，适合年轻化内容 |
| 四川女声  | zh_female_sichuan         | 带有四川口音的女声    |
| 东北男声  | tts.other.BV021_streaming | 带有东北口音的男声    |
| 粤语男声  | tts.other.BV026_streaming | 广东话男声        |
| 台湾女声  | tts.other.BV025_streaming | 带有台湾口音的女声    |
| 男主播   | zh_male_zhubo             | 专业播音风格       |
| 女主播   | zh_female_zhubo           | 专业播音风格       |
| 清新女声  | zh_female_qingxin         | 温柔自然，适合轻松内容  |
| 少儿故事  | zh_female_story           | 生动活泼，适合儿童内容  |

### 繁体中文 (zh_tw)

与简体中文相同的发音人选项。

### 英语 (en)

| 发音人昵称 | 发音人ID                          | 风格特点     |
| ----- | ------------------------------ | -------- |
| 美式男声  | en_male_adam                   | 标准美式英语男声 |
| 美式女声  | tts.other.BV027_streaming      | 标准美式英语女声 |
| 英式男声  | en_male_bob                    | 标准英式英语男声 |
| 英式女声  | tts.other.BV032_TOBI_streaming | 标准英式英语女声 |
| 澳洲男声  | tts.other.BV516_streaming      | 澳大利亚口音男声 |
| 澳洲女声  | en_female_sarah                | 澳大利亚口音女声 |

### 日语 (ja)

| 发音人昵称 | 发音人ID           | 风格特点   |
| ----- | --------------- | ------ |
| 日语男声  | jp_male_satoshi | 标准日语男声 |
| 日语女声  | jp_female_mai   | 标准日语女声 |

### 韩语 (ko)

| 发音人昵称 | 发音人ID                     | 风格特点   |
| ----- | ------------------------- | ------ |
| 韩语男声  | kr_male_gye               | 标准韩语男声 |
| 韩语女声  | tts.other.BV059_streaming | 标准韩语女声 |

### 法语 (fr)

| 发音人昵称 | 发音人ID                     | 风格特点   |
| ----- | ------------------------- | ------ |
| 法语男声  | fr_male_enzo              | 标准法语男声 |
| 法语女声  | tts.other.BV078_streaming | 标准法语女声 |

### 西班牙语 (es)

| 发音人昵称 | 发音人ID                     | 风格特点     |
| ----- | ------------------------- | -------- |
| 西语男声  | es_male_george            | 标准西班牙语男声 |
| 西语女声  | tts.other.BV065_streaming | 标准西班牙语女声 |

### 俄语 (ru)

| 发音人昵称 | 发音人ID                     | 风格特点   |
| ----- | ------------------------- | ------ |
| 俄语女声  | tts.other.BV068_streaming | 标准俄语女声 |

### 德语 (de)

| 发音人昵称 | 发音人ID            | 风格特点   |
| ----- | ---------------- | ------ |
| 德语女声  | de_female_sophie | 标准德语女声 |

### 意大利语 (it)

| 发音人昵称 | 发音人ID                     | 风格特点     |
| ----- | ------------------------- | -------- |
| 意语男声  | tts.other.BV087_streaming | 标准意大利语男声 |

### 土耳其语 (tr)

| 发音人昵称 | 发音人ID                     | 风格特点     |
| ----- | ------------------------- | -------- |
| 土耳其男声 | tts.other.BV083_streaming | 标准土耳其语男声 |

### 葡萄牙语 (pt_pt) 和 巴西葡萄牙语 (pt_br)

| 发音人昵称 | 发音人ID                     | 风格特点     |
| ----- | ------------------------- | -------- |
| 葡语男声  | tts.other.BV531_streaming | 标准葡萄牙语男声 |
| 葡语女声  | pt_female_alice           | 标准葡萄牙语女声 |

### 越南语 (vi)

| 发音人昵称 | 发音人ID                     | 风格特点    |
| ----- | ------------------------- | ------- |
| 越南男声  | tts.other.BV075_streaming | 标准越南语男声 |
| 越南女声  | tts.other.BV074_streaming | 标准越南语女声 |

### 马来语 (ms)

| 发音人昵称 | 发音人ID                     | 风格特点    |
| ----- | ------------------------- | ------- |
| 马来女声  | tts.other.BV092_streaming | 标准马来语女声 |

### 阿拉伯语 (ar)

| 发音人昵称 | 发音人ID                     | 风格特点     |
| ----- | ------------------------- | -------- |
| 阿语男声  | tts.other.BV570_streaming | 标准阿拉伯语男声 |

### 印尼语 (hi)

| 发音人昵称 | 发音人ID                     | 风格特点    |
| ----- | ------------------------- | ------- |
| 印尼男声  | tts.other.BV160_streaming | 标准印尼语男声 |
| 印尼女声  | id_female_noor            | 标准印尼语女声 |

## 示例

### 中文示例

```bash
# 使用清新女声
python volcengine_tts.py --text "这是一个基于HS引擎的语音合成工具，无需API密钥，可以直接使用。" --lang zh_cn --speaker zh_female_qingxin

# 使用四川女声
python volcengine_tts.py --text "这个工具真的很好用哦！" --lang zh_cn --speaker zh_female_sichuan

# 使用嘻哈歌手风格
python volcengine_tts.py --text "嘿，朋友，试试这个超酷的语音合成工具吧！" --lang zh_cn --speaker zh_male_rap
```

### 英文示例

```bash
# 使用美式女声
python volcengine_tts.py --text "This is a TTS tool based on Volcengine API. No API key required." --lang en --speaker tts.other.BV027_streaming

# 使用英式男声
python volcengine_tts.py --text "Hello, this is a test for British English voice." --lang en --speaker en_male_bob

# 使用澳洲女声
python volcengine_tts.py --text "G'day mate! How are you doing today?" --lang en --speaker en_female_sarah
```

### 日语示例

```bash
python volcengine_tts.py --text "こんにちは、これはHSエンジンベースの音声合成ツールです。" --lang ja --speaker jp_male_satoshi
```

### 韩语示例

```bash
python volcengine_tts.py --text "안녕하세요, 이것은 화산 엔진 기반 음성 합성 도구입니다." --lang ko --speaker kr_male_gye
```

## 批量处理

除了基本的单条文本转语音功能外，本工具还支持批量处理功能，可以从TXT或CSV文件中读取多条文本并批量转换为语音文件。

### 从TXT文件批量转换

TXT文件中每行一条文本，所有文本使用相同的语言和发音人：

```bash
python batch_tts.py --input texts.txt --lang zh_cn --speaker zh_female_qingxin --output-dir output
```

### 将整个TXT文件作为一个文本处理

如果您希望将整个TXT文件的内容作为一个整体来处理，而不是按行分割，可以使用`--whole-file`或`-w`选项：

```bash
python batch_tts.py --input example.txt --lang zh_cn --speaker zh_female_qingxin --whole-file
```

这将生成一个包含整个文件内容的音频文件。默认情况下，输出文件名将基于输入文件名（例如，`example.txt`将生成`example.mp3`）。

您也可以使用`--output`选项指定输出文件名：

```bash
python batch_tts.py --input example.txt --lang zh_cn --speaker zh_female_qingxin --whole-file --output my_audio.mp3
```

这个功能特别适合处理以下场景：

- 长篇文章或故事的语音合成
- 演讲稿或脚本的语音合成
- 需要保持整体连贯性的文本

### 从CSV文件批量转换

CSV文件可以为每条文本指定不同的语言和发音人，非常适合多语言混合场景：

```bash
python batch_tts.py --input example.csv --output-dir output
```

#### CSV文件格式

CSV文件应包含以下列（列名不区分大小写）：

- 文本/text：要转换的文本内容
- 语言/lang：语言代码
- 发音人/speaker：发音人ID（可选）

**注意**：如果文本中包含逗号，请使用引号将文本包围起来，例如：

```
文本,语言,发音人
"你好，世界！",zh_cn,zh_female_qingxin
"Hello, world!",en,en_male_adam
"こんにちは、世界！",ja,jp_male_satoshi
"안녕하세요, 세계!",ko,kr_male_gye
```

#### 完整参数说明

```
usage: batch_tts.py [-h] --input INPUT [--output-dir OUTPUT_DIR]
                    [--output OUTPUT] [--lang LANG] [--speaker SPEAKER]
                    [--prefix PREFIX] [--delimiter DELIMITER]
                    [--quotechar QUOTECHAR] [--whole-file]

批量文本转语音工具

optional arguments:
  -h, --help            显示帮助信息并退出
  --input INPUT, -i INPUT
                        输入文件路径 (.txt 或 .csv)
  --output-dir OUTPUT_DIR, -o OUTPUT_DIR
                        输出目录 (默认: output)
  --output OUTPUT       输出文件名 (仅在处理整个TXT文件为一个音频时使用)
  --lang LANG, -l LANG  语言代码 (默认: zh_cn，仅用于txt文件)
  --speaker SPEAKER, -s SPEAKER
                        发音人ID (仅用于txt文件)
  --prefix PREFIX, -p PREFIX
                        输出文件名前缀 (默认: audio)
  --delimiter DELIMITER, -d DELIMITER
                        CSV文件分隔符 (默认: ,)
  --quotechar QUOTECHAR, -q QUOTECHAR
                        CSV文件引号字符 (默认: ")
  --whole-file, -w      将整个TXT文件作为一个文本处理，生成一个音频文件
```

## 在Python代码中使用

您也可以在自己的Python代码中直接使用VolcengineTTS类：

```python
from volcengine_tts import VolcengineTTS

# 创建TTS实例
tts = VolcengineTTS()

# 简体中文，使用清新女声
tts.tts(
    text="这是一个测试文本",
    lang="zh_cn",
    speaker="zh_female_qingxin",
    output_file="output/chinese.mp3"
)

# 英语，使用美式男声
tts.tts(
    text="This is a test text",
    lang="en",
    speaker="en_male_adam",
    output_file="output/english.mp3"
)

# 查看特定语言的可用发音人
tts.list_speakers("zh_cn")
```

## 技术原理

本工具通过调用HS引擎的公开API接口实现语音合成功能。主要流程如下：

1. 接收用户输入的文本、语言和发音人参数
2. 将语言代码映射为API所需的格式
3. 构建HTTP请求，发送到HS引擎API
4. 接收API返回的Base64编码音频数据
5. 解码音频数据并保存为MP3文件或直接播放

API请求示例：

```
POST https://translate.volcengine.com/crx/tts/v1/
Content-Type: application/json

{
  "text": "要合成的文本",
  "speaker": "zh_female_qingxin",
  "language": "zh"
}
```

## 注意事项

- 本工具仅供学习和研究使用
- 请勿用于商业用途
- 请遵守HS引擎的使用条款和条件
- 单次请求的文本长度有限制，过长的文本可能会被截断
- 某些语言和发音人组合可能不可用，请使用`--list-speakers`选项查看可用的发音人

## 常见问题

### Q: 为什么不需要API密钥？

A: 本工具利用HS引擎翻译服务的公开TTS接口，该接口目前不要求API密钥。

### Q: 音频质量如何？

A: HS引擎提供的TTS服务音质较高，接近专业配音水平，特别是中文和英文的合成效果非常自然。

### Q: 有字数限制吗？

A: 是的，单次请求的文本长度有限制。对于较长的文本，建议分段处理或使用批量处理功能。

### Q: 支持自定义发音人吗？

A: 目前不支持自定义发音人，只能使用HS引擎提供的预设发音人。

### Q: 如何处理特殊符号和数字？

A: HS引擎TTS服务会自动处理文本中的特殊符号和数字，将其转换为自然语言表达。
