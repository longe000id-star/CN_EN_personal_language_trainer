 20     # 去掉含中文的说明段
 21     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
 22     # 去掉孤立括号残留（如开头的 "("）
 NORMAL  vocab_to_json.py                    utf-8    python  Top    1:1
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md output.jso Base/Data_KB/八级_vocab_english.md
解析中...
完成！已写入: output5.json
   共 1 大部分
   共 1 个分类
   共 1 个子分类
   共 757 个词条
  6
  7 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
 18     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
 19     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
 20     # 去掉含中文的说明段
 21     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
 22     # vocab_to_json.py                 utf-8     1:1  
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，>    自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md out    put.json
  6
  7 如果不指定文件名，默认读取 vocab.md，输>    出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中>    文说明、括号内容等。"""    @@@@    #<utf-8    python  Top    1:1  1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 J    SON，自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.    md output.json
  6
  7 如果不指定文件名，默认读取 vocab.m    d，输出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> l    ist:
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSO    N，自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md     output.json
  6
  7 如果不指定文件名，默认读取 vocab.md>    ，输出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> lis    t:
 17     """从原始文本中提取单词列表，去>    除中文说明、括号内容等。"""
 NORMAL <8    python  Top    1:1
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，>    自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md out    put.json
  6
  7 如果不指定文件名，默认读取 vocab.md，输>    出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中>    文说  7             while i + 1 < len(lines) and     lines[i+1].strip() and \
  6                   not re.match(r"^[-#]",     lines[i+1].strip()):
  5                 i += 1
  4
  3         # 子分类: - **标题:** (冒号在 bol    d 内)
  2         elif re.match(r"^-\s+\*\*", line)     or re.match(r"^\*\*[^*]+:\*\*\s*$", line    ):
  1             m = re.search(r"\*\*([^*:]+):    ?\*\*", line)
103             title = m.group(1).strip() if     m else "Unknown"
  1             # 收集词汇行
  2             words_raw = ""
  3             after = re.sub(r"^.*?\*\*\s*[    :：]?\s*", "", line).strip()
  4             if after:
  5                 words_raw += after + ","   6
  7             j = i + 1
 COMMAND <utf-8    python  50%  103:57
/afteri
  7             while i + 1 < len(lines) and li    n s[i+1].strip() and \
  6                   not re.match(r"^[-#]", li    n s[i+1].strip()):
  5                 i += 1
  4
  3         # 子分类: - **标题:** (冒号在 bold       )
  2         elif re.match(r"^-\s+\*\*", line) o    r re.match(r"^\*\*[^*]+:\*\*\s*$", line):
  1             m = re.search(r"\*\*([^*:]+):?\    *\*", line)
 03             title = m.group(1).strip() if m     else "Unknown"
  1             # 收集词汇行
  2             words_raw = ""
  3             after = re.sub(r"^.*?\*\*\s*[:>    ：]?\s*", "", line).strip()
  4             if after:
  5                 words_raw += after + ","
  6
  7             j = i + 1
  8             while j < len(lines):
 COMMAND <  utf-8    python  50%  103:57
/afteri
  7             while i + 1 < len(lines) and lines[i+1    ].strip() and \
  6                   not re.match(r"^[-#]", lines[i+1    ].strip()):
  5                 i += 1
  4
  3         # 子分类: - **标题:** (冒号在 bold 内)
  2         elif re.match(r"^-\s+\*\*", line) or re.ma    tch(r"^\*\*[^*]+:\*\*\s*$", line):
  1             m = re.search(r"\*\*([^*:]+):?\*\*", l    ine)
 03             title = m.group(1).strip() if m else "    Unknown"
  1             # 收集词汇行
  2             words_raw = ""
  3             after = re.sub(r"^.*?\*\*\s*[:：]?\s*"    , "", line).strip()
  4             if after:
  5                 words_raw += after + ","
  6
  7             j = i + 1
  8             while j < len(lines):
  9                 nl = lines[j]
 COMMAND <.py [+]  utf-8    python  50%  103:57
/afteri
明、括号内容等。"""
 18     # 去掉 (xxx): 格式的说明前缀（含@@@@
 NORMAL <utf-8    python  Top    1:1
 17     """从原始文本中提取单词列表，>    去除中文说明、括号内容等。"""
 NORMAL <   python  Top    1:1
