# def get_distinct_education_level(request):
#     data = Education.objects.values('education_level').annotate(distinct=Count('user_id', distinct=True))
#     l1 = data[0]['education_level']
#     l2 = data[1]['education_level']
#     l3 = data[2]['education_level']
#     l4 = data[3]['education_level']
#     d1 = data[0]['distinct']
#     d2 = data[1]['distinct']
#     d3 = data[2]['distinct']
#     d4 = data[3]['distinct']
#     return render(request, 'main.html', {'a': l1, 'b': l2, 'c': l3, 'd': l4, 'e': d1, 'f': d2, 'g': d3, 'h': d4})



# def get_org_name(request):
#     org_names = Education.objects.values_list('org_name').distinct()
#     return render(request, 'raw.html', {'org_names': org_names})