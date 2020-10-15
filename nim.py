import xlsxwriter


def nim(target, n1, add, multiply):
    mobile = 1
    results = [[0] * 2 * target for i in range(2 * target)]
    for x in range(target - 1, 0, -1):
        for y in range(target - x - 1, 0, -1):
            nextCodes = [results[x + add][y], results[multiply * x][y],
                         results[x][y + add], results[x][multiply * y]]
            negative = [c for c in nextCodes if c <= 0]
            if negative:
                results[x][y] = -max(negative) + 1
            else:
                results[x][y] = -max(nextCodes)

    # DEBUG Answer output
    """
    print('\t' + ' '.join(list(map(lambda x: str(x).rjust(4, ' '), range(1, target - 1)))))
    
    print('\n'.join(str(index + 1) + '\t' + ' '.join(list(map(
        lambda x: ('В' + str(x)).rjust(4, ' ') if x > 0 else ('П' + str(x)).replace('-', '').rjust(4,
                                                                                                   ' '),
        i[1:target - 1]))) for index, i in enumerate(results[1:target - 1])))
    """

    # Excel Answer output
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Nim.xlsx')
    worksheet = workbook.add_worksheet()

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1})

    worksheet.write(0, 0, '', header_format)
    for index, i in enumerate(results[1:target - n1]):
        if mobile:
            worksheet.write(0, index + 1, index + 1, header_format)
        for jndex, j in enumerate(i[1:target - n1]):
            if mobile:
                worksheet.write(jndex + 1, 0, jndex + 1, header_format)
            if j > 0:
                worksheet.write(index + mobile, jndex + 1, 'B' + str(j))
            else:
                worksheet.write(index + mobile, jndex + 1, ('П' + str(j)).replace('-', ''))

    workbook.close()