L 
longe@192 ~/d/d/datastr> nvim output5.json
longe@192 ~/d/d/datastr> rm output5.json
longe@192 ~/d/d/datastr> nvim
longe@192 ~/d/d/datastr> nvim vocab_to_json.py
longe@192 ~/d/d/datastr> python3 vocab_to_json.py "/Users/longe/Dropbox/Long E/Longe's Knowledge Base/Data_KB/八级_vocab_english.md" output5.json
读取: /Users/longe/Dropbox/Long E/Longe's Knowledge Base/Data_KB/八级_vocab_english.md
解析中...
完成！已写入: output5.json
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOT    E 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md output.json
  6
  7 如果不指定文件名，默认读取 vocab.md，输出 vocab.jso    n
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中文说明、括号    内容等。"""
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE >    部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md output.json
  6
  7 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中文说明、括号内>    容等。"""
 18     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标    签）
 19     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
 NORMAL 


         <b_to_json.py  utf-8    python  Top    1:1
1   """
  1 vocab_to_json.py
  2 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE 部分。
  3
  4 使用方法:
  5     python vocab_to_json.py input.md output.json
  6
  7 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
  8 """
  9
 10 import re
 11 import json
 12 import sys
 13 from pathlib import Path
 14
 15
 16 def clean_word_list(raw: str) -> list:
 17     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
 18     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
 19     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
 20     # 去掉含中文的说明段
 21     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
 22     # 去掉孤立括号残留（如开头的 "("）
 NORMAL  vocab_to_json.py                                                             utf-8    python  Top    1:1
 18     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头>    的标签）
 20     python vocab_to_json.py input.md output.json
 19
 18 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
 NORMAL  vocab_to_json.py                                                                                      utf-8    python  12%   26:1
 22
 NORMAL <o_json.py  utf-8    python  Top    1:1
 20     python vocab_to_json.py input.md output.json
 19
 18 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.                                                                                   vocab_to_json.py                                                                                utf-8    pyt  26:1  
   共 1 大部分
   共 1 个分类
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
 NORMAL  vocab_to_json.py                   utf-8    python  12%   26:1
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括>    号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头    的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw    )
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ",     raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj@@@
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括>    号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头    的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw    )
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ",     raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj@@@
 NORMAL <_json.py  utf-8    python  12%   26:1
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号    内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头>    的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ",     raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pro    n|v)\.\s*', '', raw)
 NORMAL <o_json.py  utf-8    python  12%   26:1
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内>    容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标    签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw    )
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v    )\.\s*', '', raw)
 NORMAL <b_to_json.py  utf-8    python  12%   26:1
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。    """
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v)\.\s    *', '', raw)
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。"    ""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v)\.\s*    ', '', raw)
  2     # 去掉斜杠分隔符（词性列表用的）
  3     raw = raw.replace("/", ",").replace(".", " ").replace@@@
 NORMAL  vocab_to_json.py    utf-8    python  12%   26:1
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。""    "
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v)\.\s*'    , '', raw)
  2     # 去掉斜杠分隔符（词性列表用的）
  3     raw = raw.replace("/", ",").replace(".", " ").replace(";"

   @@@
 NORMAL  vocab_to_json.py     utf-8    python  12%   26:1
 17 """
 16
 15 import re
 14 import json
 13 import sys
 12 from pathlib import Path
 11
 10
  9 def clean_word_list(raw: str) -> list:
  8     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  7     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  6     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  5     # 去掉含中文的说明段
  4     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
  3     # 去掉孤立括号残留（如开头的 "("）
  2     raw = re.sub(r"\([^)]*\)", "", raw)
  1     raw = re.sub(r"[\(\)]", "", raw)
