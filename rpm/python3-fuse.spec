# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -Ic "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-fuse
Summary:    Python 3.x bindings for libfuse 2.x
Version:    1.0.0
Release:    1
Group:      Development/Languages
License:    LGPLv2.1
URL:        https://github.com/libfuse/python-fuse
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(fuse)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This is a Python interface to libfuse (https://github.com/libfuse/libfuse).

%prep
%setup -q -n %{name}-%{version}/python-fuse

%build
CFLAGS="%{optflags}" %{__python3} setup.py build %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING
%doc AUTHORS FAQ README.md README.new_fusepy_api example
%{python3_sitearch}/*
