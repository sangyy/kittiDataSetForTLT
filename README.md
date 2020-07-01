# kittiDataSetForTLT
labelImg voc xml to kitti tlt_dataset
# rawDataset(处理前的数据)
# kittiDataset(按照这个目录结构整理labelImg的文件存储结构)
# "xml2kitti"文件夹保存的是转换VOC的.xml文件到KITT格式的工具

# changename.py是用来统计缀名的工具并检查是否缺少标签

# check.py是用来检查图片是否有损坏的工具（比如某个作者之前遇到的错误是某个图片以‘BM’开头，系统会报告格式错误）