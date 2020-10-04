Summary:	Decompress Mozilla Firefox bookmarks backup files
Summary(pl.UTF-8):	Rozpakowywanie plików kopii zapasowych zakładek Mozilla Firefoksa
Name:		dejsonlz4
Version:	1.1
Release:	1
License:	BSD-like
Group:		Applications/File
#Source0Download: https://github.com/avih/dejsonlz4/releases
Source0:	https://github.com/avih/dejsonlz4/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d42776a24de83bea90767be8fcde261d
URL:		https://github.com/avih/dejsonlz4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Decompress Mozilla Firefox bookmarks backup files.

%description -l pl.UTF-8
Rozpakowywanie plików kopii zapasowych zakładek Mozilla Firefoksa.

%prep
%setup -q

%build
cd src
%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -Wall -o dejsonlz4 dejsonlz4.c lz4.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/dejsonlz4 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/dejsonlz4
