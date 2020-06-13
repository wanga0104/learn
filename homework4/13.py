title = ["序号","姓名","班级","语文","数学","英语","理综"]
marks = [['001','宋永欣 ',2,125,132,128,256],
         ['002','朱力璇 ',2,132,123,135,232],
         ['003','杜媛  ',1,132,141,132,263],
         ['004','马上宁 ',1,123,122,140,238],
         ['005','粟怡  ',1,134,138,135,263],
         ['006','贾患英',3,111,126,122,243],
         ['007','朱雅宁',4,128,135,141,278],
         ['008','扬研  ',5,123,122,132,213]]
def sort(course):
    print(f'按照{course}成绩排序（降序）')
    print('  '.join(title))
    marks.sort(key=lambda i:i[title.index(f'{course}')],reverse=True)
    for itrm in  marks:
        marks_str=[str(i) for i in itrm]
        print('  '.join(marks_str))

title.append('总成绩')
for i in marks:
    num=i[-1]+i[-2]+i[-3]+i[-4]
    i.append(num)
sort('语文')
sort('数学')
sort('总成绩')