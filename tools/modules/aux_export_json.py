def export_json(dataframe,filex):
    
    header = list(dataframe.columns.values)
    N_data = len(dataframe)
    
    print('[',file=filex)
    for i in range(N_data):
        print('\t{',file=filex)
        for campo in header:
            value = dataframe[campo].to_list()
            if(campo==header[-1]):
                print('\t\t"{}": "{}"'.format(campo,value[i]),file=filex)
            else:
                print('\t\t"{}": "{}",'.format(campo,value[i]),file=filex)
        if(i==N_data-1):
            print('\t}',file=filex)
        else:
            print('\t},',file=filex)
    print(']',file=filex)