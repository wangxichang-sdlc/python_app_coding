# 实用Python编程技术（基础篇）
# practical_python_coding -- Foundation and Files Operation

#### 介绍
本书致力于为编程入门提供一个实用教程，内容包括创建计算环境、IDE使用、基本编程知识、各种数据文件的读写。

此处提供该书的各章代码，特别是读写DBF文件的源代码（该代码库拟提交PyPI，在此进行维护）。

#### 章节目录
第一部分 创建计算环境

1. 基本环境配置

安装Python运行环境是使用Python的开端，安装前需要熟悉本地机器操作系统有关信息，登录Python网站后，
可以根据系统提示下载目前适合本地安装的Python版本，也可以找到全部可下载版本列表，选择指定的版本下载。
下载过程中，如果使用用户定制方式，可以对很多配置项目选择配置，这时，需要了解各个配置项的含义及作用，根据需要进行配置。
随Python语言包安装的手册，是Python的重要文档，内容包括各个版本更新情况、Python使用指南、语言参考、标准库等，
是学习和掌握Python的最重要的参考资料。

2. Anaconda环境配置

Anaconda是一个Python集成环境发行包，使用Anaconda可以避免很多第三方包的安装配置，由于很多第三方包相互之间具有依赖关系，
使用Anaconda可以避免这些依赖关系产生的安装问题。同时，Anaconda提供了自身的环境管理工具conda，conda在某些方面功能比pip更加强大。
Anaconda的目标是支持数据科学应用，为数据科学研究开发提供预装的各种工具，但是Anaconda发行包比较笨重，很多安装包可能用户永远都不会使用，
而pip对依赖关系的处理越来越成熟，pip安装速度也已经变得非常快速，对于是否使用Anaconda，可以根据需要选择。

3. IPython环境配置

IPython是交互式Python（Interactive Python）的简称，是一个致力于提供Python解释器增强功能的项目，
其主体部分是支持增强Python命令的内核引擎和命令行解释器。通过内核引擎可以支持Jupyter浏览器代码编辑界面，
而命令行解释器既可以独立运行，也可以在各种编辑器中实现运行。

使用Python的理由之一是，可以很容易地编写实现一些计算任务的脚本。很多计算问题的核心只是片段的代码，
书写脚本成为十分频繁的重头工作。编写这些计算问题的核心代码脚本，并直接进行测试，也被称为探索性计算。
探索性计算不仅是科学计算的需要，在数据时代，也大量存在于各类普通业务工作中，
而IPython使这种探索性计算变得更加顺畅和动感，几乎任何使用Python的用户都会用到IPython。


4. 使用集成开发环境PyCharm

PyCharm 是一个为Python语言编程专门开发的跨平台集成开发环境，具备了现代先进编程环境的各种功能，
可以提供在Windows、macOS和Linux上的一致性体验。目前PyCharm提供了三个版本：
专业版（Professional）、社区版（Cummunity）、教育版（Edu）。
教育版和社区版是开源免费的，功能受到一些限制，但提供的各类编程体验和项目组织功能已经十分强大。
教育版提供了有关培训课程，支持在PyCharm中学习Python编程。


第二部分 编程技术基础

5. 数据类型

类型用于定义数据的结构，规定数据对象的行为。在Python中，所有存在的实体都是对象，都有其类型。
为了表示各种类型，Python构建了一个层次类型体系，最原始的类型是type和object，
最常用的类型是6种内置类型：数字、字符串(str)、列表(list)、元组(tuple)、字典(dict)、集合(set)。
数字类型是各种具体的数字类型的总称，具体类型包括布尔（bool）、整数(int)、实数(float)、复数(complex)等。

6. 程序结构

相比大多数语言，Python的流程控制语句比较精简，力图使编程方式更为清晰可读。值得称赞的是，
Python引入了一些广受欢迎的流程结构，
如列表推导式，很多复杂计算过程可以变为“一行代码”，实现了功能强大和语法简单的优美结合。

在Python的流程控制语句中，也出现了一些特别的东西，主要是在循环语句中配置了else。很多编程人员，
尤其是从其它没有该特性语句编程语言专来的技术人员，不太习惯使用并忽视这个特性。
其实，如果了解并掌握了这些特性，会强化处理流程的方式。《流程的Python》作者就认为，
“在有些语句中使用else子句，通常能让代码更容易阅读，而且能省去一些麻烦，...”

7. 编写程序

Python语言作为备受推崇的科学计算语言，在实现计算问题编程方面易学易用，从编写计算代码开始，学习体验Python编程，
或许是一个较好的选择。本章通过使用Python实现计算公式，应用计算公式解决问题，通过实现实用的公式计算，
从中掌握需要使用的一些语言概念和语法，以此来进入编写程序的开端。Python的语法非常简练，
编写代码和测试运行都十分简单，但为了有益于开发实践，在编写和测试代码，应尽量实用集成环境，
通过简单的认为，使对集成开发环境和测试工具的掌握不断深入。


