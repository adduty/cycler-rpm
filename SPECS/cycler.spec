Name: cycler
Version: 0.10.0
Release: 1%{?dist}
Summary: Composable cycle class used for constructing style-cycles

Group: Development/System
License: BSD
URL: https://pypi.python.org/pypi/Cycler
Source0: %{name}-%{version}.tar.gz

BuildRequires: python >= 2.6
BuildRequires: python <= 3
Requires: python >= 2.6
Requires: python <= 3

%description
Composable cycle class used for constructing style-cycles

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{python2_sitelib}/cycler-%{version}-py2.7.egg-info/*
%{python2_sitelib}/cycler.py*

%changelog
* Thu Jan 16 2016 Andrew Duty <tisbeok@gmail.com> - 0.10.0-1
- Initial package.
