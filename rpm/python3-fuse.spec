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
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%license COPYING
%doc AUTHORS FAQ README.md README.new_fusepy_api example
%{python3_sitearch}/*
