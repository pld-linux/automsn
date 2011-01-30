#
# Conditional build:
%bcond_with	fetch	# fetch icons and package them
#
Summary:	AutoMSN Emoticon Scraper
Summary(pl.UTF-8):	AutoMSN - narzędzie do wycinania emotikonów
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

%description -l pl.UTF-8
Ten skrypt Perla ściąga emotikony (uśmieszki) z messenger.msn.com i
ustawia je do wykorzystania np. w Kopete.

Nie zawiera on ikon. Po prostu automatyzuje proces ściągania każdej
ikony i właściwej konfiguracji pliku emoticons.xml.

%package -n kde-emoticons-AutoMSN
Summary:	MSN emoticons for KDE
Summary(pl.UTF-8):	Emotikony MSN dla KDE
License:	not distributable
Group:		Themes
URL:		http://messenger.msn.com/resource/emoticons.aspx
Requires:	kdelibs

%description -n kde-emoticons-AutoMSN
MSN emoticons for KDE applications.

%description -n kde-emoticons-AutoMSN -l pl.UTF-8
Emotikony MSN dla aplikacji KDE.

%prep
%setup -qcT
install %{SOURCE0} automsn
%patch0 -p1

%build
%if %{with fetch}
./automsn theme < /dev/null
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -D automsn $RPM_BUILD_ROOT%{_bindir}/automsn

%if %{with fetch}
install -d $RPM_BUILD_ROOT%{_themedir}
cp -a theme/* $RPM_BUILD_ROOT%{_themedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/automsn

%if %{with fetch}
%files -n kde-emoticons-AutoMSN
%defattr(644,root,root,755)
%{_themedir}
%endif
