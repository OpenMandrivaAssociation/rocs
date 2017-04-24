Summary:	Graph - Editor and a Programming Environement
Name:		rocs
Version:	17.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/rocs
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	grantlee-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Grantlee5)

BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5XmlGui)

BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5ScriptTools)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5Test)

%description
Rocs aims to be a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.
Rocs has a scripting module, done in Qt Script, that interacts with the drawn
graph and every change in the graph with the script is reflected on the drawn
one.

%files -f all.lang
%{_datadir}/applications/org.kde.rocs.desktop
%{_datadir}/rocs
%{_datadir}/kxmlgui5/rocs
%{_bindir}/rocs
%{_datadir}/metainfo/org.kde.rocs.appdata.xml
%{_datadir}/config.kcfg/rocs.kcfg
%{_iconsdir}/hicolor/*/apps/rocs.*
%{_iconsdir}/hicolor/*/actions/rocs*

%{_qt5_plugindir}/rocs

#---------------------------------------------

%libpackage rocsgraphtheory 0

#---------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{mklibname rocsgraphtheory 0} = %{EVRD}
Requires:	boost-devel
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%doc AUTHORS COPYING.GPL2 COPYING.LIB.LGPL-2.1 COPYING.DOC README
%{_includedir}/rocs
%{_libdir}/librocsgraphtheory.so
#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang rocs --with-html
%find_lang libgraphtheory
cat *.lang >all.lang
