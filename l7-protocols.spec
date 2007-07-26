%define		dashver		2007-06-22
#
Summary:	Protocol definitions files for l7-filter
Summary(pl.UTF-8):	Pliki definicji protokołów dla l7-filter
Name:		l7-protocols
Version:	2007_06_22
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/l7-filter/%{name}-%{dashver}.tar.gz
# Source0-md5:	4aa55ea4f81b7978c9b9ebdbcf7d8ff8
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