第三部分 读写文件数据

8. 使用os模块进行目录文件操作

Python语言作为备受推崇的科学计算语言，在实现计算问题编程方面易学易用，从编写计算代码开始，
学习体验Python编程，或许是一个较好的选择。本章通过使用Python实现计算公式，应用计算公式解决问题，
通过实现实用的公式计算，从中掌握需要使用的一些语言概念和语法，以此来进入编写程序的开端。
Python的语法非常简练，编写代码和测试运行都十分简单，但为了有益于开发实践，在编写和测试代码，
应尽量实用集成环境，通过简单的认为，使对集成开发环境和测试工具的掌握不断深入。

9. 使用open函数读写文件

Python提供了一些内置函数用于读写文件数据，最常用的是open函数。使用open函数可以创建文件对象，
然后调用文件对象提供的方法，读写文件中的数据。对文件的读写操作，涉及到文件格式、读写方式及字符编码等概念。

根据存储格式和读写方式，可以将文件分为三个类型：
（1）文本文件
将文件视为以字符方式存放的格式。写入文件时指定字符编码，读出文件时需要遵循存储的字符编码。
读写可以按照行的方式进行，每行定义结束符，以便读写文件时进行识别。
在Windows系统中是'\r\n'，Linux系统中只有'\n'。Python源码文件都是以文本文件方式存储。

（2）特殊格式文件
一些专业系统会使用专门的数据存储格式，如xlsx(Excel)、docx(Word)、PDF(Adobe)、Html、XML、HDF5等，
这些数据文件一般使用相应的系统或工具读写。在Python中，有很多第三方库，用于读写专业格式文件，如pandas可以读写Excel、CSV、HDF5文件等，还有一些专用于读写Excel文件的扩展包，如xlrd、xlwt及openpyxl。Python标准库中提供了用于读写CSV文件的模块csv。

（3）二进制文件
各种文件都以字节方式存储，每个字节都是八位的二进制数值。如果不知道文件的具体格式内容，
可以将其视为若干个字节，以字节流的方式读写。这种方式，被称为二进制文件读写方式。
当需要使用字节方式处理文件时，如压缩、解压、计算长度等，可以使用二进制方式操作。

10. 使用Numpy读写文件

Numpy是一个Python第三方库，主要提供数值计算功能（Numerical Python），是Python数据计算最重要的支撑平台。
在Numpy中，通过同类型多维数组，实现了多维数据的高效计算，针对数组运算配置了大量的数学函数库，
使其成为数据处理的强力引擎。Numpy是很多功能强大的工具包的基础依赖库，
数据分析平台Pandas、科学计算库Scipy、绘图库Matplotlib、机器学习库sklearn等，
都是基于Numpy实现的。可以说，没有Numpy就没有Python环境的科学计算。

本章主要介绍Numpy的读写数据文件功能，描述数据类型和一些基本的数据操作方法。
将Numpy的数据计算和文件读写结合起来，就使数据处理和数据存储连接起来，
从而为建立更高级的数据处理过程奠定基础。如希望深度掌握数学问题求解，
使用Numpy进行大规模高效计算，需要更为深入地研究Numpy。若进行应用数据管理和统计计算，
可先了解Numpy的多维数组运算和基本功能使用，再使用Pandas的数据分析处理功能。
Pandas提供了索引序列和数据框两种高级类型，具有类似关系数据库表的操作方式，
支持类似SQL语言的数据操作，更适合用于业务数据管理。

11. 使用Pandas读写文件

Pandas的名称含义是数据分析库（Python Data Analysis Library），
是多维数组、数据表、数据统计、数据可视化的集成服务平台。在计算处理方式上，
Pandas充分使用向量化计算和内存映射的方式，数据处理的效率非常高。
由于具有优化设计的数据类型、高计算效率和向量方式操作等优势，
很多大规模数据处理和计算任务都可以使用Pandas完成，很多软件平台也都支持使用Pandas数据结构。
针对各种流行的专业格式数据文件，Pandas提供了实现读写这些特殊格式数据文件的方法，
可以直接读取后转换为数据集DataFrame，同时也支持对一些专业大数据管理库Hdf5等平台的操作。

12. 使用python-docx读写Word文件

使用Python读写Word文件，可以尝试使用第三方库pthon-docx，安装后的模块名称是docx，
所以也称为docx。docx用于解析读写Word文件，该项目已经发布到PyPI平台，
可以很方便地进行安装。docx的直接依赖模块是lxml，lxml是用于解析XML等结构数据的模块，
使用pip安装时，可以自动对依赖库进行安装和更新。

13. 读写数据库数据

