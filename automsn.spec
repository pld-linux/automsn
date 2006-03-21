Summary:	AutoMSN Emoticon Scraper
Name:		automsn
Version:	1.1.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.kde-apps.org/content/files/28315-%{name}
# Source0-md5:	a54f65d6637eee58dc2817ac1d760010
Patch0:		%{name}.patch
URL:		http://www.kde-apps.org/content/show.php?content=28315
BuildRequires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	%{_datadir}/emoticons/AutoMSN

%description
This Perl script downloads the emoticons (smileys) from
messenger.msn.com and sets them up for use in e.g. Kopete.

No icons are included here. This simply automates the process of
downloading each icon and setting up an appropriate emoticons.xml
file.

%package -n kde-emoticons-AutoMSN
Summary:	MSN emoticons for KDE
Summary(pl):	Emotikony MSN dla KDE
License:	not distributable
Group:		Themes
URL:		http://messenger.msn.com/resource/emoticons.aspx
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description -n kde-emoticons-AutoMSN
MSN emoticons for KDE applications.

%prep
%setup -qcT
install %{SOURCE0} automsn
%patch0 -p1

%build
./automsn theme < /dev/null

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}
install -D automsn $RPM_BUILD_ROOT%{_bindir}/automsn
cp -a theme/* $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/automsn

%files -n kde-emoticons-AutoMSN
%defattr(644,root,root,755)
%{_themedir}
