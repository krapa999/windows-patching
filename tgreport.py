def writetofile(items,Name,csv_file,list, owner):
    for item in items:
        values = []
        avail_tags = []
        avail_values = []
        print "File writing for %s - %s" %(Name,item.id)
        resource = Name
        icontent = ''
        ivalues = ''
        icontent += owner + ',' + resource + ','+ str(item.id) +','
        csv_file.write(icontent)
        csv_file.flush()
        values = item.tags
        if values != None:
            for tag in values:
                if tag['Key'] in list:
                    if tag['Value'] != '':
                        avail_tags.append(tag['Key'])
                        avail_values.append(tag['Value'])

            a = 0
            for i in list:
                if i in avail_tags:
                    ind = avail_tags.index(i)
                    ab = avail_values[ind] +','
                    ivalues += ab
                    a += 1
                else:
                    ab = '     ,'
                    ivalues += ab
            csv_file.write(ivalues + '\n')
            csv_file.flush()
        else:
            for i in list:
                ab = '    ,'
                ivalues += ab

            csv_file.write(ivalues + '\n')
            csv_file.flush()

    #csv_file.write('\n')
    csv_file.flush()