26      # 去掉词性标注，如 n. / adj. / vt. / vi.
  1     raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v)\.\s*', '', raw)
  2     # 去掉斜杠分隔符（词性列表用的）
  3     raw = raw.replace("/", ",").replace(".", " ").replace(";", " ")
  4
  5     words = []
 NORMAL  vocab_to_json.py                                                                        utf-8    python  12%   26:1
  2     # 去掉斜杠分隔符（词性列表用的）
 20 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE 部分。
 19
 18 使用方法:
 17     python vocab_to_json.py input.md output.json
 16
 15 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 14 """
 13
 12 import re
 11 import json
 10 import sys
  9 from pathlib import Path
  8
  7
  6 def clean_word_list(raw: str) -> list:
  5     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  4     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  3     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  2     # 去掉含中文的说明段
  1     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
23      # 去掉孤立括号残留（如开头的 "("）
 NORMAL  vocab_to_json.py                                                                                      utf-8    python  11%   23:1
 22 """
  3     raw = raw.replace("/", ",").replace(".", " ").replac@@@
 20 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE 部分。
 19
 18 使用方法:
 17     python vocab_to_json.py input.md output.json
 16
 15 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 14 """
 13
 12 import re
 11 import json
 10 import sys
  9 from pathlib import Path
  8
  7
  6 def clean_word_list(raw: str) -> list:
  5     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  4     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  3     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  2     # 去掉含中文的说明段
  1     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
23      # 去掉孤立括号残留（如开头的 "("）                                                                                      vocab_to_json.py                                                                              utf-8    py  23:1  
 NORMAL  vocab_to_json.py   utf-8    python  12%   26:1
 19
 18 使用方法:
 17     python vocab_to_json.py input.md output.json
 16
 15 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 14 """
 13
 12 import re
 11 import json
 10 import sys
  9 from pathlib import Path
  8
  7
  6 def clean_word_list(raw: str) -> list:
  5     """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
  4     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  3     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  2     # 去掉含中文的说明段
  1     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
23      # 去掉孤立括号残留（如开头的 "("）
 NORMAL  vocab_to_json.py                utf-8    python  11%   23:1
 21 vocab_to_json.py
 20 将 Markdown 词汇文档解析为结构化 JSON，自动跳过 NOTE 部 19
 18 使用方法:
 17     python vocab_to_json.py input.md output.json
 16
 15 如果不指定文件名，默认读取 vocab.md，输出 vocab.json
 14 """
 13
 12 import re
 11 import json
 10 import sys
  9 from pathlib import Path
  8
  7
  6 def clean_word_list(raw: str) -> list:
  5     """从原始文本中提取单词列表，去除中文说明、括号内容等。    """
  4     # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
  3     raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
  2     # 去掉含中文的说明段
  1     raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
23      # 去掉孤立括号残留（如开头的 "("）                              vocab_to_json.py   utf-8    python  11%   23:1  NORMAL 
分 NORMAL <_json.py  utf-8    python  12%   26:1
   共 1 个子分类
   共 757 个词条
longe@192 ~/d/d/datastr> nvim output5.json
longe@192 ~/d/d/datastr> nvim vocab_to_json.py
⏎
longe@192 ~/d/d/datastr> rm output5.json
longe@192 ~/d/d/datastr> python3 vocab_to_json.py "/Users/longe/Dropbox/Long E/Longe's Knowledge Base/Data_KB/八级_vocab_english.md" output5.json
读取: /Users/longe/Dropbox/Long E/Longe's Knowledge Base/Data_KB/八级_vocab_english.md
解析中...
完成！已写入: output5.json
   共 1 大部分
   共 1 个分类
   共 1 个子分类
   共 757 个词条
