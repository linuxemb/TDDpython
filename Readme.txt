
EF
======================================================================
ERROR: test_root_url_resolve_to_home_page (lists.tests.HomePagetest)
---------------------------------------------------------------------


Test Dummy view
------
Traceback (most recent call last):
  File "C:\myenv\superlists\lists\tests.py", line 13, in test_root_url_resolve_to_home_page
    found = resolve('/')
  File "c:\myenv\lib\site-packages\django\urls\base.py", line 24, in resolve
    return get_resolver(urlconf).resolve(path)
  File "c:\myenv\lib\site-packages\django\urls\resolvers.py", line 585, in resolve
    raise Resolver404({'tried': tried, 'path': new_path})
django.urls.exceptions.Resolver404: {'tried': [[<URLResolver <URLPattern list> (admin:admin) 'admin/'>]], 'path': ''}

======================================================================
FAIL: test_bad_math (lists.tests.SmokeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\myenv\superlists\lists\tests.py", line 9, in test_bad_math
    self.assertEqual(1+1,3)


====
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\myenv\superlists\superlists\urls.py", line 27, in <module>
    url(r'^$', views.home_page, name='home'),
  File "c:\myenv\lib\site-packages\django\conf\urls\__init__.py", line 22, in url
    return re_path(regex, view, kwargs, name)
  File "c:\myenv\lib\site-packages\django\urls\conf.py", line 73, in _path
    raise TypeError('view must be a callable or a list/tuple in the case of include().')
TypeError: view must be a callable or a list/tuple in the case of include().

=====after add views.py  homepage() pass================


(myenv) C:\myenv\superlists>python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F
======================================================================
FAIL: test_bad_math (lists.tests.SmokeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\myenv\superlists\lists\tests.py", line 9, in test_bad_math
    self.assertEqual(1+1,3)
AssertionError: 2 != 3

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (failures=1)
Destroying test database for alias 'default'...

(myenv) C:\myenv\superlists>