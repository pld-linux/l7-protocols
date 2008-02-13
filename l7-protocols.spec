%define		dashver		2008-02-10
%define		_ver	%(echo %{dashver} | tr - _)
#
Summary:	Protocol definitions files for l7-filter
Summary(pl.UTF-8):	Pliki definicji protokołów dla l7-filter
Name:		l7-protocols
Version:	%{_ver}
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/l7-filter/%{name}-%{dashver}.tar.gz
# Source0-md5:	5e3f980a98fc069ac40a8b6825369d87
URL:		http://l7-filter.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protocol definitions files for use with the Linux Layer 7 Packet
Classifier. These files are regular expressions that define Internet
protocols such as HTTP, MSN Messenger, FTP, Cisco VPN, Fasttrack, DNS,
Gnutella, Quake, etc.

%description -l pl.UTF-8
Pliki definicji protokołów do użytku przez klasyfikator pakietów Layer
7. Pliki te zawierają wyrażenia regularne, które definiują protokoły
takie jak HTTP, MSN Messenger, FTP, Cisco VPN, Fasttrack, DNS,
Gnutella, Quake, itp.

%prep
%setup -qn %{name}-%{dashver}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp -R protocols extra file_types malware $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG HOWTO README WANTED
%{_sysconfdir}/%{name}
