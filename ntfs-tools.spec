Summary:	User level tools a la mtools to access an NTFS volume
Summary(pl):	Narzêdzia w stylu mtools do partycji NTFS
Name:		ntfs-tools
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://prdownloads.sf.net/%{name}/orig-%{name}-%{version}.tar.bz2
URL:		http://linux-ntfs.sf.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User level tools a la mtools to access an NTFS volume.

%description -l pl
Narzêdzia w stylu mtools do partycji NTFS.

%prep
%setup -q -n ntfs

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ntcat ntchange ntcp ntdir ntdump ntgrep ntmkdir $RPM_BUILD_ROOT%{_bindir}
# mkntfs not included - it's in more recent linux-ntfs package

gzip -9nf HACKING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/*
