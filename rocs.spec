%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graph - Editor and a Programming Environment
Name:		rocs
Version:	25.12.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/rocs
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:	cmake
BuildRequires:	boost-devel
BuildRequires:	grantlee-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6TextWidgets)

BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Test)

%description
Rocs aims to be a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.
Rocs has a scripting module, done in Qt Script, that interacts with the drawn
graph and every change in the graph with the script is reflected on the drawn
one.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.rocs.desktop
%{_datadir}/rocs
%{_bindir}/rocs
%{_datadir}/metainfo/org.kde.rocs.appdata.xml
%{_datadir}/config.kcfg/rocs.kcfg
%{_iconsdir}/hicolor/*/apps/rocs.*
%{_iconsdir}/hicolor/*/actions/rocs*
%{_qtdir}/plugins/rocs

#---------------------------------------------

%libpackage rocsgraphtheory 0

#---------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{mklibname rocsgraphtheory} = %{EVRD}
Requires:	boost-devel
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/rocs
%{_libdir}/librocsgraphtheory.so
