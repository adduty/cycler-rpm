Name: cycler
Version: 0.10.0
Release: 1%{?dist}
Summary: Composable cycle class used for constructing style-cycles

Group: Development/System
License: BSD
URL: https://pypi.python.org/pypi/Cycler
Source0: %{name}-%{version}.tar.gz

BuildRequires:
Requires:

%description
Composable cycle class used for constructing style-cycles

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc

%changelog
* Thu Jan 16 2016 Andrew Duty <tisbeok@gmail.com> - 0.10.0-1
- Initial package.
