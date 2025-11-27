import os
import json
import re

# PDF 文件所在目录
DIR = ".\deepchat"

# 输出文件
OUTPUT = "pdf_list.js"

def parse_pdf_name(filename):
    """
    解析 PDF 文件名：
    20251114-标题-标签1,标签2.pdf
    """
    name = filename[:-4]  # 去掉 .pdf
    parts = name.split("-")

    if len(parts) < 3:
        print(f"⚠ 文件名格式不正确，跳过：{filename}")
        return None

    date = parts[0]
    title = parts[1]
    tag_str = "-".join(parts[2:])  # 防止标题含有 '-'

    tags = tag_str.split(",")

    return {
        "date": date,
        "title": title,
        "tags": tags,
        "pdf": f"deepchat/{filename}"
    }

def main():
    files = os.listdir(DIR)
    pdfs = [f for f in files if f.lower().endswith(".pdf")]

    data = []

    for f in pdfs:
        parsed = parse_pdf_name(f)
        if parsed:
            data.append(parsed)

    # 按日期降序排列
    data.sort(key=lambda x: x["date"], reverse=True)

    # 转换为 HTML 所需的数组格式
    js_array = "let allData = " + json.dumps(data, ensure_ascii=False, indent=2) + ";"

    # 写出文件
    with open(OUTPUT, "w", encoding="utf-8") as fw:
        fw.write(js_array)

    print(f"✅ 生成成功！共解析 {len(data)} 个 PDF")
    print(f"👉 输出文件：{OUTPUT}")

if __name__ == "__main__":
    main()