在信息管理系统中，一般都会使用关系数据库保存数据，如Oracle、MySQL、SQLite等。
几乎所有数据库都提供了Python访问方式，也有很多第三方开发的专业性模块，
用于连接数据库。尽管各种数据库之间的连接与数据操作方式有一定差异，
为了避免给编程造成复杂性,Python制订了访问数据库的统一标准（DB-API），
目前各种连接数据库的模块也基本都遵守这个标准，使编程过程变得较为容易。在数据库读写过程中，
有关数据在Python环境和数据库之间进行传递，一般情况下两个环境之间的数据类型会具有较大的差异性，
系统会根据类型推断进行数据类型转换，在数据管理中，需认真考虑这些类型之间的对应转换情况，
防止数据内容的非正常改变和信息丢失。

14. 读写PDF文件数据

PDF是Adobe公司设计的一种电子文档格式文件，其含义是Portable Document Format，即“便携式文档格式”。
开始时，PDF用于Adobe Systems与应用程序、操作系统、硬件平台无关的方式进行文件交换，
由于PDF文件的优秀特性，各种文字编辑软件都支持生成PDF文件，成为非常流行的文件格式。
PDF是一种只读的文件存储方式，当存在大量的PDF文件，需要从中进行提取数据时，就需要对文件进行解析。
在Python生态系统中，提供了多种PDF文件读写工具，包括Pdfplumber、PyPDF2、Reportlab、Pdfminer3K及Camelot等，
可以根据用途进行选择。

15. 读写DBF文件数据

本章作为一个应用实例，从剖析DBF文件格式和数据类型开始，实现一个完全Python代码的DBF文件到pandas数据集的
数据交换读写模块。读写DBF文件数据是一个较为复杂的过程，需要对DBF文件格式进行深入的分析，
建立pandas、DataFrame和DBF之间的数据类型转换。
读写DBF文件可以作为Python数据类型、数据文件读写的一个较为高级的实践，
有助于掌握更多Python的基础知识和编程技能，在有一定基础后也可以考虑对该模块进行改进和重构。

读取DBF文件需要做几个方面的工作：
（1）使用二进制方式打开文件读取数据，以便逐字节处理数据。在Python中需要使用open(filename,'rb')方式打开文件。
（2）根据文件格式定义，对文件中二进制数据进行分离处理。特定格式文件一般会包含文件结构描述、数据类型描述和数据部分，
需要具体定位每个描述区域并提取结构数据，用于进一步解析数据。
（3）针对每个定义区域的数据，按照内容格式使用相应解码方式解析出对应的数据类型值。将二进制数据解析为Python数据对象，
可以使用字符解码（decode）或类型解析（struct.unpack）。
文件包含数据量很多时，需要有效处理数据溢出和读取效率问题。读出数据需要考虑文件内容是否会超出内存容量，
即使小于内存容量，有时也会因数据量过大使系统运行速度降低甚至反应迟缓。可以考虑每次按照要求读出少量记录，
也可以考虑使用内存映射方式写入临时文件。

16. 读写HDF5文件数据

HDF5（Hierarchical Data Format，version 5）是一个完全开源和广泛使用的数据存储管理平台，
由伊利诺伊大学厄巴纳-香槟分校 UIUC (University of Illinois at Urbana-Champaign) 开发，
非常适合用于大数据存储、处理和归档交换，已被NASA的很多项目采用，也是著名科学计算平台Matlab的标准存储格式。
在HDF5中，数据以组（group）的方式形成层次结构进行组织，类似于操作系统中的目录结构，
数据则使用数据集（dataset）进行存储，类似于Numpy中多维向量。HDF5是HDF数据平台的最新版本，
改进了前期版本数据文件规模限制、数据结构复杂等缺陷，也保持了与仍然较为流行老版本HDF4的一定兼容性。
但是，从数据管理发展的角度，如果没有遗留的数据和程序资源，就不需要再使用HDF4了。

HDF5不仅是一种数据存储结构，也是一个专业化数据管理平台，使用HDF5可以提供高性能数据读写、数据自描述、
内存映射访问、多线程安全并发访问、超大规模数据存储、跨平台数据交换等特性。
HDF5的单个文件可以达到EB级别（百万TB），对存储规模几乎没有限制。在数据内容不断丰富和规模指数增长的数据处理时代，
这些特性为大数据管理、高效计算、归档迁移等重量级数据工程提供了有力的支撑，很多领域和著名工程应用都在推行使用HDF5。

目前，有两种针对Python的HDF5数据处理接口，即H5py和Pytables。H5py基于Numpy数据类型建立与HDF5的数据处理，
将Numpy多维数组无缝对接到HDF5的数据集，在科学计算项目中应用比较广泛。Pytables支持将异构的多维数据存储到HDF5，
提供pandas数据集到HDF5的直接读写，对大数据处理工作更为适宜。本章对这两个模块的使用进行初步介绍，
如果开展更深入的应用，可以参考有关官方文档（https://www.hdfgroup.org/solutions/hdf5）。
