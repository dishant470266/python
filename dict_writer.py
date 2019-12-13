from csv import DictWriter
with open('final.csv','w') as f:
    csv_writer = DictWriter(f,fieldnames = ['first_name','last_name','age'])
    csv_writer.writerow({
        'first_name' : 'sffssd',
        'last_name' : 'dfgh',
        'age' : 500

    })