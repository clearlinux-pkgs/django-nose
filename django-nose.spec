#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-nose
Version  : 1.4.6
Release  : 32
URL      : https://files.pythonhosted.org/packages/91/b4/0f84946a3f18c1b1c75c9eac8272f684dc1f3815b24c4941d59d433d8886/django-nose-1.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/b4/0f84946a3f18c1b1c75c9eac8272f684dc1f3815b24c4941d59d433d8886/django-nose-1.4.6.tar.gz
Summary  : Makes your Django tests simple and snappy
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-nose-license = %{version}-%{release}
Requires: django-nose-python = %{version}-%{release}
Requires: django-nose-python3 = %{version}-%{release}
Requires: Django
Requires: Sphinx
Requires: check-manifest
Requires: coverage
Requires: flake8
Requires: flake8-docstrings
Requires: ipdb
Requires: ipdbplugin
Requires: ipython
Requires: nose
Requires: pyroma
Requires: tox
Requires: wheel
BuildRequires : Django
BuildRequires : buildreq-distutils3
BuildRequires : nose

%description
===========
        django-nose
        ===========

%package license
Summary: license components for the django-nose package.
Group: Default

%description license
license components for the django-nose package.


%package python
Summary: python components for the django-nose package.
Group: Default
Requires: django-nose-python3 = %{version}-%{release}

%description python
python components for the django-nose package.


%package python3
Summary: python3 components for the django-nose package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django-nose package.


%prep
%setup -q -n django-nose-1.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541265917
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-nose
cp LICENSE %{buildroot}/usr/share/package-licenses/django-nose/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-nose/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
