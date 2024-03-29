#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-nose
Version  : 1.4.7
Release  : 58
URL      : https://files.pythonhosted.org/packages/4c/d6/a340da9854cf0a2b54e23cf9147911b1e15a831911428983dd0158572ce9/django-nose-1.4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/d6/a340da9854cf0a2b54e23cf9147911b1e15a831911428983dd0158572ce9/django-nose-1.4.7.tar.gz
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
Requires: dj-database-url
Requires: flake8
Requires: flake8-docstrings
Requires: ipdb
Requires: ipdbplugin
Requires: ipython
Requires: nose
Requires: pyroma
Requires: tox
Requires: twine
Requires: wheel
BuildRequires : Django
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : check-manifest
BuildRequires : coverage
BuildRequires : dj-database-url
BuildRequires : flake8
BuildRequires : flake8-docstrings
BuildRequires : ipdb
BuildRequires : ipdbplugin
BuildRequires : ipython
BuildRequires : nose
BuildRequires : pyroma
BuildRequires : tox
BuildRequires : twine
BuildRequires : wheel

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
Provides: pypi(django_nose)
Requires: pypi(nose)

%description python3
python3 components for the django-nose package.


%prep
%setup -q -n django-nose-1.4.7
cd %{_builddir}/django-nose-1.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635724217
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-nose
cp %{_builddir}/django-nose-1.4.7/LICENSE %{buildroot}/usr/share/package-licenses/django-nose/abeb4d52f5efe6fc97782177199726a557c65aa8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-nose/abeb4d52f5efe6fc97782177199726a557c65aa8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
