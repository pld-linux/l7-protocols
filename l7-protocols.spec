%define		dashver		2005-11-05
#
Summary:	Protocol definitions files for l7-filter
Summary(pl):	Pliki definicji protoko³ów dla l7-filter
Name:		l7-protocols
Version:	2005_11_05
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/l7-filter/%{name}-%{dashver}.tar.gz
# Source0-md5:	589094d074cc047de65c957314675266
URL:		http://l7-filter.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protocol definitions files for use with the Linux Layer 7 Packet
Classifier. These files are regular expressions that define Internet
protocols such as HTTP, MSN Messenger, FTP, Cisco VPN, Fasttrack, DNS,
Gnutella, Quake, etc.

%description -l pl
Pliki definicji protoko³ów do u¿ytku przez klasyfikator pakietów Layer
7. Pliki te zawieraj± wyra¿enia regularne, które definiuj± protoko³y
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
%doc CHANGELOG README HOWTO WANTED
%{_sysconfdir}/%{name}
