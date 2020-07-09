from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.marketing, name='marketing'),
    url(r'^ML$', views.marketing, name='marketing'),
    url(r'^dashboard', views.index, name='index'),
    url(r'^library', views.library, name='library'),
    url(r'^neuromine', views.neuromine, name='neuromine'),
    url(r'^config', views.config, name='config'),
    url(r'^Search/$', views.index, name='search'),
    url(r'^Search/([\w-]+)/$', views.index_code, name='search_code'),
    url(r'^codelist', views.codelist),
    url(r'^datasets/$', views.DatasetList.as_view(), name='dataset_list'),
    url(r'^codes/$', views.CodesList.as_view(), name='codes_list'),
    url(r'^N1/$', views.DatasetList.as_view(), name='dataset_list'),
    url(r'^N2/$', views.DatasetList.as_view(), name='dataset_list'),
    url(r'^N3/$', views.DatasetList.as_view(), name='dataset_list'),
    url(r'^N4/$', views.DatasetList.as_view(), name='dataset_list'),
    url(r'^datasets/(?P<pk>\d+)/$', views.DatasetDetail.as_view(), name='dataset_detail'),
    url(r'^codes/([\w-]+)/$', views.CodesByDatasetList.as_view()),
    url(r'^code/([\w-]+)/$', views.code_detail),
    url(r'^N1/([\w-]+)/$', views.N1_list),
    url(r'^N2/([\w-]+)/$', views.N2_list),
    url(r'^N3/([\w-]+)/$', views.N3_list),
    url(r'^N4/([\w-]+)/$', views.N4GroupByDatasetList.as_view()),
    url(r'^N1/([\w-]+)/Group/([\w-]+)', views.N1_group_detail),
    url(r'^N1/([\w-]+)/Entry/([\w-]+)', views.N1_entry),
    url(r'^N1/Compare/([\w-]+)/([\w-]+)/([\w-]+)/([\w-]+)', views.N1_compare),
    url(r'^N2/([\w-]+)/Group/([\w-]+)', views.N2_group_detail),
    url(r'^N2/([\w-]+)/Entry/([\w-]+)', views.N2_entry),
    url(r'^N3/([\w-]+)/Group/([\w-]+)', views.N3_group_detail),
    url(r'^N3/([\w-]+)/Entry/([\w-]+)', views.N3_entry),
    url(r'^N4/([\w-]+)/Group/([\w-]+)', views.N4_group_detail),
    url(r'^N4/([\w-]+)/Entry/([\w-]+)', views.N4_entry)
]
