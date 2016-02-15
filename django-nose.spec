#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-nose
Version  : 1.4.2
Release  : 14
URL      : https://pypi.python.org/packages/source/d/django-nose/django-nose-1.4.2.tar.gz
Source0  : https://pypi.python.org/packages/source/d/django-nose/django-nose-1.4.2.tar.gz
Summary  : Makes your Django tests simple and snappy
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-nose-python
BuildRequires : Django-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : south-python

%description
===========
django-nose
===========
.. image:: https://img.shields.io/pypi/v/django-nose.svg
:alt: The PyPI package
:target: https://pypi.python.org/pypi/django-nose

%package python
Summary: python components for the django-nose package.
Group: Default
Requires: Django-python
Requires: nose-python

%description python
python components for the django-nose package.


%prep
%setup -q -n django-nose-1.4.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