longe@192 ~/d/d/datastr> nvim output5.json
longe@192 ~/d/d/datastr> rm output5.json
longe@192 ~/d/d/datastr> ls
output1.json      output3.json      vocab_to_json.py
output2.json      output4.json
longe@192 ~/d/d/datastr> nvim vocab_to_json.py
longe@192 ~/d/d/datastr> git init
Initialized empty Git repository in /Users/longe/Desktop/demo/datastr/.git/
longe@192 ~/d/d/datastr (main)> ls -a
./                output1.json      output4.json
../               output2.json      vocab_to_json.py
.git/             output3.json
longe@192 ~/d/d/datastr (main)> touch README.md
longe@192 ~/d/d/datastr (main)> ls
output1.json      output3.json      README.md
output2.json      output4.json      vocab_to_json.py
longe@192 ~/d/d/datastr (main)> nvim output5.json
longe@192 ~/d/d/datastr (main)> ls
output1.json      output4.json      vocab_to_json.py
output2.json      output5.json
output3.json      README.md
longe@192 ~/d/d/datastr (main)> cd ..
longe@192 ~/d/demo> cd ..
longe@192 ~/desktop> cd ..
longe@192 ~> cd ..
longe@192 /Users> cd ~/desktop
longe@192 ~/desktop> ls
demo/
longe@192 ~/desktop> cd demo/
longe@192 ~/d/demo> ls
01.py
CN_EN_personal_language_trainer/
debug*
debug.c
debug.dSYM/
myfirstpro/
README.md
longe@192 ~/d/demo> cd CN_EN_personal_language_trainer/
longe@192 ~/d/d/CN_EN_personal_language_trainer> ls
datastr/
longe@192 ~/d/d/CN_EN_personal_language_trainer> ls -a
./       ../      datastr/
longe@192 ~/d/d/CN_EN_personal_language_trainer> cd datastr/
longe@192 ~/d/d/C/datastr (main)> ls -a
./                output2.json      README.md
../               output3.json      vocab_to_json.py
.git/             output4.json
output1.json      output5.json
longe@192 ~/d/d/C/datastr (main)> rm -rf .git
longe@192 ~/d/d/C/datastr> cd ..
longe@192 ~/d/d/CN_EN_personal_language_trainer> git init
Initialized empty Git repository in /Users/longe/Desktop/demo/CN_EN_personal_language_trainer/.git/
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> git add .
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> git commit -m "First initial"
[main (root-commit) e28e09e] First initial
 7 files changed, 28568 insertions(+)
 create mode 100644 datastr/README.md
 create mode 100644 datastr/output1.json
 create mode 100644 datastr/output2.json
 create mode 100644 datastr/output3.json
 create mode 100644 datastr/output4.json
 create mode 100644 datastr/output5.json
 create mode 100644 datastr/vocab_to_json.py
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> gh
? Type longe000id-star/CN_EN_personal_language_trainer to confirm deletion: longe000id-star/CN_EN_personal_language_trainer
✓ Deleted repository longe000id-star/CN_EN_personal_language_trainer
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> gh repo create longe000id-star/CN_EN_personal_language_trainer --public --source . --push
✓ Created repository longe000id-star/CN_EN_personal_language_trainer on github.com
  https://github.com/longe000id-star/CN_EN_personal_language_trainer
✓ Added remote https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 104.99 KiB | 8.75 MiB/s, done.
Total 10 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
 * [new branch]      HEAD -> main
branch 'main' set up to track 'origin/main'.
✓ Pushed commits to https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> cd datastr/
longe@192 ~/d/d/C/datastr (main)> ls
output1.json      output4.json      vocab_to_json.py
output2.json      output5.json
output3.json      README.md
longe@192 ~/d/d/C/datastr (main)> mv output1.json vocab_gaokao.json

longe@192 ~/d/d/C/datastr (main)> mv output5.json vocab_tem8.json
longe@192 ~/d/d/C/datastr (main)> mv output2.json vocab_cet46_1.json
                                  mv output3.json vocab_cet46_2.json
                                  mv output4.json vocab_cet46_3.json
