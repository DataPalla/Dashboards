"""

# Using Cursor and SQL query to get specific data ( This will cause lag which loading the web page

cursor = connection.cursor()
cursor.execute("select count( distinct user_id) as User_Count from Education group by Education_Level ")
r = cursor.fetchall()

# Using Python models and objects to get the dats
def bar(request):
    b = Education.objects.values('education_level').distinct()
    print(b[1])
    print(b.query)
    print(connection.queries)
    return render(request, 'bar.html', {'b': b[3]})


# Gets Distinct Education_level
def raw(request):
    categories = Education.objects.values_list('education_level').distinct()
    data = Education.objects.values('education_level').annotate(distinct=Count('user_id', distinct=True))
    l1 = categories[3][0]
    l2 = categories[2][0]
    l3 = categories[0][0]
    l4 = categories[1][0]
return render(request, 'raw.html', {'x': data, 'y': categories})

#get single value from field

def bar(request):
    b = Education.objects.values('education_level').distinct()
    print(b[1])
    print(b.query)
    print(connection.queries)
    return render(request, 'bar.html', {'b': b[3]})
"""