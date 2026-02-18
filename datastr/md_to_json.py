"""
vocab_to_json.py
将 Markdown 词汇Obsidian文档解析为结构化 JSON，自动跳过 NOTE 部分。

使用方法:
    python vocab_to_json.py input.md output.json

如果不指定文件名，默认读取 vocab.md，输出 vocab.json
"""

import re
import json
import sys
from pathlib import Path


def clean_word_list(raw: str) -> list:
    """从原始文本中提取单词列表，去除中文说明、括号内容等。"""
    # 去掉 (xxx): 格式的说明前缀（含中文或括号开头的标签）
    raw = re.sub(r"\([^)]*\)\s*[:：]\s*", " ", raw)
    # 去掉含中文的说明段
    raw = re.sub(r"[^\x00-\x7F]+.*?[:：]\s*", " ", raw)
    # 去掉孤立括号残留（如开头的 "("）
    raw = re.sub(r"\([^)]*\)", "", raw)
    raw = re.sub(r"[\(\)]", "", raw)
    # 去掉词性标注，如 n. / adj. / vt. / vi.
    raw = re.sub(r'\b(n|adj|vt|vi|adv|prep|conj|pron|v)\.\s*', '', raw)
    # 去掉斜杠分隔符（词性列表用的）
    raw = raw.replace("/", ",").replace(".", " ").replace(";", " ")   

    words = []
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        # 斜杠同义词: mom/mum → [mom, mum]
        if "/" in token:
            parts = [p.strip() for p in token.split("/")]
            words.extend(p for p in parts if p)
        else:
            words.append(token)

    # 去重，保持顺序，只保留含英文字母的词
    seen = set()
    result = []
    for w in words:
        w = w.strip()
        if not w:
            continue
        w_lower = w.lower()
        if w_lower not in seen and re.search(r"[a-zA-Z]", w):
            seen.add(w_lower)
            result.append(w)
    return result


def remove_notes(text: str) -> str:
    """去掉所有 Obsidian NOTE callout 块。"""
    text = re.sub(
        r"^[ \t]*> \[!NOTE\].*?(?=\n[ \t]*(?!>)|\Z)",
        "",
        text,
        flags=re.DOTALL | re.MULTILINE,
    )
    text = re.sub(r"^[ \t]*>.*$", "", text, flags=re.MULTILINE)
    return text


def parse_markdown(text: str) -> dict:
    text = remove_notes(text)
    lines = text.splitlines()

    result = {"parts": []}
    current_part = None
    current_section = None

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # 大部分: ### 第X部分
        if re.match(r"^#{1,3}\s+\*{0,2}第[一二三四五六七八九十百]+部分", line):
            title = re.sub(r"^#+\s+\d+[\.\、．]?\s*\d*\.?\s*", "", line).strip()
            current_part = {"title": title, "sections": []}
            result["parts"].append(current_part)
            current_section = None

        # 分类: #### 1. xxx
        elif re.match(r"^#{2,5}\s+\d+[\.\、．]\s*", line) or re.match(r"^#{2,5}\s+\d+\.\s+[A-Z]", line):
            title = re.sub(r"^#+\s+\d+[\.\、．]\s*", "", line).strip()
            if current_part is None:
                current_part = {"title": "General", "sections": []}
                result["parts"].append(current_part)
            current_section = {"title": title, "subcategories": []}
            current_part["sections"].append(current_section)
            while i + 1 < len(lines) and lines[i+1].strip() and \
                  not re.match(r"^[-#]", lines[i+1].strip()):
                i += 1

        # 子分类: - **标题:** (冒号在 bold 内)
        elif re.match(r"^-\s+\*\*", line) or re.match(r"^\*\*[^*]+:\*\*\s*$", line):
            m = re.search(r"\*\*([^*:]+):?\*\*", line)
            title = m.group(1).strip() if m else "Unknown"
            # 收集词汇行
            words_raw = ""
            # 如果是纯标题行（**xxx:**），after 为空，不收集
            after = re.sub(r"^\*\*[^*]+:\*\*\s*$", "", line).strip()
            if not after:
                after = re.sub(r"^-\s+\*\*[^*]*\*\*\s*[:：]?\s*", "", line).strip()
            if after and re.search(r"[a-zA-Z]{2,}", after):
                words_raw += after + ","

            j = i + 1
            while j < len(lines):
                nl = lines[j]
                s = nl.strip()
                if re.match(r"^#{1,6}\s", s) or re.match(r"^-\s+\*\*", s):
                    break
                if s == "":
                    k = j + 1
                    while k < len(lines) and lines[k].strip() == "":
                        k += 1
                    if k < len(lines):
                        peek = lines[k].strip()
                        if re.match(r"^#{1,6}\s", peek) or re.match(r"^-\s+\*\*", peek):
                            j = k
                            break
                    j += 1
                    continue
                words_raw += s + ","
                j += 1
            i = j - 1

            words = clean_word_list(words_raw)

            if current_section is None:
                if current_part is None:
                    current_part = {"title": "General", "sections": []}
                    result["parts"].append(current_part)
                current_section = {"title": "General", "subcategories": []}
                current_part["sections"].append(current_section)

            current_section["subcategories"].append({
                "title": title,
                "words": words,
                "count": len(words),
            })

        i += 1

    # 统计词数
    total = 0
    for part in result["parts"]:
        part_total = 0
        for section in part.get("sections", []):
            section_total = sum(sub["count"] for sub in section.get("subcategories", []))
            section["word_count"] = section_total
            part_total += section_total
        part["word_count"] = part_total
        total += part_total
    result["total_words"] = total
    result["metadata"] = {
        "description": "English vocabulary organized by topic and function",
        "source": "Markdown vocabulary document",
    }
    return result


def main():
    if len(sys.argv) >= 2:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path("vocab.md")

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix(".json")

    if not input_path.exists():
        print(f"找不到文件: {input_path}")
        print("用法: python vocab_to_json.py input.md [output.json]")
        sys.exit(1)

    print(f"读取: {input_path}")
    text = input_path.read_text(encoding="utf-8")
    print("解析中...")
    data = parse_markdown(text)

    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    total_sections = sum(len(p["sections"]) for p in data["parts"])
    total_subs = sum(
        len(s["subcategories"])
        for p in data["parts"]
        for s in p["sections"]
    )
    print(f"完成！已写入: {output_path}")
    print(f"   共 {len(data['parts'])} 大部分")
    print(f"   共 {total_sections} 个分类")
    print(f"   共 {total_subs} 个子分类")
    print(f"   共 {data['total_words']} 个词条")


if __name__ == "__main__":
    main()
