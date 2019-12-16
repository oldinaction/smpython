# -*- coding: utf-8 -*-

import xlrd


class SmExcel:
    """Excel读取"""

    def open_excel(self, file='file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception, e:
            print str(e)

    # 读取一行
    def excel_row_byindex(self, file='file.xls', by_index=0, colnameindex=0):
        data = self.open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        while (colnameindex < nrows):
            # 某一行数据
            colnames = table.row_values(colnameindex)
            yield colnames
            colnameindex = colnameindex + 1

    # 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_index：表的索引
    def excel_table_byindex(self, file='file.xls', colnameindex=0, by_index=0):
        data = self.open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list = []
        for rownum in range(1, nrows):

            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list

    # 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
    def excel_table_byname(self, file='file.xls', colnameindex=0, by_name=u'Sheet1'):
        data = self.open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list

    def main(self):
        f = self.excel_row_byindex()
        for i in range(12):
            try:
                print f.next()
            except StopIteration, e:
                print e

        tables = self.excel_table_byindex()
        for row in tables:
            print row

        '''
        tables = excel_table_byname()
        for row in tables:
            print row
        '''


if __name__ == "__main__":
    smexcel = SmExcel()
    smexcel.main()
