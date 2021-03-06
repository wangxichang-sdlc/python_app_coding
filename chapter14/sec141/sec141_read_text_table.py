# coding = utf8

import pdfplumber


def read_pdf_texts_tables(pdfname, password=None):
    """
    使用Pdfplumber读取PDF文件文本和表格数据

    >>> texts, tables = read_pdf_texts_tables('../demo.pdf')
    >>> print(len(texts))				# 只有一组文本（文档为单页）
    1
    >>> print(texts[0])
    高一三班成绩表
    学号 姓名 语文 数学 外语 物理 化学 地理 总分
    210101 梁玉英 88 89 90 91 92 93 543
    210102 陈平 76 74 76 76 76 76 454
    210103 张凤英 84 83 84 84 84 84 503
    210104 王畅 39 59 39 39 39 39 254
    210105 朱斌 98 88 98 98 98 98 578
    210106 杨红梅 68 85 68 68 68 68 425
    210107 陈柳 87 87 87 87 87 87 522
    210108 张倩 56 53 56 56 56 56 333
    >>> print(len(tables))				# 本文档中只有一个表格
    1

    # 查看表格的数据
    >>> for line in tables[0][0]:print(line)
    ['学号', '姓名', '语文', '数学', '外语', '物理', '化学', '地理', '总分']
    ['210101', '梁玉英', '88', '89', '90', '91', '92', '93', '543']
    ['210102', '陈平', '76', '74', '76', '76', '76', '76', '454']
    ['210103', '张凤英', '84', '83', '84', '84', '84', '84', '503']
    ['210104', '王畅', '39', '59', '39', '39', '39', '39', '254']
    ['210105', '朱斌', '98', '88', '98', '98', '98', '98', '578']
    ['210106', '杨红梅', '68', '85', '68', '68', '68', '68', '425']
    ['210107', '陈柳', '87', '87', '87', '87', '87', '87', '522']
    ['210108', '张倩', '56', '53', '56', '56', '56', '56', '333']
    """
    # 打开文档，读取文本和表格数据，如有密码使用password
    texts, tables = [], []
    with pdfplumber.open(pdfname, password=password) as pdf:
        # 遍历文档各页
        for page in pdf.pages:
            texts.append(page.extract_text())                   # 提取该页的文本
            tables.append(page.extract_tables())	            # 提取该页的表格
    # 返回各页的文本，表格
    return texts, tables
