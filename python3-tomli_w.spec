Summary:	A lil' TOML writer
Summary(pl.UTF-8):	Malutki moduł do zapisu TOML
Name:		python3-tomli_w
Version:	1.0.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tomli-w/
Source0:	https://files.pythonhosted.org/packages/source/t/tomli-w/tomli_w-%{version}.tar.gz
# Source0-md5:	2c050134d4842b449ec4129c97d51e62
URL:		https://pypi.org/project/tomli-w/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:61
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomli-W is a Python library for writing TOML (<https://toml.io/). It
is a write-only counterpart to Tomli
(<https://github.com/hukkin/tomli>), which is a read-only TOML parser.

Tomli-W is fully compatible with TOML v1.0.0.

%description -l pl.UTF-8
Tomli-W to biblioteka Pythona do zapisu plików w formacie TOML
(<https://toml.io/). Jest to, obsługujący wyłącznie zapis, odpowiednik
modułu Tomli (<https://github.com/hukkin/tomli>), który jest parserem
TOML, obsługującym wyłącznie odczyt.

Tomli-W jest w pełni zgodny z TOML v1.0.0.

%prep
%setup -q -n tomli_w-%{version}

cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/tomli_w
%{py3_sitescriptdir}/tomli_w-%{version}-py*.egg-info
