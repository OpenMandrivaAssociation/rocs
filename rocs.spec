Name:		rocs
Summary:	Graph - Editor and a Programming Environement
Version:	4.8.97
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://edu.kde.org/rocs
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	boost-devel

%description
Rocs aims to be a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.
Rocs has a scripting module, done in Qt Script, that interacts with the drawn
graph and every change in the graph with the script is reflected on the drawn
one.

%files
%doc AUTHORS COPYING COPYING.LIB.LGPL-2 COPYING.LIB.LGPL-2.1 COPYING.DOC README HACKING.txt 
%doc %{_kde_docdir}/HTML/en/rocs
%{_kde_bindir}/rocs
%{_kde_appsdir}/rocs
%{_kde_appsdir}/rocs_rootedtree
%{_kde_applicationsdir}/rocs.desktop
%{_kde_datadir}/config.kcfg/rocs.kcfg
%{_kde_configdir}/rocs.knsrc
%{_kde_libdir}/kde4/rocs_plaintxt.so
%{_kde_libdir}/kde4/rocs_GraphStructure.so
%{_kde_libdir}/kde4/rocs_ListStructure.so
%{_kde_libdir}/kde4/rocs_assignvaluesplugin.so
%{_kde_libdir}/kde4/rocs_generategraphplugin.so
%{_kde_libdir}/kde4/rocs_transformedgesplugin.so
%{_kde_libdir}/kde4/rocs_GMLParser.so
%{_kde_libdir}/kde4/rocs_dotFilePlugin.so
%{_kde_libdir}/kde4/rocs_RootedTreeStructure.so
%{_kde_services}/rocs_GMLParser.desktop
%{_kde_services}/rocs_dotFilePlugin.desktop
%{_kde_services}/rocs_plaintxtplugin.desktop
%{_kde_services}/rocs_GraphStructure.desktop
%{_kde_services}/rocs_ListStructure.desktop
%{_kde_services}/rocs_assignvaluesplugin.desktop
%{_kde_services}/rocs_generategraphplugin.desktop
%{_kde_services}/rocs_transformedgesplugin.desktop
%{_kde_services}/rocs_RootedTreeStructure.desktop
%{_kde_servicetypes}/RocsFilePlugin.desktop
%{_kde_servicetypes}/RocsToolsPlugin.desktop
%{_kde_servicetypes}/RocsDataStructurePlugin.desktop

#---------------------------------------------

%define rocslib_major 4
%define librocslib %mklibname rocslib %{rocslib_major}

%package -n %{librocslib}
Summary:	Runtime library for Rocs
Group:		System/Libraries

%description -n %{librocslib}
Runtime library for Rocs

%files -n %{librocslib}
%{_kde_libdir}/librocslib.so.%{rocslib_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{librocslib} = %{EVRD}
Requires:	boost-devel
Conflicts:	kdeedu4-devel < 4.6.90

%description  devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/rocs
%{_kde_libdir}/librocslib.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

