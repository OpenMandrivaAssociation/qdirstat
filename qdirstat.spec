Summary:	Qt-based directory statistics
Name:		qdirstat
Version:	1.9
Release:	1
License:	GPLv2
URL:		https://github.com/shundhammer/qdirstat
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.appdata.xml
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme

%description
QDirStat is a graphical application to show where your disk space has gone
and to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
 latest Qt 5. It does not need any KDE libs or infrastructure. It runs on
 every X11-based desktop on Linux, BSD and other Unix-like systems.

%prep
%autosetup -p1

%build
%{qmake_qt5}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/qdirstat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%{_bindir}/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc %{_mandir}/man1/qdirstat-cache-writer.1.*
%doc %{_mandir}/man1/qdirstat.1.*
%doc %{_docdir}/%{name}/