longe@192 ~/d/d/C/datastr (main)> ls
README.md           vocab_gaokao.json
vocab_cet46_1.json  vocab_tem8.json
vocab_cet46_2.json  vocab_to_json.py
vocab_cet46_3.json
longe@192 ~/d/d/C/datastr (main)> git add .
longe@192 ~/d/d/C/datastr (main)> git commit . -m "rename"
[main 64e0dcb] rename
 5 files changed, 0 insertions(+), 0 deletions(-)
 rename datastr/{output2.json => vocab_cet46_1.json} (100%)
 rename datastr/{output3.json => vocab_cet46_2.json} (100%)
 rename datastr/{output4.json => vocab_cet46_3.json} (100%)
 rename datastr/{output1.json => vocab_gaokao.json} (100%)
 rename datastr/{output5.json => vocab_tem8.json} (100%)
longe@192 ~/d/d/C/datastr (main)> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#       renamed:    vocab_to_json.py -> md_to_json.py
#
~
~
~
~
~
~
~
~
~
~
~
~
<anguage_trainer/.git/COMMIT_EDITMSG" 10L, 282B
rename
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 310 bytes | 310.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
   e28e09e..64e0dcb  main -> main
longe@192 ~/d/d/C/datastr (main)> ls
README.md           vocab_gaokao.json
vocab_cet46_1.json  vocab_tem8.json
vocab_cet46_2.json  vocab_to_json.py
vocab_cet46_3.json
longe@192 ~/d/d/C/datastr (main)> mv vocab_to_json.py md_to_json.py
longe@192 ~/d/d/C/datastr (main)> ls
md_to_json.py       vocab_cet46_3.json
README.md           vocab_gaokao.json

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#       modified:   md_to_json.py
#
~
~
~
~
~
~
~
~
~
~
~
~
<anguage_trainer/.git/COMMIT_EDITMSG" 10L, 262B c
Change
vocab_cet46_1.json  vocab_tem8.json
vocab_cet46_2.json
longe@192 ~/d/d/C/datastr (main)> git add .
longe@192 ~/d/d/C/datastr (main)> git commit .
[main d7e8669] rename
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename datastr/{vocab_to_json.py => md_to_json.py} (100%)
longe@192 ~/d/d/C/datastr (main)> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 302 bytes | 302.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
   64e0dcb..d7e8669  main -> main
longe@192 ~/d/d/C/datastr (main)> nvim md_to_json.py
longe@192 ~/d/d/C/datastr (main)> git add md_to_json.py
longe@192 ~/d/d/C/datastr (main)> git commit md_to_json.py
[main cef8c7a] Change
 1 file changed, 1 insertion(+), 1 deletion(-)
longe@192 ~/d/d/C/datastr (main)> git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 337 bytes | 337.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
   d7e8669..cef8c7a  main -> main
longe@192 ~/d/d/C/datastr (main)> rm README.md
longe@192 ~/d/d/C/datastr (main)> git push
Everything up-to-date
longe@192 ~/d/d/C/datastr (main)> git add .
longe@192 ~/d/d/C/datastr (main)> git commit . -m "delete README.md"
[main dca459b] delete README.md
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 datastr/README.md
longe@192 ~/d/d/C/datastr (main)> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 273 bytes | 273.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/longe000id-star/CN_EN_personal_language_trainer.git
   cef8c7a..dca459b  main -> main
longe@192 ~/d/d/C/datastr (main)> cd ..
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> touch README.md
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> nvim README.md
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> git add README.md
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> git commit README.md -m "Add README.md"
[main e731a4d] Add README.md
 1 file changed, 23 insertions(+)
 create mode 100644 README.md
longe@192 ~/d/d/CN_EN_personal_language_trainer (main)> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 761 bytes | 761.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/longe000id-star/CN_EN_personal_langua 12 # Personal Language Learning Assistant
 11
 10 ## Overview
  9
  8 This is a private language learning assistant built for     my own use.
  7
  6 It is designed to create a structured and disciplined l    earning system that guides regular study, generates act    ive practice, evaluates performance, and tracks long-te    rm progress.
  5
  4 All training and testing are generated strictly from se    lected source materials. The system focuses on controll    ed input and deep reinforcement rather than random cont    ent.
  3
  2 ## Key Features
  1
13  - Systematic study scheduling
  1 - Material-based training (listening, speaking, reading    , writing)
  2 - Automatic test generation
 NORMAL   main <md  utf-8    markdown  56%   13:23

